# Archive Print Lab / 旧档博物志

[![中文](https://img.shields.io/badge/中文-CN-blue)](README.md)
[![English](https://img.shields.io/badge/English-EN-lightgreen)](README.en.md)

> **AI image-generation skill (生图 Skill)** — compile any subject into a generator-ready editorial poster prompt.
> **AI 生图 Skill** — 把任意主题编译成可直接出图的编辑海报提示词。

## What style is this?

One sentence: **vintage museum-archive editorial posters** — old botanical plates and museum archive cards, crossed with modern magazine layout.

Every image keeps the same skeleton:

```text
a giant serif title dominating the upper third to half of the frame
+ the subject complete and compact at the center (flower, tree, object...)
+ printed-paper texture, a hint of old archive
+ sparse labels, ticks and cross-marks, like an index in a field guide
+ a quiet lower-right release with a small publication imprint
```

Think of a carefully crafted archive card: big title, centered specimen, print details, quiet sign-off. New themes only swap the specimen and the color mood — the skeleton stays.

## Input & output

Give it a subject (sunflower, oil lamp, gypsophila, red rose...), get back a ready-to-use prompt for your image generator:

```text
/archive-print-lab generate a sunflower with Image2
/archive-print-lab write a poster prompt for an oil lamp
/archive-print-lab create a frosted editorial cover about gypsophila
```

Works with Image2 / gpt-image-2, Midjourney, Flux, SDXL, Stable Diffusion, ComfyUI, Gemini, and consumer image tools.

## What it does

- **Image-generation prompt compiler**: turns objects, plants, artifacts, materials, and editorial themes into ready-to-use image prompts.
- **Generator-agnostic**: works without a specific model; the default deliverable is a ready-to-use prompt.
- Adapts prompt syntax only when a generator is named, keeping strong title, central-event, and contacting-field pressure.
- Exact lettering in image-native generation is approximate by nature; prompts keep displayed text short and report that limitation honestly.

## Gallery — example generated outputs

| Image | Subject | Description |
|-------|---------|-------------|
| ![Sunflower](examples/sunflower.png) | Sunflower 向日葵 | Warm analog print — golden petals, dark seed head, summer solstice light. |
| ![Baby's Breath](examples/babys-breath.png) | Gypsophila 满天星 | Contemporary frosted — white blooms on airy branches, mineral cool light. |
| ![Lily](examples/lily-pink.png) | Lily 百合 | Soft pastel editorial — pink petals, spotted throat, gentle gradient. |
| ![Lily](examples/lily-stargazer.png) | Lily 百合 | Dreamy diffused — warm pink, luminous atmosphere. |
| ![Oil Lamp](examples/oil-lamp.png) | Oil Lamp 油灯 | Warm analog print — brass base, amber oil, glowing wick. |
| ![Tree](examples/tree.png) | Tree 树 | Earthy analog — gnarled trunk, mossy canopy, ring and fork annotations. |
| ![Daisy](examples/daisy.png) | Daisy 雏菊 | Contemporary frosted — white petals, golden center, structure in balance. |
| ![Plum Blossom](examples/plum-blossom.png) | Plum Blossom 梅花 | Delicate editorial — pale pink petals, frost background, fork and bud. |
| ![Rose](examples/rose.png) | Rose 玫瑰 | Material archive — velvet petals, thorned stem, botanical precision. |

## Use

Load `SKILL.md` as the entrypoint. It routes the task, compiles the theme and palette, plans the composition, then produces one generator-ready prompt.

## Validation

```sh
python3 scripts/validate_skill.py
```

## Release

The packaged v5.1.0 archive is in [`releases/`](releases/).

## License

No license has been selected yet. Add one before accepting outside contributions or reuse.