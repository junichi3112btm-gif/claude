#!/usr/bin/env python3
"""対外文書の送付前検証。

2026年8月28日の送付前検証で、検査式に起因する誤判定が4件発生した（文書側はすべて正しかった）。
そこから導いた日本語文書の機械照合の3原則を、このスクリプトが実装している。

  原則1  空白・改行を除去してから照合する
         → PDFの行折り返しで語が分断され、偽陰性が出る
  原則2  数値は単位語を含めた原文で照合する
         → 「2億5,426万円」を「25426」で探すと、間の「億」で不一致になる
  原則3  検索語は当該節に固有の長さを確保する
         → 短い語は他節を拾う。全出現箇所を節つきで報告して人が判断できるようにする

使い方:
    python3 tools/verify.py --doc dglobal/対外版.md --profile external
    python3 tools/verify.py --doc deck.pptx --profile deck --recompute
    python3 tools/verify.py --list-profiles

終了コード: 0=合格 / 1=不合格（禁止語の残存、必須語の欠落、数値の不一致）
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML が必要です:  pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RULES = ROOT / "tools" / "verify_rules.yaml"

# 原則3: これより短い検索語は他節を拾いうるため警告する
SHORT_TERM_THRESHOLD = 4


# ────────────────────────────────────────────────────────────
# 本文の取り出し
# ────────────────────────────────────────────────────────────

@dataclass
class Segment:
    """本文の一区画。節・ページ・スライドのいずれか。"""
    label: str
    text: str


@dataclass
class Document:
    path: Path
    segments: list[Segment]

    @property
    def raw(self) -> str:
        return "\n".join(s.text for s in self.segments)


_HTML_COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def _load_markdown(path: Path, skip_html_comments: bool = False) -> list[Segment]:
    """見出しごとに区切る。見出しが無ければ全体を1区画とする。

    skip_html_comments: 内部メタデータ（HTMLコメント）を本文から外す。
      内部正本のメタデータは「除去した語」を説明のために書いているため、
      そのまま照合すると禁止語の偽陽性になる。
      対外版の検証では**必ず False**にする ── コメントの残存自体が検出対象であるため。
    """
    text = path.read_text(encoding="utf-8")
    if skip_html_comments:
        text = _HTML_COMMENT.sub("", text)
    segments: list[Segment] = []
    label, buf = "（冒頭）", []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            if buf:
                segments.append(Segment(label, "\n".join(buf)))
            label, buf = m.group(2).strip(), [line]
        else:
            buf.append(line)
    if buf:
        segments.append(Segment(label, "\n".join(buf)))
    return segments or [Segment("（全体）", text)]


def _load_pptx(path: Path) -> list[Segment]:
    """python-pptx に依存せず、zip 内の XML から <a:t> を拾う。

    ノート（登壇原稿）も必ず読む。スライドを伏せても原稿に実名が残れば口頭で露出するため。
    """
    segments: list[Segment] = []
    with zipfile.ZipFile(path) as z:
        names = z.namelist()

        def _num(n: str) -> int:
            m = re.search(r"(\d+)\.xml$", n)
            return int(m.group(1)) if m else 0

        slides = sorted((n for n in names if re.match(r"ppt/slides/slide\d+\.xml$", n)), key=_num)
        notes = sorted((n for n in names if re.match(r"ppt/notesSlides/notesSlide\d+\.xml$", n)), key=_num)
        for group, kind in ((slides, "slide"), (notes, "notes")):
            for name in group:
                xml = z.read(name).decode("utf-8", errors="replace")
                runs = re.findall(r"<a:t>(.*?)</a:t>", xml, re.DOTALL)
                body = "".join(runs)
                body = (body.replace("&amp;", "&").replace("&lt;", "<")
                            .replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'"))
                segments.append(Segment(f"{kind}{_num(name)}", body))
    return segments


def _load_pdf(path: Path) -> list[Segment]:
    try:
        from pypdf import PdfReader           # type: ignore
    except ImportError:
        try:
            from PyPDF2 import PdfReader      # type: ignore
        except ImportError:
            sys.exit(
                "PDF を読むには pypdf が必要です:  pip install pypdf\n"
                "（.md の正本に対して検証すれば依存なしで実行できます）"
            )
    reader = PdfReader(str(path))
    return [Segment(f"p{i}", (pg.extract_text() or "")) for i, pg in enumerate(reader.pages, 1)]


def load_document(path: Path, skip_html_comments: bool = False) -> Document:
    suffix = path.suffix.lower()
    if suffix in (".md", ".txt", ".markdown"):
        segs = _load_markdown(path, skip_html_comments)
    elif suffix == ".pptx":
        segs = _load_pptx(path)
    elif suffix == ".pdf":
        segs = _load_pdf(path)
    else:
        sys.exit(f"未対応の形式です: {suffix}（.md / .txt / .pptx / .pdf）")
    return Document(path, segs)


# ────────────────────────────────────────────────────────────
# 原則1: 空白除去後の照合
# ────────────────────────────────────────────────────────────

_WS = re.compile(r"[\s　 ​\-‐-―ー]+")


def normalize(text: str) -> str:
    """NFKC 正規化 → 空白・改行・各種ハイフンを除去。

    PDF の行折り返しで語が分断されても一致するようにする。
    2026/08/28 の偽陰性1件（§1 の仮値注記が行折り返しで未検出）はこれで消える。
    """
    return _WS.sub("", unicodedata.normalize("NFKC", text))


def find_all(doc: Document, term: str) -> list[tuple[str, int]]:
    """正規化後に照合し、(区画ラベル, 件数) を全件返す。

    原則3: 最初の一致で打ち切らない。短い語が他節を拾っていることが目で見えるようにする。
    """
    needle = normalize(term)
    if not needle:
        return []
    hits = []
    for seg in doc.segments:
        n = normalize(seg.text).count(needle)
        if n:
            hits.append((seg.label, n))
    return hits


# ────────────────────────────────────────────────────────────
# 判定
# ────────────────────────────────────────────────────────────

@dataclass
class Finding:
    level: str            # NG / WARN / OK
    category: str
    term: str
    detail: str
    hits: list[tuple[str, int]] = field(default_factory=list)


def check_forbidden(doc: Document, rules: list) -> list[Finding]:
    """残存してはならない語。1件でも出れば NG。"""
    out = []
    for item in rules:
        term, why, allow = _unpack(item)
        hits = find_all(doc, term)
        hits = [(lbl, n) for lbl, n in hits if not _excused(lbl, allow)]
        if hits:
            out.append(Finding("NG", "禁止語", term, why, hits))
        else:
            out.append(Finding("OK", "禁止語", term, why))
    return out


def check_required(doc: Document, rules: list) -> list[Finding]:
    """保持されていなければならない語（是正の維持）。欠落すれば NG。"""
    out = []
    for item in rules:
        term, why, _ = _unpack(item)
        hits = find_all(doc, term)
        if hits:
            out.append(Finding("OK", "保持必須", term, why, hits))
        else:
            out.append(Finding("NG", "保持必須", term, why))
    return out


def check_numbers(doc: Document, rules: list) -> list[Finding]:
    """原則2: 数値は単位語込みの原文で照合する。

    'expect' に「2億5,426万円」のような表示形をそのまま書く。
    'formula' があれば Python 式として評価し、'expect' と突き合わせる。
    """
    out = []
    for item in rules:
        label = item.get("label", "")
        expect = str(item.get("expect", ""))
        formula = item.get("formula")
        detail = item.get("note", "")

        if formula:
            try:
                got = eval(formula, {"__builtins__": {}}, {})  # noqa: S307 — 設定は自分で書いたもの
            except Exception as exc:
                out.append(Finding("NG", "数値", label, f"算式の評価に失敗: {exc}"))
                continue
            want = float(re.sub(r"[^\d.\-]", "", expect) or "nan")
            if abs(got - want) > float(item.get("tol", 0.5)):
                out.append(Finding(
                    "NG", "数値", label,
                    f"算式 {formula} ＝ {got:,.4g} だが期待値は {expect}。{detail}"))
                continue

        hits = find_all(doc, expect)
        if hits:
            out.append(Finding("OK", "数値", label, f"{expect} を確認。{detail}", hits))
        else:
            out.append(Finding(
                "NG", "数値", label,
                f"{expect} が本文に見当たらない（単位語込みの原文で照合済）。{detail}"))
    return out


def check_short_terms(doc: Document, rules_all: list[list]) -> list[Finding]:
    """原則3: 検索語が短すぎると他節を拾う。設定そのものへの警告。

    全出現箇所を併記する。2026/08/28 の偽陽性3件（短い検索語が他節にも出現し、
    最初の一致ページを拾った）は、最初の一致で打ち切ったことが原因だった。
    """
    out = []
    seen = set()
    for rules in rules_all:
        for item in rules:
            term, _, _ = _unpack(item)
            if not term or term in seen:
                continue
            seen.add(term)
            if len(normalize(term)) < SHORT_TERM_THRESHOLD:
                hits = find_all(doc, term)
                out.append(Finding(
                    "WARN", "検索語", term,
                    f"検索語が {len(normalize(term))} 文字で短い。"
                    "他節を拾いうるため、下記の全出現箇所を目視で確認すること",
                    hits))
    return out


def _unpack(item) -> tuple[str, str, list[str]]:
    if isinstance(item, str):
        return item, "", []
    return (str(item.get("term", "")),
            str(item.get("why", "")),
            list(item.get("allow_in", []) or []))


def _excused(label: str, allow: list[str]) -> bool:
    """正当な例外（例: §13 出典の「執行計画書 第1.5版」は別文書の版）。"""
    return any(normalize(a) in normalize(label) for a in allow)


# ────────────────────────────────────────────────────────────
# 出力
# ────────────────────────────────────────────────────────────

def report(doc: Document, findings: list[Finding], verbose: bool) -> int:
    ng = [f for f in findings if f.level == "NG"]
    warn = [f for f in findings if f.level == "WARN"]
    ok = [f for f in findings if f.level == "OK"]

    print(f"\n検証対象: {doc.path}")
    print(f"区画数  : {len(doc.segments)}（{', '.join(s.label for s in doc.segments[:6])}"
          f"{' …' if len(doc.segments) > 6 else ''}）")
    print("─" * 70)

    for f in ng:
        print(f"  ✗ NG   [{f.category}] {f.term}")
        if f.detail:
            print(f"          {f.detail}")
        for lbl, n in f.hits:
            print(f"          → {lbl} に {n}件")

    for f in warn:
        print(f"  ! WARN [{f.category}] {f.term}")
        print(f"          {f.detail}")
        for lbl, n in f.hits:
            print(f"          → {lbl} に {n}件")

    if verbose:
        for f in ok:
            loc = "／".join(f"{lbl}×{n}" for lbl, n in f.hits) if f.hits else "0件"
            print(f"  ✓ OK   [{f.category}] {f.term}  （{loc}）")

    print("─" * 70)
    print(f"合格 {len(ok)}  警告 {len(warn)}  不合格 {len(ng)}")
    if ng:
        print("\n判定: 不合格。上記 NG を解消するまで対外提示は不可。")
        return 1
    print("\n判定: 合格。" + ("（警告は検索語の設計に関するもので、文書側の欠陥ではない）" if warn else ""))
    return 0


# ────────────────────────────────────────────────────────────

def main() -> int:
    ap = argparse.ArgumentParser(description="対外文書の送付前検証（日本語照合の3原則を実装）")
    ap.add_argument("--doc", type=Path, help="検証対象（.md / .txt / .pptx / .pdf）")
    ap.add_argument("--rules", type=Path, default=DEFAULT_RULES, help="ルールファイル（YAML）")
    ap.add_argument("--profile", default="external", help="適用するプロファイル名")
    ap.add_argument("--recompute", action="store_true", help="数値の算式を再計算して照合する")
    ap.add_argument("--list-profiles", action="store_true", help="プロファイル一覧を表示して終了")
    ap.add_argument("-v", "--verbose", action="store_true", help="合格項目も表示する")
    args = ap.parse_args()

    rules_doc = yaml.safe_load(args.rules.read_text(encoding="utf-8"))
    profiles = rules_doc.get("profiles", {})

    if args.list_profiles:
        for name, p in profiles.items():
            print(f"{name:12s} {p.get('description', '')}")
        return 0

    if not args.doc:
        ap.error("--doc を指定してください")
    if args.profile not in profiles:
        sys.exit(f"プロファイル '{args.profile}' が無い。--list-profiles で確認できる。")

    prof = profiles[args.profile]
    common = rules_doc.get("common", {})

    def merged(key: str) -> list:
        return list(common.get(key, []) or []) + list(prof.get(key, []) or [])

    forbidden, required, numbers = merged("forbidden"), merged("required"), merged("numbers")

    skip_comments = bool(prof.get("skip_html_comments", False))
    doc = load_document(args.doc, skip_comments)
    if skip_comments:
        print("\n注記: 内部メタデータ（HTMLコメント）を本文から除外して照合している"
              "（プロファイル設定 skip_html_comments）。")
    findings: list[Finding] = []
    findings += check_forbidden(doc, forbidden)
    findings += check_required(doc, required)
    if args.recompute and numbers:
        findings += check_numbers(doc, numbers)
    findings += check_short_terms(doc, [forbidden, required])

    return report(doc, findings, args.verbose)


if __name__ == "__main__":
    sys.exit(main())
