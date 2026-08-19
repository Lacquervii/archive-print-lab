# Aspect-ratio contract — 16:9 default, explicit override

## Scope

The ordinary `Archive Print Lab / 旧档博物志` series canvas defaults to exact **16:9 landscape**. This is the default production profile, not an irreversible lock.

```text
default_ratio  = 16:9
selected_ratio = latest explicit user request, otherwise default_ratio
ratio_test     = for selected a:b, actual_width × b == actual_height × a
```

A latest explicit user ratio request overrides 16:9 and must be recorded as `ratio_source: explicit_user_override` with the requested ratio. A subject noun, backend/model preset, accidental backend return or convenience crop can never silently change the selected ratio. A ratio override changes canvas geometry only; it does not automatically change canonical mode, chassis, palette rules or series review.

## Working and final canvases

- **Default request target:** when the user names a generator, use its closest supported 16:9 target (e.g. `1792x1008` on gpt-image-2-style APIs); otherwise deliver the prompt with 16:9 framing instructions and let the user set the size.
- **Delivered image:** if rendering happens, use the returned file and record its actual dimensions.
- **Explicit ratio override:** choose the named generator’s matching supported target, or note the selected ratio in the prompt; record the requested ratio/source.
- **Returned backend image:** compare its dimensions with the request for transparent reporting; do not crop, normalize or rebuild it in a second production route.

A 3:2, 2.35:1 or 21:9 request is valid only when the user explicitly asks for it. It must never be reported as 16:9 merely because it is landscape.

## Default 16:9 layout consequences

The default 16:9 field establishes a repeatable page skeleton:

- broad upper title corridor;
- compact, generally lateral central event belt;
- contacting meso field crossing the belt;
- short lower release, not a tall tail;
- breathable side corridors that remain part of the composition.

For a ratio override, build an adapted layout plan before generation. Do not design for one ratio and crop it afterward; rebuild title fit, central envelope, meso contacts, corridors and release for the selected canvas.

## Backend enforcement

1. Put the exact **selected ratio** in the model-facing canvas sentence.
2. When the user names a generator, use its closest supported target for the selected ratio (e.g. `1792x1008` for 16:9 on gpt-image-2-style APIs); otherwise give the ratio instruction only.
3. If rendering happens, inspect the actual returned file against the selected-ratio test.
4. If the returned file does not match the selected ratio exactly, label the ratio status `near_match` or `mismatch` and report it honestly.
5. Deliver the returned result as generated; do not blindly center-crop, normalize or rebuild it.
6. Record default/override source, requested size and returned size when rendering happened.

## Pass/fail

For prompt delivery:

- report the selected ratio and, when rendering happened, requested/returned sizes without false claims;
- review the macro → meso → subject → release skeleton in the compiled plan and in any returned image;
- do not hide a mismatch with a filename or prose claim;
- do not add a second normalization workflow.

A nonmatching generated return remains a usable delivered image when clearly labeled with its actual dimensions.
