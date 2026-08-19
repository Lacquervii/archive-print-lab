# Prompt renderer — compile plans into visible spatial prose

## Goal

The prompt should receive a resolved visual scene, not an internal audit report, a menu of options, or a giant negative list. Build the composition first with `theme-compiler.md` and `composition-planner.md`, then write one continuous model-facing description.

This file is generator-neutral. Adapt to the user’s chosen tool only when they name one:

- **Image2 / gpt-image-2 and other natural-language models:** keep the scene as the prompt; for the canonical cover, load the optional Image2 editorial adapter and attempt the tiny lowercase `archive-print-lab` imprint in the release; keep displayed words short and report approximate lettering honestly.
- **Midjourney / Flux / SDXL / Stable Diffusion WebUI / ComfyUI / 即梦 / 通义 / 豆包 / Gemini-style tools:** add the same scene in their preferred format — comma-separated keywords, aspect-ratio parameters (`--ar 16:9`), quality/style tags, and a compact negative-prompt block — while preserving the visual decisions below.
- **Unknown tool:** deliver the natural-language scene plus a note that the user should adapt framing, aspect ratio and negative prompts to their generator.

## Canonical shell preflight

Before rendering, state the canonical series record, selected ratio, and the internally resolved finish. If the user explicitly names a branch, use it; otherwise derive it from theme evidence and whole-composition fit. Do not expose a branch menu or infer a different page grammar from the finish.

```text
canonical:
  mode: concentrated_cover
  recipe: concentrated editorial cover
  chassis: structural
  aspect_ratio: 16:9
  ratio_source: default_16_9
  requested_size: depends on the generator the user names (default guidance: 16:9)
  override_reason: null
  rendering_style_branch: internally_resolved_from_theme_and_fit
  rendering_style_selection_source: internal_theme_fit
```

or:

```text
override:
  mode: [hero|material|process|archive|narrative|information|quiet]
  reason: [explicit brief reason, or null for a ratio-only override]
  chassis: [none|light|active|structural]
  aspect_ratio: [latest explicit user ratio]
  ratio_source: explicit_user_override
  requested_size: [the named generator’s closest supported target]
```

Do not produce a prompt without this record. The mode/chassis/ratio tuple is a series decision, not a side effect of the generator.

## Prompt sequence

For an editorial cover, use this sequence unless the selected mode clearly needs another:

```text
1. carrier + canvas + intended reading
2. macro plane / title behavior
3. complete primary gestalt and bounded central family
4. one or two meso events with depth/contact
5. selected graphic chassis and its front/back behavior
6. protected release and low-weight continuation
7. selected rendering-style branch surface clause, then material, lighting, palette and finish
8. short branch-specific and strong-prior refusal block
```

Canvas and composition come before subject detail. Rendering-style branch, material, lighting and palette are separate controls. Before writing the surface/palette sentence, load the selected branch from `rendering-branches.md` and the complete palette record from `theme-customization-contract.md`; a phrase such as “restrained accent” is incomplete and must not reach the model. Do not inherit warm paper, halftone, ink bleed, analog-print nostalgia or any other surface cue unless the selected branch licenses it.

## Visible-language rules

Prefer observable descriptions:

```text
spans, enters, overlaps, compresses, passes behind, is cut by,
reappears, aligns with, recedes, fades, releases into
```

Do not send phrases such as `macro ladder`, `profile-native`, `meso requirement`, `density score`, `footprint percentage`, `quality gate`, or `do not overfit`.

Resolve choices before writing. Do not ask for all of these at once: cropped and contained type, light and dense overlays, full subject and fragments, quiet and maximum density. Select one behavior suited to the plan.

## Typography and graphic constraints

- Put displayed words in quotation marks; keep image-native text short.
- For canonical covers, attempt the small lowercase series imprint `archive-print-lab` in the lower-right release as a decorative publication colophon; keep it widely tracked, low contrast and secondary. Do not present it as a watermark or logo.
- Specify text role, type character, approximate position and contact—not just the word.
- Keep displayed text short. Most generators letter approximately; do not claim exact glyph shape, vector geometry or deterministic reading order.
- A `structural` chassis may include oversized typography, a few unequal flat planes, restrained dark blocks and sparse micro marks. Describe their relative depth and purpose in space; never dump a generic inventory of frames, stars, brackets and labels.
- A `none` or `light` chassis should not be padded with graphical leftovers merely because the family can use them.

## Refusal block

Use 4–10 concrete category priors, not a massive prohibition catalogue.

- tree: forest postcard, landscape horizon, giant edge-to-edge crown, root carpet, textbook diagram, HUD
- computer: product lineup, exploded parts, e-commerce render, fake spec sheet, HUD
- book: neat still-life stack, scattered page specimens, exploded binding, library scene

A positive spatial plan is stronger than repeated negatives. For negative-prompt-capable tools, convert the same categories into their negative field; otherwise keep them inside the natural-language scene.

## Template

```text
Create one [ratio] [carrier] about [theme proposition].

[Macro plane and title fit.] [Complete primary gestalt and bounded central relation.] [One or two visible meso events and their depth.] [Resolved chassis members pass behind / through / align with the event.] [Release and corridors.] [Selected rendering-style branch surface clause.] [Material + lighting + palette + finish.]

Avoid [short targeted priors].
```

This is a writing scaffold, not a literal prompt to expose unchanged. Remove headings and audit vocabulary before delivery.

## Preflight

Before send:

- title authority occupies about 1/3–1/2 of the full page visual mass, targeting roughly 2/5;
- a small clean breathing gap of approximately 3%–5% of canvas height remains above the title;
- the title remains complete and contained inside the canvas with narrow side margins; it does not accidentally crop or bleed off the edges;
- the compact subject is reduced enough to cross the lower title edge without taking over the macro plane;
- if the title reads like a header, enlarge it; if it touches the top edge or becomes a full-bleed crop, pull it inward before adding subject detail;
- the canvas is the selected ratio (16:9 by default), and the concrete size parameter follows the generator the user names;
- one recorded rendering-style branch has been selected by the user, explicitly carried over, or delegated with `user_allows_auto`;
- the surface clause and refusal block match that branch rather than a prior poster’s atmosphere;
- one theme proposition governs the image;
- complete gestalt appears before component detail;
- one chosen chassis intensity is visible in the prose;
- contacts and release are spatially described;
- the canonical release includes a small lowercase `archive-print-lab` imprint attempt when the named generator is Image2 or another image renderer;
- the actual field, undertone, localized volume, material tints, primary accent, title ink and graphic ink are stated;
- the prompt includes the short forbidden-hue block from the palette record;
- no title, plane or mark is allowed to inherit the previous case’s color by omission;
- provider-specific syntax appears only when the user named a generator.
