# Archive Print Lab / 旧档博物志

A generator-agnostic prompt-compilation system for a stable 9010-derived editorial cover family.

一个与生成器无关的提示词编译系统，基于稳定的 9010 衍生编辑封面家族。

---

## Core visual contract / 核心视觉契约

```text
oversized high-contrast serif title
+ compact complete central subject event
+ unequal contacting printed field
+ sparse subject-specific index marks
+ quiet authored lower-right release
+ tiny lowercase `archive-print-lab` editorial imprint
```

```text
超大高对比度衬线标题
+ 紧凑完整的中央主体事件
+ 不等距接触印刷场
+ 稀疏的学科专属索引标记
+ 安静的右下角作者释放区
+ 小写 `archive-print-lab` 编辑出版署名
```

The family keeps the page grammar stable while re-authoring the subject, palette, material proof, structural carriers, and release for each new theme.

该家族在保持页面语法稳定的同时，为每个新主题重新编排主体、色板、材质证明、结构载体和释放区。

---

## What it does / 功能

- Compiles image-generation prompts and visual direction for objects, plants, artifacts, materials, and editorial themes.
  编译物体、植物、器物、材质和编辑主题的图像生成提示词与视觉方向。
- Works without a specific image model; the default deliverable is a ready-to-use prompt.
  无需指定具体图像模型即可工作；默认交付物为可直接使用的提示词。
- Adapts prompt syntax only when a generator is named, including Image2 / gpt-image-2, Midjourney, Flux, SDXL, Stable Diffusion, ComfyUI, Gemini, and consumer image tools.
  仅在指定生成器时适配提示词语法，支持 Image2 / gpt-image-2、Midjourney、Flux、SDXL、Stable Diffusion、ComfyUI、Gemini 及消费级图像工具。
- Uses an optional Image2 editorial adapter to retain strong title, central-event, and contacting-field pressure in image-native output.
  使用可选的 Image2 编辑适配器，在原生图像输出中保留强烈的标题、中央事件和接触场压力。

---

## Canonical route / 规范路径

```yaml
series: 9010-derived-editorial-family
mode: concentrated_cover
recipe: concentrated_editorial_cover
chassis: structural
ratio: 16:9
```

For ordinary requests, the family retains:

1. a dominant upper title plane;
   占主导地位的上方标题平面；
2. a broad, compact, dark-anchored central event;
   宽大、紧凑、深色锚定的中央事件；
3. a primary/support/return contacting field;
   主/辅/回返接触场；
4. soft material volume against crisp printed structure;
   柔软材质体量与清晰印刷结构的对比；
5. a connected lower-right release with the small `archive-print-lab` publication imprint.
   连通的右下角释放区，带有小字 `archive-print-lab` 出版署名。

---

## Use / 使用

Load `SKILL.md` as the entrypoint. It routes the task, compiles the theme and palette, plans the composition, then produces one generator-ready prompt.

以 `SKILL.md` 为入口。它路由任务、编译主题与色板、规划构图，然后产出一条生成器就绪的提示词。

```text
/archive-print-lab generate a sunflower with Image2
/archive-print-lab write a poster prompt for an oil lamp
/archive-print-lab create a frosted editorial cover about gypsophila
```

```text
/archive-print-lab 用 Image2 生成一张向日葵
/archive-print-lab 为油灯写一张海报提示词
/archive-print-lab 制作一份关于满天星的磨砂编辑封面
```

Exact lettering in image-native generation is approximate by nature; prompts keep displayed text short and report that limitation honestly.

在原生图像生成中，精确的文字排版本质上是近似的；提示词会保持显示文字简短，并如实报告这一局限。

---

## Gallery / 画廊

Below are example outputs generated with the system. Each follows the 9010-derived editorial family contract.

以下是使用本系统生成的示例输出。每张都遵循 9010 衍生编辑家族契约。

| Image | Subject | Description |
|-------|---------|-------------|
| ![Sunflower](examples/sunflower.png) | 向日葵 Sunflower | Warm analog print — golden petals, dark seed head, summer solstice light. 暖调模拟印刷——金黄花瓣、深色种盘、夏至光线。 |
| ![Baby's Breath](examples/babys-breath.png) | 满天星 Gypsophila | Contemporary frosted — white blooms on airy branches, mineral cool light. 当代冷灰弥散—— airy 枝条上的白色小花，矿物冷光。 |
| ![Lily](examples/lily-pink.png) | 百合 Lily | Soft pastel editorial — pink petals, spotted throat, gentle gradient. 柔和粉彩编辑——粉色花瓣、斑点花喉、温柔渐变。 |
| ![Lily](examples/lily-stargazer.png) | 百合 Lily | Dreamy diffused — stargazer variety, warm pink, luminous atmosphere. 梦幻弥散——百合品种，暖粉，光感氛围。 |
| ![Oil Lamp](examples/oil-lamp.png) | 油灯 Oil Lamp | Warm analog print — brass base, amber oil, glowing wick, fire fuel time. 暖调模拟印刷——黄铜底座、琥珀燃油、燃烧灯芯。 |
| ![Tree](examples/tree.png) | 树 Tree | Earthy analog — gnarled trunk, mossy canopy, ring and fork annotations. 泥土模拟——扭曲树干、苔藓树冠、年轮与分叉标注。 |
| ![Daisy](examples/daisy.png) | 雏菊 Daisy | Contemporary frosted — white petals, golden center, structure in balance. 当代冷灰弥散——白色花瓣、金色花心，结构平衡。 |
| ![Plum Blossom](examples/plum-blossom.png) | 梅花 Plum Blossom | Delicate editorial — pale pink petals, frost background, fork and bud. 精致编辑——淡粉花瓣、霜色背景、分叉与花苞。 |
| ![Rose](examples/rose.png) | 玫瑰 Rose | Material archive — velvet petals, thorned stem, botanical precision. 材质档案——绒面花瓣、带刺茎干、植物学精确。 |

---

## Validation / 校验

```sh
python3 scripts/validate_skill.py
```

---

## Release / 发布

The packaged v5.1.0 archive is in [`releases/`](releases/).

打包的 v5.1.0 归档位于 [`releases/`](releases/)。

---

## License / 许可

No license has been selected yet. Add one before accepting outside contributions or reuse.

尚未选择许可证。在接受外部贡献或复用之前请添加一个。
