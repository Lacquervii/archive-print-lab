---
name: archive-print-lab
description: Compile stable Archive Print Lab / 旧档博物志 editorial image prompts for any image model or generator. Use for new objects, plants, artifacts, materials, themes, prompt writing, and result review: oversized high-contrast serif title, compact complete central subject, contacting printed field, sparse editorial marks, and authored release. Resolve the surface internally from the current theme; do not expose a style menu for ordinary requests. Backend-agnostic: no image model, API, or generation service is required for the Skill to work.
version: 5.1.0
---
# Archive Print Lab / 旧档博物志

## Product contract

This is one fixed editorial-image family, not a menu of unrelated poster styles.

```text
9010-derived editorial cover
= oversized high-contrast serif title
+ complete, compact central subject event
+ visible unequal translucent / printed field in contact with it
+ sparse meaningful marks
+ quiet authored lower-right release
+ soft material volume against crisp printed structure
```

For ordinary requests, keep this page grammar stable. Re-author the subject, title, carriers, palette, material evidence, structural field, and release for the current theme. Never copy a prior theme’s noun, palette, accent, title, symbol, geometry, or composition by inertia.

## Backend-agnostic contract

- This Skill produces **image-generation prompts and visual direction**; it does not require any specific image model, API key, or generation service.
- The default deliverable is one well-compiled prompt. Whether and how the user renders it is their choice.
- When the user names a generator (Image2 / gpt-image-2, Midjourney, Flux, SDXL, DALL·E, Gemini, Stable Diffusion WebUI, ComfyUI, 即梦, 通义万相, 豆包, or any other), adapt only the prompt format and parameter hints; the visual family logic stays unchanged.
- A user with no generator at all can still use this Skill: prompt compilation, theme planning, composition direction, and result review all work without rendering.
- Never hard-code one provider’s size list, command syntax, or capabilities into the family rules. Provider details belong to the optional delivery/execution layer.

## Default routing

```yaml
series: 9010-derived-editorial-family
mode: concentrated_cover
recipe: concentrated_editorial_cover
chassis: structural
ratio: 16:9
ratio_source: default_16_9
delivery: prompt
surface_selection_source: internal_theme_fit
canonical_generated_imprint: archive-print-lab
```

A subject noun alone does not change the route. Use an explicit mode override only when the user asks for a hero image, material study, process plate, archive/specimen plate, narrative scene, information system, or quiet art-book plate.

## Surface selection

The page grammar stays fixed while surface atmosphere is resolved internally from the current theme and the whole composition:

- `contemporary_frosted` — high-key mineral field, selective matte diffusion, clean translucent planes;
- `warm_analog_print` — intentionally warm paper, restrained offset / halftone behavior;
- `crisp_modern_graphic` — bright controlled field, sharper planes, limited haze;
- `material_archive` — material evidence leads while the cover grammar stays intact;
- `custom` — an atmosphere explicitly requested by the user.

Do not ask the user to choose A/B/C/D for an ordinary request. Resolve one finish internally and record the rationale. A direct user style instruction overrides the internal choice. Ask only if the latest brief is genuinely contradictory.

## Fixed family roles

### Series imprint

Every canonical generated cover carries a tiny lowercase **`archive-print-lab`** editorial imprint in the authored release. It is a decorative publication credit/colophon: widely tracked, low contrast, aligned to a rule, contour or edition line, and never a watermark, logo, badge or second title. Exact spelling is generator-dependent; do not promise pixel-perfect lettering.

### 1. Macro title plane

- Use a short title or word pair as the first attention event in the canonical route.
- Its visual authority occupies roughly **one-third to one-half** of the page, targeting about **two-fifths**.
- Keep a clean **3–5% top breathing gap**.
- Keep the title fully inside the canvas with narrow side margins; do not force a full-bleed crop.
- Let the compact central subject interrupt the title’s lower edge. If the title reads only as a header, enlarge it.
- Short displayed text is safer across models: most generators render lettering approximately. Treat exact typography as out of scope for image-native output.

### 2. Compact central event

Build one complete, readable subject or subject family with a bounded outer envelope:

- one dominant whole gestalt;
- unequal related forms, echoes, states, shadows, or material traces;
- front / middle / rear depth;
- one or more localized dark anchors;
- rich internal detail without consuming title, margins, or release.

An artifact remains a complete artifact before any parts appear. An organic subject remains a coherent organism, not loose specimens or petal confetti.

### 3. Contacting meso field

Create a medium-scale field that can be seen without zooming in:

- one primary carrier, one unequal support, and one return or continuation;
- theme-native, carrier-native, profile-native, or a deliberate combination;
- at least three visible contacts: interrupted by, passes behind, cut and reappears, aligns with, crosses, or continues into release;
- no generic HUD furniture, fake data, copied purple rectangles, or random frames.

### 4. Soft / hard separation

Keep the material layer and crisp printed layer distinct, then make them touch. Petal volume, glass, paper, bark, fabric, or metal should not collapse into the same treatment as type, planes, lines, blocks, and registration marks.

### 5. Closed theme palette

Every theme must independently resolve:

- field/substrate and undertone;
- localized dark volume hue and where it appears;
- material colors;
- one primary accent and an optional secondary only when it has a job;
- title ink, graphic ink, and release behavior;
- inherited hue families explicitly forbidden for this theme.

Purple, plum, magenta, gray-purple, red, blue, warm paper, or any other recent choice is never portable without a fresh reason.

### 6. Authored release

Reserve a connected lower or lateral quiet region before the subject grows. It carries only a low-weight continuation: a fading plane, shadow, contour, paper residue, or tiny label. It is neither a dead blank band nor a second subject.

## Theme compiler

Before writing a prompt, resolve internally:

```text
theme proposition
→ complete primary gestalt
→ unequal related forms / echoes
→ one or two readable meso events
→ material proof with a real host
→ carrier and chassis provenance
→ fresh palette record
→ targeted refusal list
```

Use `references/theme-grammar.md`, `references/theme-compiler.md`, and `references/theme-customization-contract.md` when needed. A current theme is incomplete if it only says “pale gray with a restrained accent.”

## Composition and prompt sequence

1. Read `references/family-standard.md` and `references/decision-router.md`.
2. Resolve the canonical route or an explicit user-requested mode override.
3. Compile the theme and fresh palette; do not consult historical outputs for a fresh request.
4. Plan macro title, central envelope, meso contacts, protected corridors, layer order, and release with `references/composition-planner.md`, `references/graphic-chassis.md`, and (for canonical covers) `references/structural-scale-ladder.md`.
5. Resolve the surface internally with `references/rendering-branches.md`.
6. Use `references/aspect-ratio-contract.md` for the selected ratio; adapt the concrete size to the generator the user names.
7. For a named Image2 / gpt-image-2 backend, additionally load `references/image2-editorial-adapter.md` and `references/editorial-imprint.md` before rendering; this restores Image2-specific structural pressure without making the family backend-dependent.
8. Render one natural visual scene through `references/prompt-renderer.md`. For canonical covers, include the small lowercase `archive-print-lab` imprint in the authored release.

For the canonical cover, load `references/poster-mechanics.md` as well. Keep audit vocabulary, percentages, menus, and giant negative lists out of the model-facing prompt.

## Prompt rules

Write one coherent visible scene in this order:

```text
canvas and intended reading
→ macro title behavior
→ complete compact central gestalt
→ meso contacts and front/back order
→ quiet release
→ selected surface clause
→ material, lighting, resolved palette
→ 4–10 concrete failure priors to avoid
```

Prefer visible verbs: `spans`, `enters`, `overlaps`, `passes behind`, `is cut by`, `reappears`, `aligns with`, `recedes`, `fades`, `releases into`.

Never paste internal audit labels or every available rule into the prompt.

## Reference boundary

- A reference teaches transferable hierarchy, pressure, layer tension, material continuity, and reading behavior.
- It does not donate its subject nouns, exact title, palette, logo, symbols, or literal geometry.
- Use an image as an input only when the user explicitly asks to edit, transform, or recreate that source. Otherwise create a new text-to-image prompt.
- For a fresh ordinary request, do not inspect historical case files or past generations.

## Quality gates

Revise when any relevant condition fails:

- title is a caption rather than a first-attention plane;
- central subject is a generic still life, bouquet, lineup, detached specimen, or full-canvas wallpaper;
- meso field is missing, microscopic, pasted on, or generic technical costume;
- subject, field, and title do not visibly contact;
- palette is inherited rather than freshly authored;
- release is accidental dead space or perimeter clutter;
- unselected retro, sepia, neon, or other surface behavior leaks into the result;
- the prompt is provider-specific when the user did not name a provider;
- image-native text limitations are hidden rather than stated.

## Response behavior

### Prompt request (default)

Return the resolved canonical route or explicit override, fresh theme/palette rationale, and one ready-to-use prompt in the user’s language. Do not offer an unnecessary surface menu.

### Generation request

If the user asks to render and names a generator, adapt the prompt to that generator’s conventions, render when the execution layer is available, and return:

- inline image (when rendering succeeded);
- generator, requested size, actual returned size, and ratio status;
- image link and prompt link;
- concise honest review: what matches, the largest limitation, and the next change only if needed.

If no generator is available in the current environment, say so plainly and still deliver a prompt plus the exact parameters the user would need elsewhere.

### Iteration request

Identify only the top one or two failures, change the corresponding composition or prompt blocks, and regenerate the prompt. Do not patch a routing failure by piling on adjectives.

### Skill optimization request

Edit this package, validate it, and report the changed rules. Do not generate an image unless separately asked.

## Package map

- `references/decision-router.md` — visual job and canonical routing
- `references/family-standard.md` — non-negotiable series page roles
- `references/theme-grammar.md` / `theme-compiler.md` / `theme-customization-contract.md` — theme and palette compilation
- `references/graphic-chassis.md` / `composition-planner.md` / `poster-mechanics.md` — contact field and cover mechanics
- `references/structural-scale-ladder.md` — reusable macro/meso/subject/micro pressure ladder for canonical covers
- `references/editorial-imprint.md` — small series colophon and release placement
- `references/image2-editorial-adapter.md` — optional Image2 pressure restoration and backend translation
- `references/rendering-branches.md` — internal surface selection
- `references/aspect-ratio-contract.md` / `prompt-renderer.md` / `backend-adapters.md` — ratio, prompt and optional execution adaptation
- `references/quality-rubric.md` / `reference-analysis.md` — review and reference boundary
- `workflows/` — optional operational checklists
- `schemas/` — optional structured records
- `scripts/validate_skill.py` — package validation
