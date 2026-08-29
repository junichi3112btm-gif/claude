# スキル

## リポジトリ内スキル（本ディレクトリ）

| スキル | 用途 |
| :-- | :-- |
| `doc-critique` | CSO としてレッドチーム検証し、5基準で走査・分級して PASS/REVISE/BLOCK を判定する |
| `external-version` | 内部正本から対外版を生成し、検証4層をかける |
| `number-propagation` | 数値を1つ変更したとき、波及先を数値台帳から全走査する |
| `notes-to-onepager` | 雑然としたメモを1ページまとめに変換する |
| `checkin` | セッション開始時の定例確認（Gmail・Drive の走査 → 1〜3行報告 → 本作業） |

## アカウント側スキルの整理（要手動対応）

`notes-to-onepager` と `messy-notes-to-onepager` は**同一のスキルが2本登録されている**状態。
規則・出力フォーマット・使用例まで一致し、description のトリガー文言もほぼ同じため、
どちらが起動するか不定になる。片方だけを改良すると挙動が割れる。

| 登録名 | skillId | 最終更新 |
| :-- | :-- | :-- |
| notes-to-onepager | `skill_01ECQBH8tqF759fJJokmLjuz` | 2026-07-14 18:01 |
| messy-notes-to-onepager | `skill_01FpKNcmmqU955vAVozfV6gm` | 2026-07-15 11:35 |

差分は文言のみで、規則の実質的な違いは無い（7/15版は表現を締めた書き直し）。

**推奨する整理：**

1. claude.ai の設定 → スキルで **`messy-notes-to-onepager` を削除**する
   （名前は `notes-to-onepager` の方が汎用的で、"messy" は description が既にカバーしている）
2. 残した `notes-to-onepager` の本文を、本ディレクトリの
   `notes-to-onepager/SKILL.md` の内容で**置き換える**

統合版は7/15版の文言を採り、トリガーに「議事録おこして」「音声書き起こし」を追加してある。

> アカウント側のスキルはこのサンドボックスからは変更できない
> （`claude` CLI にスキル管理コマンドは無く、利用できるスキル系ツールは参照・提案のみ。
> 同期ディレクトリはアカウントから毎セッション取得される側であり、ここで消しても反映されない）。
> 本ディレクトリのファイルが以後の正本であり、貼り付け元として使う。
>
> **`meta/実装プロンプト_スキル統合.md` に、統合版の全文を埋め込んだ自己完結の依頼文がある。**
> スキル管理ができる環境へ貼れば、そのまま実行させられる。

### checkin の全スレッド展開（要手動1回）

`checkin/SKILL.md` を claude.ai の Customize でアカウントスキルとしてアップロードすると、
**Cowork・claude.ai チャット・全リポジトリのクラウドセッション**に同期される。
本リポジトリでは SessionStart フック（`.claude/settings.json`）が同じ定例確認を毎回注入するため
二重の保険になる。チャット側で使うには Gmail・Drive のコネクタが有効であること。
