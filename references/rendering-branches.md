# Rendering-style branches — select atmosphere before production

## Purpose

The Diffused Editorial Series has two independent design axes:

```text
series structure / page mechanics
= macro title → compact central event → contacting meso field → authored release

rendering-style branch
= how the material field, diffusion, print treatment and surface atmosphere feel
```

The first axis stays stable for a canonical-series cover unless the user explicitly changes the visual mode. The second axis is **not** silently inherited from 9010, a prior case, a recent generation or the subject noun.

This separation fixes a real failure mode: a poster can preserve the 9010-style structural hierarchy while becoming either a cool contemporary diffused cover or a warm analog-print cover. Neither is automatically more correct; the user selects the atmosphere before production.

`rendering_style_branch` does **not** choose the visual mode, recipe, chassis intensity, aspect ratio, subject grammar, or palette. It constrains the material/print/atmosphere treatment. The theme compiler still derives the actual hues from the current subject.

## Finish selection inside the fixed family

Keep the canonical page grammar stable and choose the surface internally from two levels of evidence:

1. **theme evidence:** material, light behavior, time/use, cultural register and emotional temperature;
2. **fit evidence:** whether the proposed field temperature, title ink, subject colors and carrier planes form a coherent whole with enough contrast and release.

Resolve one finish before writing the prompt. Do not ask the user to select a branch for an ordinary subject request. Record the internal choice and rationale in the manifest. A direct user instruction overrides it. If the evidence conflicts, ask one compact clarification.

The finish changes only atmosphere, material lens and print behavior:

- `contemporary_frosted`: pale mineral field, selective matte diffusion, crisp translucent planes;
- `warm_analog_print`: bone/sand paper, restrained halftone, tactile offset behavior;
- `crisp_modern_graphic`: bright controlled field, cleaner planes, defined ink and limited haze;
- `material_archive`: material-hosted texture and documentation attention without automatically changing the cover grammar;
- `custom`: resolve the user's phrase without altering the family roles.

Never let a finish branch delete the giant title, compressed subject, contacting field, soft/hard tension or release.

## Branch catalog

### A. `contemporary_frosted` — 当代冷灰弥散（9010 推荐）

**Use for:** contemporary experimental editorial covers, especially when the user wants the closest atmospheric kinship with the uploaded 9010 reference.

- high-key cool mineral, soft silver-gray, chalk-white or theme-derived pale field;
- soft frosted/diffused material image with preserved graphite volume;
- sheer translucent planes, clean dark ink, refined registration behavior;
- controlled photographic/matte grain, not nostalgic damage;
- crisp typography and 2D overlay remain precise, contemporary and spatial.

**Do not drift into:** warm antique paper, sepia, distressed poster, heavy halftone, risograph nostalgia, propaganda graphics, aged-library styling, cyberpunk UI.

### B. `warm_analog_print` — 暖调复古印刷

**Use for:** a deliberately warm, tactile, print-led branch. This is legitimate, not a failure, when selected.

- warm bone, sand, tobacco, cream or subject-derived paper field;
- restrained offset/risograph character, light halftone, slight ink spread or registration drift;
- tactile ink/material relationship and lower-saturation printed color;
- historical warmth without pretending the page is an antique artifact.

**Do not drift into:** brown sepia wash, crumpled fake antique paper, propaganda poster, heavy distress, generic retro travel poster, obsolete typography stereotype, global yellowing.

### C. `crisp_modern_graphic` — 清晰现代图形

**Use for:** a sharper, more minimal contemporary branch while retaining the dense canonical page mechanics.

- bright neutral or theme-derived controlled field;
- defined cutouts, clean translucent planes, exact-looking flat contrast;
- limited material haze; overlay and typography are crisp and contemporary;
- surface remains polished and editorial rather than sterile product UI.

**Do not drift into:** generic startup branding, glossy product render, vector-only icon set, fake dashboard, neon technical interface, loss of material depth.

### D. `material_archive` — 材质档案

**Use for:** themes whose physical evidence is part of the point—silk, paper, bark, ceramic, metal, fabric, fibre, weathering—without automatically becoming retro.

- material texture has a specific host, scale and localized light behavior;
- documentation-like attention to seams, fibres, grain, wear, pressure or construction;
- controlled print/chassis layer remains contemporary and subordinate to material proof;
- substrate temperature follows the material rather than a generic old-paper preset.

**Do not drift into:** museum-label clutter, isolated specimens, process teardown, sepia archive, generic craft fair mood, texture with no spatial host.

### `custom`

Use the user's own stated atmosphere. Record the phrase verbatim enough to preserve meaning, then resolve which qualities affect field temperature, diffusion, ink/print behavior, texture source and exclusion list. A custom branch still cannot silently erase the canonical page skeleton.

## Prompt-rendering rule

After the theme and composition are resolved, append one compact, branch-specific surface clause to the model-facing scene:

```text
composition and contacts
→ selected branch’s field / diffusion / print behavior
→ current theme palette and material proof
→ short branch-specific refusal block
```

Do not paste every branch into the prompt. Do not let a surface branch reintroduce a prior theme's palette, title style, symbols, frames or content. Do not call `warm analog print` merely because the current subject is a tree, flower, book, craft or heritage object.

## Review rule

Review branch fit separately from series fit:

1. Does the produced surface match the selected branch?
2. Did an unselected branch leak in—for example, warm retro print when `contemporary_frosted` was selected?
3. Did branch treatment preserve the macro → meso → subject → release hierarchy, central pressure, soft/hard separation and theme-specific palette?
4. Did style selection become a pretext for an inherited hue, copied source furniture or generic genre drift?

A branch match cannot compensate for a failed canonical-series structure. A structurally valid poster with an unselected surface treatment is a `rendering_style_branch` failure and should be rerendered or corrected before being called a pass.
