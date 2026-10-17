# Checkpoint 1 — local Kozak Lab page

Date: 2026-10-17
Branch: `codex/checkpoint-1-single-page`

## Scope

- Built a Polish, static, responsive one-page portfolio.
- Added a clear route to the public `@kozak_lab` Instagram profile for real work and contact.
- Added two generated illustrative photographs, each visibly labelled on the page.
- Kept unverified product categories, prices, testimonials, turnaround claims, and patient images out of the draft.

## Verification

- `git diff --check origin/main..HEAD`: passed before the evidence commit.
- Local HTTP preview: `/`, `/styles.css`, both JPEG assets, and `/assets/favicon.svg` returned HTTP 200.
- HTML structure check: one H1, internal anchors resolve, external links target the known Instagram profile, and local assets exist.
- Browser at 689 px viewport: no horizontal overflow; hero, portfolio, and contact sections inspected visually; all three mobile navigation links visible; Kontakt link reached `#kontakt`; skip link reached `#main` from keyboard focus.

## Independent review

- Initial review found one Important issue: mobile navigation links were hidden. It also noted two Minor copy issues around illustrative imagery and clinic targeting.
- Focused fixes restored mobile links and clarified the portfolio and clinic copy.
- Follow-up independent review of `4b06291..6ce9a8c` found no remaining Critical or Important issues.

## Content needed before public launch

Confirm Mikołaj's actual product list, preferred contact channel, service area, order process, and permissions for any real work photographs. The current site is a local draft.
