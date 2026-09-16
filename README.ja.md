# Codex 用 Nessie デスクトップペット

[中文](README.md) · [日本語](README.ja.md) · [English](README.en.md)

*Apex Legends* の Nessie を着想元にした、Codex v2 対応のアニメーション付きデスクトップペットです。淡いオリーブグリーン、クリーム色の腹部、濃いオリーブの輪郭線、つやのある黒い瞳を持つステッカー風の首長竜として制作しています。

![アニメーションと視線方向の一覧](assets/qa/contact-sheet-extended.png)

![右向き移動](assets/previews/running-right.gif)
![左向き移動](assets/previews/running-left.gif)

## 同梱内容

| パス | 内容 |
| --- | --- |
| `assets/Nessie-v2-pet.zip` | すぐにインストールできる Codex v2 パッケージ。 |
| `assets/spritesheet.webp` | 1536×2288、透明背景のロスレススプライト atlas。 |
| `assets/pet.json` | `spriteVersionNumber: 2` を指定したペット設定。 |
| `assets/previews/` | idle と左右移動の GIF プレビュー。 |
| `assets/qa/` | コンタクトシートと検証レポート。 |
| `source/` | 閲覧可能なプロンプト、書き出しスクリプト、再現用メモ。 |
| `Nessie-source-artifacts.zip.part-*` | 完全な画像ソースアーカイブの分割ファイル。連結して ZIP にします。 |

## Codex へのインストール

1. `assets/Nessie-v2-pet.zip` をダウンロードして展開します。
2. `pet.json` と `spritesheet.webp` を `~/.codex/pets/nessie/` にコピーします。
3. Codex を再起動し、ペット設定から **Nessie** を選択します。

atlas は 8 列 × 11 行、1 セルは 192×208 ピクセルです。0〜8 行目が標準アニメーション、9〜10 行目が時計回りの 16 視線方向です。

## アニメーションと品質確認

idle、running-right、running-left、waving、jumping、failed、waiting、running、review を収録しています。最終版では移動行の濃すぎる頭部陰影、左向きの尾の境界切れ、不自然なひれ、GIF の青いクロマキー縁を修正しました。

v2 atlas の寸法と透明度は検証済みです。9 本すべての GIF をデコードして確認し、可視の青色キー画素と alpha マスク不一致はいずれも 0 です。左向き移動は、完全に登録された右向きセルをフレームごとに反転しているため、動きのリズムと自然な尾の輪郭を保っています。

根拠は `assets/qa/`、`assets/creation-notes.md`、`assets/repair-notes.md` にあります。

## ソースと再現性

`source/` にはプロンプト、書き出しスクリプト、再現用メモを保存しています。完全な画像ソース（キャラクター参照、生成ストリップ、抽出フレーム、最終 PNG/WebP atlas、QA 証跡）は `Nessie-source-artifacts.zip.part-*` にあります。全分割ファイルをダウンロードし、macOS/Linux で `cat Nessie-source-artifacts.zip.part-* > Nessie-source-artifacts.zip` を実行してから展開してください。

配布時は、同梱のキャラクター参照・プロンプト・最終アートワークの出典表記を維持してください。
