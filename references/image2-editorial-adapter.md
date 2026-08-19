# Image2 editorial adapter — restore canonical cover pressure

## Scope

This is an **optional backend adapter**, loaded only when the user names Image2 / gpt-image-2 (or an equivalent natural-language image generator). It restores the production constraints that make the Archive Print Lab family survive an image-native render without making the Skill itself Image2-dependent.

The generator-neutral contract remains authoritative. This card translates the selected canonical plan into Image2-safe spatial prose; it does not change the theme, surface branch, ratio decision, or family roles.

## Canonical Image2 preflight

```text
mode: concentrated_cover
recipe: concentrated_editorial_cover
chassis: structural
ratio: 16:9 by default
requested_target: 1792x1008 when supported
surface: resolved before rendering
editorial_imprint: tiny lowercase “archive-print-lab” in the release
```

If the user explicitly selects another mode, use that mode's chassis and density; do not apply this pressure profile mechanically.

## Pressure restoration rules

### Macro title

- Make the title a broad, composition-shaping image plane, not a neat header.
- Target roughly one-third to one-half of the page's visual mass, with about two-fifths as the default pressure target.
- Keep a small clean top breathing gap of approximately 3–5% of the canvas height and narrow definite side margins. Contained does not mean timid: the title should still span most of the upper field and may enter the upper middle.
- Let the complete central event visibly interrupt the lower edge of the title.
- Choose the strongest short display title for the theme. Do not automatically replace a visually authoritative common-name word pair with a weaker taxonomic abbreviation merely because it is shorter; use a small botanical/specification line only as a subordinate aid when useful.

### Central event

- Build a broad, generally lateral middle belt rather than a narrow vertical column.
- Preserve one complete dominant gestalt plus unequal related whole-form echoes, front/middle/rear depth, internal overlap, a localized dark anchor, and material evidence.
- For organic subjects, stems, spines, trunks or axes may remain present, but they must be countered by lateral forms, cross-structure, shadow mass, leaf/petal spread, or a contacting field so the page does not become a single line.
- Keep the outer envelope controlled while making the interior rich. Do not solve a weak center by either enlarging it to the edges or reducing it to one polite icon.

### Meso field

For the canonical structural cover, compile a visible unequal trio of related carriers. These are roles, not mandatory literal shapes:

1. **primary carrier** — the main plane, disc, contour, shadow or graphic field;
2. **support carrier** — an unequal block, plane, path, echo or counter-pressure;
3. **return carrier** — a member that disappears behind the subject and reappears toward the release.

At normal viewing distance the trio should read as one coherent printed field. Use visible spatial contacts: the title is interrupted, a plane passes behind the subject, a member is cut and reappears, a dark anchor sits behind a light material form, and the field continues into the release. Do not reduce the field to one faint line, one isolated circle, or decorative corner furniture.

The carriers may be theme-native, carrier-native, profile-native, or mixed, but each must have a current page job. Re-author direction, opacity, scale, color and contact for the subject. Never copy a prior theme's purple frames, symbols or literal geometry.

### Micro layer and release

- Use a small but legible subject-specific index system when the canonical cover benefits from it: usually two to four short labels, one scale/axis gesture, and one or two restrained registration marks. They must align with actual forms or carrier edges; they are not fake scientific data.
- Reserve a connected lower-right release with one fading field edge, contour, shadow, material residue or short rule. It must be quiet but visibly authored.
- In that release, add the tiny lowercase imprint **“archive-print-lab”**, widely tracked and low contrast, aligned with the short rule or study/edition label. It is a publication-like colophon, not a watermark, logo, badge or second title. Keep it subordinate to the title, subject and meso field.

## Image2 prompt order

Write one coherent scene in this order:

```text
canvas and intended reading
→ broad title plane and contained fit
→ complete compact central event and lateral envelope
→ primary/support/return meso carriers with front/back contacts
→ localized dark anchor and sparse theme index
→ connected release with “archive-print-lab” imprint
→ selected surface branch
→ material, lighting, palette and short refusal block
```

Use visible verbs: `spans`, `enters`, `interrupts`, `overlaps`, `passes behind`, `is cut by`, `reappears`, `aligns with`, `recedes`, and `releases into`.

Do not send internal labels such as `macro`, `meso`, `trio`, `quota`, `chassis`, or `pressure profile` to the model. Compile them into spatial prose first.

## Image-native text boundary

Image2 can approximate words, labels and fine marks. Keep the title and imprint short, state that lettering is approximate, and never claim exact spelling from pixels.

## Targeted refusal block

Use only strong priors for the current theme: generic bouquet/field postcard, product still life, detached specimen sheet, fake textbook diagram, random HUD, edge-filling subject, or dead blank release. A positive spatial plan should carry most of the prompt.

## Adapter review gate

Before calling an Image2 result a useful canonical exploration, check:

- title has real upper-plane authority without touching the top edge;
- central event is complete, rich and broadly packed;
- the printed field has visible unequal members and at least three readable contacts;
- local dark pressure survives;
- the lower-right release is connected and contains the small imprint or a clearly attempted imprint;
- the image has not drifted into a generic subject poster or a narrow vertical story.

A result may still be attractive with approximate lettering or a near-match backend size, but those limitations must be reported honestly.
