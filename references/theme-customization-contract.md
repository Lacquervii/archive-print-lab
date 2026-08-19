# Theme customization contract — no silent inheritance

## Purpose

A reference-derived family should remain recognizable through relationships, not through a repeated hue, title, object family, scaffold, or material preset. Every new theme must be **re-authored** before a model prompt is written.

```text
same relational engine
+ new theme proposition
+ new material behavior
+ new palette decision
+ new carrier/scaffold
+ new title and type behavior
+ new composition and release
```

If the prompt can be made by changing only the subject noun and one adjective, the customization pass has failed.

## Fixed versus mandatory custom dimensions

| Keep as family relationship | Re-author for every brief |
|---|---|
| hierarchy and first-attention logic | field temperature and substrate undertone |
| meaningful scale contrast | dark-anchor hue and location |
| soft/material versus crisp/printed tension | accent family and optional secondary hue |
| controlled overlap, crop and front/back contact | material tints and title/graphic ink |
| local density plus usable release | complete subject gestalt and related forms |
| tactile finish with a physical host | meso carrier/scaffold and its geometry |
| asymmetry and resolved visual causality | title wording, type character and title fit |
| selected chassis when the carrier needs it | footprint, density distribution and release behavior |

The fixed family does **not** include a universal pale-cool-gray hue, purple, red, square frames, stars, labels, a title word, a material, or a particular subject count. A high-key or materially controlled field may remain a relationship, but its temperature, undertone and color atmosphere are selected per theme.

## Required adaptation record

Before generation, record all of the following. `kept` describes the family relationships retained; `changed` must name concrete decisions for the current theme; `inherited_exclusions` lists source/recent-case features deliberately rejected.

```text
adaptation_delta:
  kept:
    - relational engine decisions that remain
  changed:
    - subject family and whole-form behavior
    - palette and substrate
    - material treatment
    - meso carrier / graphic vocabulary
    - title and type behavior
    - composition / footprint / density / release
  inherited_exclusions:
    - prior case hues, title, geometry, marks, materials or nouns not independently justified
```

A generation is blocked when palette, material, carrier, title decision, or composition decision is merely inherited and not explicitly marked as either independently justified or changed.

## Palette compiler — mandatory, not an adjective

`palette_roles` is a resolved design decision, not a generic phrase such as “restrained accent.” Compile it from the current subject and brief in this order:

1. **Find color evidence.** Identify physical material, use context, cultural meaning, light behavior, historical association or requested mood that belongs to this theme. Do not begin with the previous poster’s hue.
2. **Choose the substrate.** Select the field’s temperature and undertone: for example warm paper-white, mineral blue-gray, chalky bone, smoked silver, desaturated sand, or another justified ground. Keep it high-key/materially controlled only when that serves the family and brief.
3. **Choose localized volume.** Select the dark anchor from the subject/material—graphite, ink black, iron oxide, deep umber, blue-black, pine charcoal, etc.—and state where it appears. “Dark gray” alone is not a palette decision.
4. **Choose one primary accent family.** Derive it from the subject’s physical or semantic evidence: oxidized copper, safety orange, faded cobalt, mineral green, clay red, tobacco ochre, algae teal, and so on. Purple is valid only when this theme independently supports it.
5. **Add a secondary hue only with a job.** It may indicate a material state, optical trace, cultural counterpoint or carrier distinction. Otherwise leave it null; do not decorate with a second random color.
6. **Assign roles.** State the actual colors for field, volume, material surfaces, primary accent, secondary accent, title ink, graphic ink and release. State where each color is allowed to appear.
7. **Close the palette.** Explicitly forbid unrelated hues and every inherited hue that could leak from the reference or most recent case. The model prompt must name the fresh palette positively and include a short targeted prohibition.
8. **Run the freshness check.** Compare the hue families and role assignments against recent generated themes and optional case packs. If the same accent family, title ink and graphic ink recur without an explicit brief reason, reject and recompile. Similarity in grayscale structure is not a palette pass.

### Palette record minimum

```text
palette_id: a short authored name, not “default”
derivation: why these colors belong to this theme
field: substrate color + temperature/undertone
volume: localized dark anchor + locations
material: subject surface colors/tints
accent: primary accent family + job
secondary: optional secondary hue + job, or null
title_ink: resolved title color
graphic_ink: resolved plane/mark color
release: low-weight release color behavior
contrast_strategy: where pressure is concentrated
coverage_strategy: where each hue is allowed and where it is absent
forbidden_inherited_hues: prior/source hue families to block
freshness_check: comparison against recent cases and result
```

A palette is not fresh merely because it has two synonyms for the same hue. `smoky plum + faded lilac`, for example, is still one purple decision.

## Prompt-rendering gate

The model-facing prompt must contain:

- the resolved field and undertone;
- the resolved dark anchor;
- the actual primary accent and any secondary hue;
- the material/title/graphic role of each non-neutral color;
- a short explicit block against inherited or unrelated hues.

Do not send “use a restrained palette” without actual colors. Do not let a chassis member silently inherit the previous title ink. Do not hide the color decision in an internal JSON record while the prompt falls back to a family adjective.

## Cross-theme audit examples

These are demonstrations of the method, not defaults:

- A mouse may justify warm bone polymer, carbon graphite, oxidized safety-orange movement marks and a faded petrol trace; it does not inherit chanhua plum merely because both use an editorial chassis.
- A book may justify paper-cream, ink umber, tobacco ochre and a desaturated vermilion bookmark trace; it does not automatically become gray-purple.
- A botanical craft theme may justify a violet family because silk dye and the brief call for it; that explicit derivation does not make violet portable to computers, books or trees.

## Palette audit — mandatory before beauty review

For every generation, compare the resolved palette record to the actual pixels at thumbnail and normal distance:

- Does the field retain the selected temperature/undertone rather than collapsing to generic cool gray?
- Are the dark anchors the chosen material hue and located where the record says pressure belongs?
- Can the primary accent, title ink and graphic ink be distinguished by their assigned jobs?
- Has a forbidden inherited hue appeared in title, frames, shadows, small marks or material tint?
- Does this palette differ in **hue family and role allocation**, not merely saturation, from unrelated recent themes?

If any answer fails, classify it as a **palette compiler / renderer failure**, not a cosmetic “color tweak.” Recompile the palette and rerender the complete scene; do not only append a new hue adjective.

## Hard review failures

Fail or revise when:

- two unrelated themes use the same accent family without a stated independent reason;
- the palette record contains only “pale gray + restrained accent”;
- title, planes and marks retain the prior case’s color by inertia;
- the new hue exists only in a late adjective and not in the material/carrier roles;
- a fresh accent is present but the rest of the theme remains an uncustomized template;
- the prompt positively names one palette but leaves enough ambiguity for the model to restore the inherited hue.

The repair is to recompile the palette and the other changed dimensions together—not to append more color adjectives to a stale prompt.
