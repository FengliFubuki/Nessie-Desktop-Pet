# Nessie Desktop Pet for Codex

[中文](README.md) · [日本語](README.ja.md) · [English](README.en.md)

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
