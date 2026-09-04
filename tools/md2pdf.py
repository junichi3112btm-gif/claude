#!/usr/bin/env python3
"""Markdown（本リポジトリで使う部分集合）→ HTML → PDF。

LibreOffice が pptx/docx を変換できない環境（CLAUDE.md §9）で、md の対外文書を PDF にする経路。
依存：同梱 Chromium（/opt/pw-browsers/chromium*）。pandoc・python-docx・reportlab は不要。

対応する記法：# 見出し／段落／**太字**／*斜体*／`コード`／- 箇条書き／1. 番号付き／| 表 |／---（改ページ）。

使い方：
    python3 tools/md2pdf.py <input.md> <output.pdf> [--title "..."]
"""
from __future__ import annotations

import argparse
import glob
import html
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

CSS = """
@page { size: A4; margin: 13mm 14mm 13mm 14mm; }
body { font-family: "Helvetica Neue", Helvetica, Arial, "Noto Sans", "Noto Sans CJK JP", sans-serif;
       font-size: 9.3pt; line-height: 1.30; color: #1a1a1a; }
h1 { font-size: 17pt; margin: 0 0 6pt; line-height: 1.25; }
h2 { font-size: 12pt; margin: 11pt 0 4pt; padding-bottom: 2pt; border-bottom: 1px solid #999; }
h3 { font-size: 10.8pt; margin: 10pt 0 3pt; }
p  { margin: 0 0 4.5pt; }
ul, ol { margin: 0 0 6pt 18pt; padding: 0; }
li { margin: 0 0 2pt; }
table { border-collapse: collapse; width: 100%; margin: 4pt 0 8pt; font-size: 8.8pt; }
th, td { border: 1px solid #bbb; padding: 3pt 5pt; vertical-align: top; text-align: left; }
th { background: #f0f0f0; }
code { font-family: Menlo, Consolas, monospace; font-size: 9pt; background: #f4f4f4; padding: 0 2pt; }
hr { border: 0; border-top: 1px solid #ccc; margin: 10pt 0; }
em { color: #333; }
"""

INLINE = [
    (re.compile(r"\*\*(.+?)\*\*"), r"<strong>\1</strong>"),
    (re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)"), r"<em>\1</em>"),
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
]


def inline(text: str) -> str:
    out = html.escape(text, quote=False)
    for pat, rep in INLINE:
        out = pat.sub(rep, out)
    return out


def table_html(rows: list[str]) -> str:
    cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
    # 2行目がアラインメント行なら除去
    body = cells
    header = None
    if len(cells) >= 2 and all(re.fullmatch(r":?-{2,}:?", c) or c == "" for c in cells[1]):
        header, body = cells[0], cells[2:]
    parts = ["<table>"]
    if header is not None and any(header):
        parts.append("<tr>" + "".join(f"<th>{inline(c)}</th>" for c in header) + "</tr>")
    elif header is not None:
        pass
    for r in body:
        parts.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    parts.append("</table>")
    return "\n".join(parts)


def md_to_html(md: str, title: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    para: list[str] = []
    list_type: str | None = None

    def flush_para():
        nonlocal para
        if para:
            out.append(f"<p>{inline(' '.join(para))}</p>")
            para = []

    def close_list():
        nonlocal list_type
        if list_type:
            out.append(f"</{list_type}>")
            list_type = None

    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            flush_para(); close_list(); i += 1; continue
        if s.startswith("|"):
            flush_para(); close_list()
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i]); i += 1
            out.append(table_html(rows)); continue
        m = re.match(r"^(#{1,3})\s+(.*)$", s)
        if m:
            flush_para(); close_list()
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>"); i += 1; continue
        if s == "---":
            flush_para(); close_list(); out.append("<hr>"); i += 1; continue
        m = re.match(r"^[-*]\s+(.*)$", s)
        if m:
            flush_para()
            if list_type != "ul":
                close_list(); out.append("<ul>"); list_type = "ul"
            out.append(f"<li>{inline(m.group(1))}</li>"); i += 1; continue
        m = re.match(r"^\d+\.\s+(.*)$", s)
        if m:
            flush_para()
            if list_type != "ol":
                close_list(); out.append("<ol>"); list_type = "ol"
            out.append(f"<li>{inline(m.group(1))}</li>"); i += 1; continue
        if s.startswith(">"):
            s = s.lstrip("> ").strip()
        close_list()
        para.append(s); i += 1
    flush_para(); close_list()
    body = "\n".join(out)
    return f"<!doctype html><html><head><meta charset='utf-8'><title>{html.escape(title)}</title><style>{CSS}</style></head><body>{body}</body></html>"


def find_chromium() -> str:
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome", "/opt/pw-browsers/chromium*/chrome-linux/chrome",
                "/opt/pw-browsers/chromium_headless_shell-*/chrome-linux/headless_shell"):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    for name in ("chromium", "chromium-browser", "google-chrome"):
        p = subprocess.run(["which", name], capture_output=True, text=True).stdout.strip()
        if p:
            return p
    raise SystemExit("Chromium が見つからない（/opt/pw-browsers 配下を確認）")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("src"); ap.add_argument("dst"); ap.add_argument("--title", default=None)
    a = ap.parse_args()
    src, dst = Path(a.src), Path(a.dst)
    md = src.read_text(encoding="utf-8")
    title = a.title or next((l.lstrip("# ").strip() for l in md.splitlines() if l.startswith("# ")), src.stem)
    html_text = md_to_html(md, title)
    with tempfile.TemporaryDirectory() as td:
        hp = Path(td) / "doc.html"
        hp.write_text(html_text, encoding="utf-8")
        chrome = find_chromium()
        cmd = [chrome, "--headless=new", "--disable-gpu", "--no-sandbox", "--no-pdf-header-footer",
               f"--print-to-pdf={dst.resolve()}", f"--user-data-dir={td}/prof", hp.resolve().as_uri()]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if not dst.exists():
            sys.stderr.write(r.stdout + r.stderr)
            return 1
    pages = len(re.findall(rb"/Type\s*/Page[^s]", dst.read_bytes()))
    print(f"wrote {dst} ({dst.stat().st_size:,} bytes, ~{pages} pages)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
