# Archive Print Lab / 旧档博物志

[![中文](https://img.shields.io/badge/中文-CN-blue)](README.zh.md)
[![English](https://img.shields.io/badge/English-EN-lightgreen)](README.md)

> **AI image-generation skill (生图 Skill)** — compile any subject into a generator-ready editorial poster prompt.
> **AI 生图 Skill** — 把任意主题编译成可直接出图的编辑海报提示词。

A generator-agnostic prompt-compilation system for a stable **9010-derived editorial cover family**. Feed it a subject (plant, object, artifact, material, theme); it returns a structured prompt that produces the same editorial family across Image2 / gpt-image-2, Midjourney, Flux, SDXL, Stable Diffusion, ComfyUI, Gemini, and consumer image tools.

## Core visual contract

```text
oversized high-contrast serif title
+ compact complete central subject event
+ unequal contacting printed field
+ sparse subject-specific index marks
+ quiet authored lower-right release
+ tiny lowercase `archive-print-lab` editorial imprint
```

The family keeps the page grammar stable while re-authoring the subject, palette, material proof, structural carriers, and release for each new theme.

## What it does

- **Image-generation prompt compiler**: turns objects, plants, artifacts, materials, and editorial themes into ready-to-use image prompts.
- **Generator-agnostic**: works without a specific model; the default deliverable is a ready-to-use prompt.
- Adapts prompt syntax only when a generator is named — Image2 / gpt-image-2, Midjourney, Flux, SDXL, Stable Diffusion, ComfyUI, Gemini, and consumer image tools.
- Uses an optional Image2 editorial adapter to retain strong title, central-event, and contacting-field pressure in image-native output.

## Canonical route

```yaml
series: 9010-derived-editorial-family
mode: concentrated_cover
recipe: concentrated_editorial_cover
chassis: structural
ratio: 16:9
```

For ordinary requests, the family retains:

1. a dominant upper title plane;
2. a broad, compact, dark-anchored central event;
3. a primary/support/return contacting field;
4. soft material volume against crisp printed structure;
5. a connected lower-right release with the small `archive-print-lab` publication imprint.

## Gallery — example generated outputs / 生成效果示例

| Image | Subject | Description |
|-------|---------|-------------|
| ![Sunflower](examples/sunflower.png) | Sunflower 向日葵 | Warm analog print — golden petals, dark seed head, summer solstice light. |
| ![Baby's Breath](examples/babys-breath.png) | Gypsophila 满天星 | Contemporary frosted — white blooms on airy branches, mineral cool light. |
| ![Lily](examples/lily-pink.png) | Lily 百合 | Soft pastel editorial — pink petals, spotted throat, gentle gradient. |
| ![Lily](examples/lily-stargazer.png) | Lily 百合 | Dreamy diffused — stargazer variety, warm pink, luminous atmosphere. |
| ![Oil Lamp](examples/oil-lamp.png) | Oil Lamp 油灯 | Warm analog print — brass base, amber oil, glowing wick. |
| ![Tree](examples/tree.png) | Tree 树 | Earthy analog — gnarled trunk, mossy canopy, ring and fork annotations. |
| ![Daisy](examples/daisy.png) | Daisy 雏菊 | Contemporary frosted — white petals, golden center, structure in balance. |
| ![Plum Blossom](examples/plum-blossom.png) | Plum Blossom 梅花 | Delicate editorial — pale pink petals, frost background, fork and bud. |
| ![Rose](examples/rose.png) | Rose 玫瑰 | Material archive — velvet petals, thorned stem, botanical precision. |

## Use

Load `SKILL.md` as the entrypoint. It routes the task, compiles the theme and palette, plans the composition, then produces one generator-ready prompt.

```text
/archive-print-lab generate a sunflower with Image2
/archive-print-lab write a poster prompt for an oil lamp
/archive-print-lab create a frosted editorial cover about gypsophila
```

Exact lettering in image-native generation is approximate by nature; prompts keep displayed text short and report that limitation honestly.

## Validation

```sh
python3 scripts/validate_skill.py
```

## Release

The packaged v5.1.0 archive is in [`releases/`](releases/).

## License

No license has been selected yet. Add one before accepting outside contributions or reuse.
