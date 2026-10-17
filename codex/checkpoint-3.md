# Checkpoint 3 — journal MVP

Branch: `codex/checkpoint-3-journal`

## Scope

- Added a “Z pracowni” section, navigation link, featured article card, and future topic prompts.
- Added a standalone, linkable article draft about digital workflow and ceramic work, with primary sources and a link to the original portfolio post.
- Marked the text as pending Mikołaj's approval; added `noindex,nofollow` while it remains a draft.
- Documented file-based article creation and fields for a later publishing system.

## Verification and review

- HTML: one title and H1 per page, image alt text and local assets, all internal pages and fragment links, draft noindex — passed.
- Local HTTP: home page, article, stylesheet, and shared image returned 200 — passed.
- Browser: home journal and article rendered at 1280 px and 689 px without horizontal overflow; image loaded. Navigation and article structure appeared in the accessibility tree.
- `git diff --check` — passed.
- Independent review by `site_review`: PubMed and Ivoclar claims supported by source material; no Critical or Important findings. Two Minor points about the teaser image and draft indexing were fixed and re-reviewed. Reviewer could not access the local preview server from its session.

The article is an editorial sample and awaits Mikołaj's edits and approval before a public website launch. No CMS or author login was added in this checkpoint.
