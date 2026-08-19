# Canonical layout specification — default 16:9

```text
layout: canonical-diffused-editorial-16x9
mode: concentrated_cover
recipe: concentrated_editorial_cover
chassis: structural
```

## Default zones

Use normalized coordinates from `(0,0)` at upper-left to `(1,1)` at lower-right. These are planning guides, not literal model instructions.

- title corridor: upper `y=0.00..0.27`, title broadly spanning the field while staying contained;
- central event: generally `x=0.20..0.80`, `y=0.27..0.79`, broad rather than a narrow column;
- meso field: roughly `x=0.15..0.85`, `y=0.27..0.80`, with unequal carriers and visible contact;
- release: lower `y=0.79..1.00`, quieter and connected to the central event.

Protect side breathing fields and a lower/right reading corridor. Do not casually crop a planned page into another ratio.

## Weight ladder

```text
1. title / glyph authority
2. compact central subject
3. contacting meso field
4. localized dark anchor
5. sparse micro evidence
6. quiet release
```

## Ratio reporting

The default ratio is 16:9; the concrete request target follows the generator the user names (on gpt-image-2-style APIs, commonly `1792x1008`). Record the actual returned size when rendering happens. If the returned dimensions are not exact 16:9, report `near_match` or `mismatch`; do not hide the difference or rebuild the image.

For the canonical concentrated cover, ratio reporting does not relax composition pressure: the title corridor, broad central event, unequal contacting field, protected release, and series imprint are planned before the backend return is inspected.
