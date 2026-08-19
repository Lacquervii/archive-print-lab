# Backend adapters — optional execution layer

## Principle

This Skill compiles themes and prompts; it needs no generator at all. When the user names one, adapt only the prompt format, size parameters, and delivery notes. No image model, API key or generation service is required for the Skill to work.

## General rule

Resolve the visual mode, recipe, selected ratio and rendering-style branch first. The generator is chosen after those decisions, never before. A model cannot repair a wrong mode, an unverified canvas, or a surface atmosphere that was never selected.

## Adapter notes (non-exhaustive)

- A canonical Image2 cover may use the optional `image2-editorial-adapter.md`: it restores broad title pressure, a rich lateral central belt, unequal primary/support/return carriers, localized dark anchors and the small `archive-print-lab` colophon without making the family Image2-only.
- **Midjourney:** keep the scene in natural language, add `--ar 16:9` (or the selected ratio), keep the title short, and move the refusal list into a concise negative description. Do not promise deterministic text or vector geometry.
- **Flux / SDXL / Stable Diffusion family:** split the scene into positive prompt tags plus a compact negative prompt; set the aspect ratio parameter or canvas size for the selected ratio; keep typography short and accept approximate lettering.
- **ComfyUI / WebUI:** same decisions; expose the prompt as the positive text, the refusal list as negative text, and the ratio as the canvas size or latent size.
- **即梦 / 通义万相 / 豆包 / Gemini / other consumer generators:** paste the natural-language scene, set the ratio if offered, and keep displayed words short. These tools vary in how much text they can render accurately.
- **Unknown or unnamed tool:** deliver the natural-language scene plus a note that framing, aspect ratio and negative prompts should be adapted to the user’s generator.

## Image-to-image

Use an image as an input only for an explicit edit, transformation or recreation the user requests. Explain that content leakage is possible and inspect the result for source nouns, palette, text, and geometry leakage.

## Delivery honesty

- Report actual returned dimensions, not requested dimensions, whenever rendering happens.
- Never claim exact text or geometry when the pixels (or the generator’s known behavior) do not support it.
- Store the final prompt beside the image for reproducibility.
- Never claim a prompt was recovered verbatim when it was reconstructed.
- If no generator is available in the current environment, say so and still deliver the prompt plus the exact parameters the user would need elsewhere.
