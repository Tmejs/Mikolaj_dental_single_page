# Checkpoint 2 — Instagram work gallery

Branch: `codex/checkpoint-2-instagram-work`

## Scope

- Added three selected photographs from Mikołaj Kozak's public Instagram posts, linked to their source posts.
- Used photos of restorations on dental models without visible patient identifiers.
- Added responsive cards and captions; removed the unused generated work image.
- Updated source and content notes in `README.md` and `PLAN.md`.

## Verification and review

- HTML structure and local assets: three sourced cards, three images with alt text and lazy loading, gallery group role — passed.
- Local HTTP responses for the page, stylesheet, and three JPEGs — passed.
- Caption contrast against the card background: 5.03:1 — passed WCAG AA normal text threshold.
- Responsive browser inspection at 689 px: gallery displayed without horizontal overflow.
- `git diff --check` — passed.
- Independent review by `gallery_review`: initial Important caption contrast finding fixed; re-review found no Critical or Important findings. Reviewer verified post captions and dates against source posts and found no visible patient identifiers. Reviewer could not independently inspect the local browser because its file preview was blocked.

The website remains a local preview. Product details and contact preferences still need confirmation before a separate public launch.
