# Nessie Desktop Pet for Codex

[中文](#中文) · [日本語](#日本語) · [English](#english)

## 中文

一个基于 *Apex Legends* Nessie 概念创作的 Codex v2 动态桌面宠物。它使用柔和的贴纸 / 表情包插画风格：浅橄榄绿色长颈海怪、奶油色腹部、深橄榄描边与黑色珠光眼睛。

![Nessie 全部动画与视角](assets/qa/contact-sheet-extended.png)

![向右移动](assets/previews/running-right.gif)
![向左移动](assets/previews/running-left.gif)

## 内容

| 路径 | 说明 |
| --- | --- |
| `assets/Nessie-v2-pet.zip` | 可直接安装的 Codex v2 宠物包。 |
| `assets/spritesheet.webp` | 1536×2288 的无损透明精灵图。 |
| `assets/pet.json` | Codex 宠物清单，声明 `spriteVersionNumber: 2`。 |
| `assets/previews/` | idle 与两个方向的 GIF 动画预览。 |
| `assets/qa/` | 接触表、色键清理和 GIF 导出验证。 |
| `source/` | 可浏览的提示词、导出脚本和复现说明。 |
| `Nessie-source-artifacts.zip.part-*` | 完整图像源工件归档的分卷；拼合后即为 ZIP 文件。 |

## 安装到 Codex

1. 下载并解压 `assets/Nessie-v2-pet.zip`。
2. 将 `pet.json` 和 `spritesheet.webp` 复制到 `~/.codex/pets/nessie/`。
3. 重启 Codex，并在宠物设置中选择 **Nessie**。

精灵表为 8 列 × 11 行，单元格为 192×208。前 9 行是标准动画，最后 2 行包含 16 个顺时针视角；默认空闲帧保持安静微动，移动行在不改变帧序的前提下提供左右两个方向。

## 动画与质量检查

动画包括：idle、running-right、running-left、waving、jumping、failed、waiting、running 与 review。最终版本修复了移动行头部过深的阴影、左向尾巴边界切割、额外鳍肢，以及 GIF 蓝色色键残留。

最终检查确认：

- v2 atlas 尺寸和透明区域通过验证；
- 全部 9 个 GIF 解码后蓝色色键像素为 0；
- GIF alpha 遮罩与 atlas 一致，误差为 0；
- 左向移动动画逐帧镜像完整注册后的右向角色，因此保留了正常尾巴轮廓和动作节奏。

详见 `assets/qa/`、`assets/creation-notes.md` 与 `assets/repair-notes.md`。

## 源码与复现

`source/` 保留了生成提示词、导出脚本和复现说明。完整图像源工件（角色参考、每行生成结果、提取出的单帧、最终 PNG/WebP atlas 及 QA 证据）在 `Nessie-source-artifacts.zip.part-*` 中。下载全部分卷后，在 macOS/Linux 上运行 `cat Nessie-source-artifacts.zip.part-* > Nessie-source-artifacts.zip`，再解压即可离线审阅或复现该工作流。

角色参考、动画提示词和最终作品由本仓库作者提供；请在再发布时保留来源说明。

---

## 日本語

*Apex Legends* の Nessie を着想元にした、Codex v2 対応のアニメーション付きデスクトップペットです。淡いオリーブグリーン、クリーム色の腹部、濃いオリーブの輪郭線、つやのある黒い瞳を持つステッカー風の首長竜として制作しています。

![アニメーションと視線方向の一覧](assets/qa/contact-sheet-extended.png)

![右向き移動](assets/previews/running-right.gif)
![左向き移動](assets/previews/running-left.gif)

### 同梱内容

| パス | 内容 |
| --- | --- |
| `assets/Nessie-v2-pet.zip` | すぐにインストールできる Codex v2 パッケージ。 |
| `assets/spritesheet.webp` | 1536×2288、透明背景のロスレススプライト atlas。 |
| `assets/pet.json` | `spriteVersionNumber: 2` を指定したペット設定。 |
| `assets/previews/` | idle と左右移動の GIF プレビュー。 |
| `assets/qa/` | コンタクトシートと検証レポート。 |
| `source/` | 閲覧可能なプロンプト、書き出しスクリプト、再現用メモ。 |
| `Nessie-source-artifacts.zip.part-*` | 完全な画像ソースアーカイブの分割ファイル。連結して ZIP にします。 |

### Codex へのインストール

1. `assets/Nessie-v2-pet.zip` をダウンロードして展開します。
2. `pet.json` と `spritesheet.webp` を `~/.codex/pets/nessie/` にコピーします。
3. Codex を再起動し、ペット設定から **Nessie** を選択します。

atlas は 8 列 × 11 行、1 セルは 192×208 ピクセルです。0〜8 行目が標準アニメーション、9〜10 行目が時計回りの 16 視線方向です。

### アニメーションと品質確認

idle、running-right、running-left、waving、jumping、failed、waiting、running、review を収録しています。最終版では移動行の濃すぎる頭部陰影、左向きの尾の境界切れ、不自然なひれ、GIF の青いクロマキー縁を修正しました。

v2 atlas の寸法と透明度は検証済みです。9 本すべての GIF をデコードして確認し、可視の青色キー画素と alpha マスク不一致はいずれも 0 です。左向き移動は、完全に登録された右向きセルをフレームごとに反転しているため、動きのリズムと自然な尾の輪郭を保っています。

根拠は `assets/qa/`、`assets/creation-notes.md`、`assets/repair-notes.md` にあります。

### ソースと再現性

`source/` にはプロンプト、書き出しスクリプト、再現用メモを保存しています。完全な画像ソース（キャラクター参照、生成ストリップ、抽出フレーム、最終 PNG/WebP atlas、QA 証跡）は `Nessie-source-artifacts.zip.part-*` にあります。全分割ファイルをダウンロードし、macOS/Linux で `cat Nessie-source-artifacts.zip.part-* > Nessie-source-artifacts.zip` を実行してから展開してください。

配布時は、同梱のキャラクター参照・プロンプト・最終アートワークの出典表記を維持してください。

---

## English

A Codex v2 animated desktop pet inspired by the *Apex Legends* Nessie concept. It is a light olive-green, sticker-style plesiosaur with a cream belly, dark olive outlines, and glossy black bead eyes.

![Complete animation and direction sheet](assets/qa/contact-sheet-extended.png)

![Running right](assets/previews/running-right.gif)
![Running left](assets/previews/running-left.gif)

### Included files

| Path | Purpose |
| --- | --- |
| `assets/Nessie-v2-pet.zip` | Ready-to-install Codex v2 package. |
| `assets/spritesheet.webp` | Lossless transparent 1536×2288 sprite atlas. |
| `assets/pet.json` | Pet manifest with `spriteVersionNumber: 2`. |
| `assets/previews/` | Idle and directional GIF previews. |
| `assets/qa/` | Contact sheet and validation reports. |
| `source/` | Browsable prompts, export script, and reproduction notes. |
| `Nessie-source-artifacts.zip.part-*` | Split parts of the complete image-source archive; concatenate them into a ZIP. |

### Install in Codex

1. Download and extract `assets/Nessie-v2-pet.zip`.
2. Copy `pet.json` and `spritesheet.webp` to `~/.codex/pets/nessie/`.
3. Restart Codex and choose **Nessie** in Pet Settings.

The atlas contains 8 columns × 11 rows at 192×208 pixels per cell. Rows 0–8 hold the standard animation states; rows 9–10 provide 16 clockwise look directions.

### Animation and QA

The pet includes idle, running-right, running-left, waving, jumping, failed, waiting, running, and review states. The final build repairs dark head shading in the movement rows, a left-facing tail boundary cut, malformed flippers, and blue chroma-key fringes in GIF exports.

Final checks confirm valid v2 geometry and transparency; zero visible blue-key pixels and zero alpha-mask mismatches after decoding all nine GIFs. Left-running frames are mirrors of complete registered right-running cells, which preserves the cadence and a clean tail silhouette.

See `assets/qa/`, `assets/creation-notes.md`, and `assets/repair-notes.md` for the evidence.

### Source and reproducibility

`source/` keeps the prompts, export script, and reproduction notes. The complete image-source set—character references, generated strips, extracted frames, final PNG/WebP atlases, and QA evidence—is stored in `Nessie-source-artifacts.zip.part-*`. Download every part, run `cat Nessie-source-artifacts.zip.part-* > Nessie-source-artifacts.zip` on macOS/Linux, then extract the ZIP for offline review or reproduction.

Please retain the attribution notes when redistributing the supplied character references, prompts, or final artwork.
