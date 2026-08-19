# Theme compiler — convert a noun into an authored content system

## Purpose

Do not insert a subject noun into a style paragraph. Compile the brief into a theme-specific visual system before composition or prompt writing:

```text
brief -> proposition -> whole gestalt -> relational supports -> meso events
      -> material proof -> carrier/chassis translation -> palette/refusal plan
```

The compiler protects both sides of the task:

- a new subject does not become a reskinned 9010 flower poster;
- removal of source-specific furniture does not leave a polite isolated object.

## Required compilation decisions

Before the seven content decisions below, load `theme-customization-contract.md` and resolve a **fresh adaptation delta and palette record**. The compiler is incomplete until the current theme has independently chosen its substrate, dark-anchor hue, material tints, accent family, title/graphic inks, coverage, contrast strategy and inherited-hue exclusions. Do not use a prior case palette as a placeholder.

### Customization gate

Record:

```text
adaptation_delta:
  kept:
  changed:
  inherited_exclusions:
palette_record:
  palette_id:
  derivation:
  field:
  volume:
  material:
  accent:
  secondary:
  title_ink:
  graphic_ink:
  release:
  contrast_strategy:
  coverage_strategy:
  forbidden_inherited_hues:
  freshness_check:
```

Reject a compiled theme if `derivation`, `forbidden_inherited_hues`, `freshness_check`, or any role-specific color is missing. A phrase such as `restrained accent` is not a palette record.

### 1. Theme proposition

Write what the viewer should remember, not a parts inventory.

- weak: `a tree with bark, roots and leaves`
- useful: `a mature organism holding weather, growth and time inside one compressed living form`

### 2. Primary gestalt

Name the complete form/event that must survive thumbnail scale. For artifacts this is usually one intact object or coherent object family, never an involuntary exploded view.

### 3. Related forms or echoes

Choose only supports that add a meaningful relation: unequal companions, contained whole-form echoes, states, shadows, reflections, pressure returns, material traces or environmental residues. Give each one a front/middle/rear role.

### 4. Meso events

Define one or two unequal medium-scale events visible at normal distance. Micro texture cannot substitute for these.

Examples:

| Theme | Useful meso events |
|---|---|
| Tree | fork/canopy cavity; root buttress/contact-shadow crescent |
| Book | cover/page-block overlap; folded-paper shadow return |
| Computer | whole-device silhouette against screen glow/reflection plane; lid/body shadow transition |
| Craft | material tension between layered forms; wrapped contour crossing a dark cavity |
| Architecture | threshold/cavity exchange; plane-shadow intersection |
| Fabric | fold crest against compressed shadow valley; translucent layer overlap |

### 5. Material proof

Select close-view evidence with a host: thread direction in craft, bark fissures in tree, absorbed ink in paper, reflection in glass, wear in metal, weave in cloth. Do not use generic "premium texture."

### 6. Carrier provenance and chassis translation

Record separately:

- **theme-native field** — subject contours, paths, shadows, planes or boundaries;
- **carrier-native field** — title, archive, exhibition, catalog or comparison logic;
- **profile-native chassis** — selected from `graphic-chassis.md` when the visual family needs it.

Resolve how they touch. A profile chassis can be active even if a literal frame is not naturally produced by the subject; it must still be translated through the subject's direction, palette, scale and contact behavior.

### 7. Palette roles and freshness

Assign actual, theme-derived roles—not merely colors or generic adjectives. Follow the mandatory palette compiler in `theme-customization-contract.md`:

```text
field: material ground + temperature/undertone
volume: localized dark anchor + locations
material: subject surface colors/tints
accent: primary ink / dyed material / state / attention + job
secondary: optional hue + job, or null
title_ink: resolved title color
graphic_ink: resolved plane/mark color
release: low-weight fade or paper residue
forbidden_inherited_hues: prior/source families to block
freshness_check: comparison against recent themes/cases
```

A new theme must explicitly explain why the palette belongs to it and where each non-neutral hue is allowed. `smoky plum + faded lilac` is one purple decision, not two independent customizations. Do not let the renderer fall back to the last theme’s title or plane color.

### 8. Refusal list

Block only strong theme/model priors: product-lineup, forest postcard, generic bouquet, HUD, exploded view, etc. Never turn a model-facing prompt into a giant defensive catalogue.

## Category safeguards

- **Organic/living:** preserve one organism or one relational family; use growth, anatomy, stages and traces; do not become stock nature scene or detached specimens.
- **Artifact/object:** whole gestalt first; related forms default to shadow, reflection, use trace or contained echo; separate parts only for a real process/archive task.
- **Craft:** material construction may make a true family, but details serve an assembled central gestalt, not an instructional teardown by default.
- **Architecture:** derive field from cavity, threshold, plane, circulation and shadow; do not decorate with unrelated boxes.
- **Human/body:** preserve identity and anatomy; use gesture/fabric/shadow relationships instead of scattering body fragments.
- **Material:** give grain/fold/fracture/translucency a spatial host and a medium-scale event.
- **Narrative/information:** compile story or semantic logic first; do not force a relational-cover chassis over a task that needs a readable scene or diagram.

## Compiled-theme record

```text
theme_proposition:
subject_behavior:
primary_gestalt:
related_forms_or_echoes:
meso_events:
material_proof:
carrier_provenance:
profile_translation:
adaptation_delta:
palette_record:
  palette_id:
  derivation:
  field:
  volume:
  material:
  accent:
  secondary:
  title_ink:
  graphic_ink:
  release:
  contrast_strategy:
  coverage_strategy:
  forbidden_inherited_hues:
  freshness_check:
palette_roles:
title_candidate:
release_behavior:
refusal_list:
```

Only after this record is stable should the composition planner decide size, title fit, corridors and overlay depth.
