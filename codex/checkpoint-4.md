# Checkpoint 4 — font-led K monogram studies

Branch: `codex/checkpoint-4-k-monograms`

## Scope

- Replaced the rejected hand-drawn concept set with ten K glyphs from named script and italic typefaces.
- Bundled the ten source fonts and their SIL OFL license files from the Google Fonts repository.
- Generated portable SVG outlines, an individual option board with 40 px previews, and one comparison sheet.
- Left the production website mark and favicon unchanged pending a selection.

## Verification and review

- Ten font files and ten corresponding OFL texts present.
- Ten SVG files and the comparison sheet parsed as valid XML and served over local HTTP.
- Regeneration with fontTools produced no file changes; `git diff --check` passed.
- Browser inspection: all ten marks rendered in the board and sheet at desktop width.
- Independent review by `site_review`: no Critical or Important findings; all assets loaded, no horizontal overflow at 320 px, 40 px previews visible, and production logo unchanged. A Minor documentation mismatch about the fontTools dependency was corrected. The reviewer noted that Pinyon Script's thin hairlines warrant an actual favicon size check if selected.

The concepts are for selection and refinement. No logo has been applied to the website.
