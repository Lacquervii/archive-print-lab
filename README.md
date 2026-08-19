# Archive Print Lab / 旧档博物志

A generator-agnostic prompt-compilation system for a stable 9010-derived editorial cover family.

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

- Compiles image-generation prompts and visual direction for objects, plants, artifacts, materials, and editorial themes.
- Works without a specific image model; the default deliverable is a ready-to-use prompt.
- Adapts prompt syntax only when a generator is named, including Image2 / gpt-image-2, Midjourney, Flux, SDXL, Stable Diffusion, ComfyUI, Gemini, and consumer image tools.
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
