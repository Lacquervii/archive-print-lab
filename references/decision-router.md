# Decision router — choose the visual job, then the rendering-style branch

## Scope

Use this router for every request handled by `Archive Print Lab / 旧档博物志`. It prevents a successful reference case or recent failure from becoming the default composition for unrelated subjects. It also separates the selected **visual job** (mode/recipe/chassis) from the separately user-selected **rendering-style branch** (surface atmosphere); see `rendering-branches.md`.

## Canonical aspect ratio

The ordinary series canvas **defaults** to exact 16:9 landscape. Record one of these before planning:

```text
default:
  aspect_ratio: 16:9
  ratio_source: default_16_9
  requested_size: named generator’s closest 16:9 target, or ratio instruction only
  returned_size: report after rendering, when rendering happens
```

or, only when the latest user brief explicitly requests another ratio:

```text
ratio override:
  aspect_ratio: [user-requested ratio]
  ratio_source: explicit_user_override
  requested_size: [named generator’s matching target, or ratio instruction only]
  returned_size: report after rendering, when rendering happens
```

A subject noun, model preset, accidental backend return or convenience crop cannot silently alter the selected ratio. Compare the backend return with the **selected** ratio and report it as exact, near-match or mismatch. A ratio override changes geometry only—it does not automatically alter the canonical mode, chassis, palette or series review.

## Canonical default

For an ordinary invocation that names a subject and asks for a poster, cover, visual, image or generation without an explicit alternate viewer job, use the canonical series shell in `family-standard.md`:

```text
concentrated_cover + concentrated editorial cover + structural chassis
```

This fixes the page skeleton, not the subject, color or source inventory. A hero, material, process, archive, narrative, information or quiet route is an **explicit mode override** and must be recorded as such. A noun like “book”, “computer” or “mouse” does not silently switch the family into `hero + active`.

The canonical shell is not a command to copy 9010/9014’s flowers, purple, frames, title or exact geometry. It is the stable macro → meso → subject → release contract that makes separate themes read as one series.

The router decides what the image must do before deciding how it should look:

```text
selected ratio → canonical series shell → task action → subject behavior → reference evidence → visual mode → recipe → chassis intensity → theme compiler → composition plan → rendering-style branch selection → backend
```

## Fixed versus selected

Keep these levels separate:

- **Canonical series shell:** the stable page contract for ordinary poster/cover requests: upper macro title, compact central event, contacting meso field, soft/hard layer separation and authored release.
- **Fixed engine:** hierarchy, meaningful scale contrast, relationship, crop, material cause, layer tension and deliberate release.
- **Fixed family tone:** the family-level relational atmosphere—materially controlled field, localized dark volume, selective diffusion, crisp structural contrast, asymmetry, restrained accent and tactile surface. It does not itself select a nostalgic or retro treatment.
- **Rendering-style branch:** the surface-atmosphere route is selected internally from theme evidence plus whole-composition fit. It may be `contemporary_frosted`, `warm_analog_print`, `crisp_modern_graphic`, `material_archive` or custom. This is not a user-facing menu for ordinary requests; an explicit user direction overrides it.
- **Selected mode:** concentrated cover by default; hero poster, archive/specimen, material/process study, narrative scene, information system or quiet plate only as an explicit override.
- **Selected recipe:** the pressure profile chosen for the selected mode and viewer action; ordinary requests use the concentrated editorial cover recipe.
- **Selected chassis intensity:** `structural` by default for the canonical shell; `none`, `light` or `active` only when an explicit alternate mode justifies the reduction. See `graphic-chassis.md`.
- **Theme compiler:** subject proposition, complete gestalt, supports, meso events, material proof, provenance-aware carrier translation, palette roles and refusal plan.
- **Composition plan:** macro plane, central envelope, contacts, chassis members, corridors, release and layer order.
- **Production choice:** prompt compilation, with optional rendering adaptation when the user names a generator.

A mode is not a style adjective. It is a contract about attention, reading path, density and subject arrangement.

## Preflight record

Before selecting a mode, record:

1. **Task action** — what should the viewer do first: identify, feel, understand, inspect, compare, remember, or navigate?
2. **Subject behavior** — is the subject one event, a family, a process, a material state, a narrative scene, or an information system?
3. **Carrier** — poster, cover, hero, material plate, archive plate, process study, scene, diagram, or other.
4. **Aspect ratio:** default exact 16:9 landscape; use `aspect-ratio-contract.md` and `canonical-layout-spec.md`. A latest explicit user ratio request sets `ratio_source: explicit_user_override`; request a matching target and verify the returned file against the selected ratio. Never silently accept a backend convenience ratio.
5. **Reference evidence** — what is actually visible and transferable: title as image, central cluster, sequence, image treatment, material continuity, diagram logic, or quiet field.
6. **Canonical series shell:** upper title plane, compact central event, contacting meso field, soft/hard tension and authored release. Record an explicit mode override only when the latest brief requests another viewer job.
6. **Rendering-style branch:** resolve internally from theme evidence and overall palette/composition fit before generation. Do not expose a branch menu for an ordinary request. Record the internal choice; a direct user style instruction overrides it. Ask only when the brief is contradictory.

Do not infer these fields from the subject noun alone. “A book”, “a computer”, or “a flower” does not select a mode, a chassis intensity, a composition plan, or a surface-atmosphere branch.

## Chassis selection after mode

Choose `none`, `light`, `active`, or `structural` only **after** visual mode and recipe are selected. See `graphic-chassis.md`.

- A narrative scene, quiet plate or factual process may use `none` or `light` even inside the same visual family.
- A hero poster can use `light` for title/print family continuity without manufacturing a dense diagram field.
- A designed relational cover may use `active` or `structural` when the reference evidence and viewer action need a soft-image / crisp-graphic tension with real page pressure.
- Chassis selection does not license copied purple rectangles, literal source symbols, false annotations, HUD furniture, or subject fragmentation. Translate profile grammar through the new theme and carrier.
- Keep title wording and graphic marks generator-safe; do not promise reproducible vector geometry.

## Mode selection table

### Concentrated editorial cover

This is the canonical default for ordinary poster, cover and visual-generation requests. For an explicit alternate mode, use it only when the viewer job still needs a strong first-attention plane, compact relational subject family, visible structural field and authored release. Do not impose it on a brief explicitly asking for a singular hero, product image, factual archive, process explanation, material study, narrative scene, information system or quiet plate.

### Hero poster / singular event

Select when one subject, gesture, object, person, or event must be understood immediately and supporting elements should remain subordinate. Scale and focal clarity lead; repetition and structural furniture decrease. A title may be integrated, but it does not have to create a four-rung cluster.

### Archive / specimen plate

Select when collecting, indexing, cataloging, comparing, or documenting several instances is the actual task. Labels and systematic marks may become important, but the system must explain the collection. Do not let an archive request collapse into a decorative concentrated cover.

### Material / process study

Select when surface, transformation, construction, wear, light, or physical credibility is the subject. Material operations carry the hierarchy. Typography and external graphics become subordinate unless the brief makes them structural.

### Narrative editorial scene

Select when place, time, action, atmosphere, or a relationship between figures and environment is the main content. Build a reading path and figure-ground relation. Do not force a central cluster, title plane, or poster scaffold if it damages the scene.

### Information / diagram system

Select when nodes, sequence, comparison, evidence, labels, axes, or explanation must be understood. Information hierarchy and semantic connections lead. Decorative editorial marks cannot replace a readable system.

### Quiet art-book plate

Select only when calm, silence, minimalism, or broad empty space is explicit in the brief or strongly evidenced by the reference. Quiet is a chosen task behavior, not a default response to a delicate subject.

## Decision rules

Use the following order when several modes seem possible:

4. If one singular event must dominate **and the brief explicitly asks for a hero/singular presentation**, choose Hero before Concentrated Cover.
5. If material transformation or surface credibility is the message **and explicitly requested**, choose Material/Process before adding title architecture.
6. If place, time, action, or atmosphere is essential **and explicitly requested**, choose Narrative Scene before poster mechanics.
7. Otherwise retain the canonical Concentrated Cover shell; an object noun or a model preference does not constitute an override.
8. Keep type and mark expectations image-native and generator-aware; use short displayed words and do not promise exact geometry or deterministic reading order.

## Concentrated-cover activation test

For the canonical default, this test is already active. For an explicit alternate mode, do not load concentrated-cover machinery unless the user still requests its page pressure. The canonical shell must not be accidentally downgraded by a subject-first prompt.

## Mode record

The internal decision record should state:

```text
mode:
viewer_action:
subject_behavior:
first_attention:
subject_arrangement:
subject_footprint:
protected_corridors:
chassis_intensity:
chassis_role:
structural_role:
composition_plan:
density_distribution:
release_role:
typography_role:
title_fit:
rendering_style_branch:
rendering_style_selection_source:
backend:
refusal_list:
```

The record is for reasoning and review. Convert it into natural spatial prose before sending a prompt to an image model. Do not expose mode labels, quotas, percentages, or audit language as if they were visual instructions.

## Mode-fit review

Before judging beauty or subject detail, ask:

- Does the image perform the selected viewer action?
- Does its density distribution match the selected mode?
- Is the subject arrangement appropriate to its behavior?
- Is typography doing the selected job rather than borrowing a reference role?
- Are structural marks serving the mode, or merely announcing “editorial”?
- Would another mode make the same subject more truthful and effective?

If the answer to the last question is yes, diagnose a **router or recipe failure**, not a subject-detail failure.
