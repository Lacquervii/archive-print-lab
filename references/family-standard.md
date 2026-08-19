# Canonical family standard — Diffused Editorial Series

## Purpose

This is the **series-level contract** for ordinary poster/cover requests handled by `Archive Print Lab / 旧档博物志`. It restores a stable house standard without freezing the subject, palette or material.

The family is recognizable through a repeated page event:

```text
macro title plane
→ compressed central subject event
→ visible contacting meso field
→ authored lower release
```

Theme customization changes what carries each role. It does not delete the roles or freely replace the carrier with a different poster genre.

## Activation and overrides

Activate `canonical-series-cover` when the user invokes this Skill with a subject and asks for a poster, cover, visual, image or generation without explicitly selecting another mode.

Explicit overrides are allowed only when the brief says so, for example:

- `hero poster` / `singular portrait` → hero override;
- `material study` / `macro material plate` → material override;
- `process`, `archive`, `diagram`, `narrative scene`, `quiet plate` → corresponding override;
- `Image2` → one possible rendering path, adapted from this Skill’s prompts; never a requirement.

A subject noun alone never activates an override. “Mouse”, “book” and “computer” remain canonical-series covers unless the user asks for a product image, hero image, process plate, or another explicit job.

## Non-negotiable page roles

### 1. One uninterrupted default-16:9 carrier

Default is one exact 16:9 landscape editorial cover: no split screen, diptych, stacked panels, collage divider, catalog grid or unrelated scene. The **latest explicit user ratio request may override 16:9**; record it as a ratio override without changing the series identity or silently changing the visual mode. Build the title corridor, lateral central event and short release for the selected ratio from the beginning. Do not design at one ratio and casually crop to another.

### 2. Macro title plane

A short title, word pair or abstract glyph mass is the first structural event by default.

- **visual mass occupies 1/3–1/2 of the full page, targeting roughly 2/5 by default**; this is title authority across the page, not merely the height of a neat text line;
- leave a small clean breathing gap above the title, approximately 3%–5% of the canvas height;
- keep the title fully inside the canvas with narrow but definite side margins; do not force edge-to-edge bleed or accidental cropping;
- spread broadly across the upper field and may overlap into the upper middle, with the compact subject visibly interrupting its lower edge;
- must read before the subject at thumbnail scale; if the title reads as a header/caption, the composition fails;
- the central subject stays materially rich but externally small enough that the title retains this dominance;
- Any image generator’s lettering is image-native and approximate; use short displayed words rather than requiring exact typography.

The title may be dark, accent-colored or materially translated, but its role and authority remain stable.

### 3. Compact central event

The middle is a designed event, not a subject placed on empty paper.

- one dominant readable gestalt;
- unequal supporting whole forms, echoes, states, shadows or material returns;
- front / middle / rear depth;
- meaningful overlap, crop and at least one local dark anchor;
- a bounded, generally lateral middle envelope with usable air around it;
- internal richness without an oversized outer silhouette.

For an artifact, supporting forms default to whole-object echoes, reflections, shadows or use traces. Detached parts are allowed only when process/archive/construction is the stated viewer job.

### 4. Visible meso field

Every canonical-series cover must contain a readable medium-scale field between title and micro marks. It can be theme-native, carrier-native, profile-native or mixed, but it must be translated for the current theme.

- one coherent field, not isolated decoration;
- several unequal planes, paths, shadows, contours or blocks with shared direction;
- at least three visible contacts: interrupt, pass behind, get cut, align, disappear/reappear, or continue into release;
- visible at normal viewing distance;
- subordinate to the complete subject unless the title plane is intentionally first;
- no universal purple rectangles, stars, labels, fake data or HUD furniture.

A hero override may reduce this to a light chassis. The canonical default may not silently reduce it to one faint line. For Image2, preserve a readable primary/support/return field and at least three distinct contacts before adding micro marks; if source-specific furniture is removed, replace its lost pressure with theme-native overlap, dark anchors, scale contrast or translated planes rather than simply making the page sparser.

### 5. Soft / hard layer separation

Keep a tactile matte or diffused material/image layer distinct from a crisp flat printed/structural layer:

- material layer: volume, localized occlusion, selective focus, frosted edges;
- structural layer: type, planes, paths, blocks, registration and short marks;
- both layers must contact, occlude or align rather than float independently.

### 6. Closed, theme-derived color system

Color is variable; color roles are fixed.

Every canonical series image contains:

- a resolved field/substrate;
- localized dark volume;
- one primary theme-derived accent;
- optional secondary hue only with a stated job;
- resolved title and graphic inks;
- a short inherited-hue prohibition.

The accent may be purple for a craft theme, orange for a mouse, ochre for a book, or another justified family. Hue variation is expected; role variation is not.

### 7. Authored release

The lower field and outer margins are quieter than the central event but not accidental leftovers.

- preserve a continuous lower or lateral pause;
- carry one low-weight continuation of a shadow, plane, contour, material residue or short label;
- on canonical generated covers, place a tiny lowercase `archive-print-lab` imprint in this release, aligned to an existing rule or axis and clearly subordinate to the title and subject;
- no repeated second subject;
- no dead blank band and no perimeter clutter.

## Canonical scale ladder

Use this as a review scaffold, not as a prompt full of numbers:

```text
macro  = title / glyph authority
meso   = contacting structural field
subject = compact rich theme event
micro  = sparse index + material proof
release = quiet authored continuation
```

At thumbnail size, macro + subject + release must be legible. At normal distance, the meso field and contacts must appear. At close range, material proof and print finish must reward inspection.

## Allowed variation budget

The following may change freely when justified:

- subject grammar and complete gestalt;
- material and surface behavior;
- substrate temperature and palette family;
- title word, language and type character;
- geometry of planes/paths/contours;
- density inside the central envelope;
- release trace;
- aspect ratio within a coherent carrier;
- Image2 prompt / any generator prompt production.

The following may not change silently in the canonical default:

- title/glyph authority as the macro role;
- compact central event as the subject role;
- visible contacting meso field;
- soft/hard layer tension;
- local dark pressure;
- lower authored release;
- one continuous editorial carrier;
- review at thumbnail, normal and close distance.

## Production standard

When the output is generated, use the named generator’s interpretation but preserve the compiled page pressure. Image-native renderers may approximate lettering, fine marks and geometry; the prompt should still carry the full title → broad central event → unequal contacting field → release sequence. The tiny series imprint is part of the canonical release and should be attempted in-image; report any lettering approximation honestly.

## Canonical pass/fail gates

Pass only when all applicable gates hold:

1. hidden-subject test still reveals the same macro → meso → subject → release page skeleton;
2. title has real authority and subject contact;
3. central event is compact, unequal and materially specific;
4. meso field is visible at normal distance and has at least three meaningful contacts;
5. soft and crisp layers are distinct;
6. palette is fresh but role-consistent;
7. lower release is authored and connected;
8. no source-case inventory has leaked;
9. actual returned size (when rendering happens) and image-native text limitations are reported accurately.

If a result is attractive but fails the page skeleton, it is not a pass. Diagnose the failed role—router, series contract, composition, theme, palette or backend—instead of adding more style adjectives.

## Series identity statement

A successful adaptation should be describable in one sentence without naming its subject:

> A wide pale/materially controlled editorial cover with a dominant upper title plane, a compact dark-anchored central event, a contacting flat structural field, selective matte diffusion, a fresh closed palette, and a quiet but authored lower release.

If two outputs cannot both satisfy this sentence at thumbnail and normal distance, they are not yet members of the same canonical series.
