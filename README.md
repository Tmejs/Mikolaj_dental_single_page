# Kozak Lab — one-page website

Static, Polish-language portfolio page for dental technician Mikołaj Kozak.

## Preview locally

From this directory, run `python3 -m http.server 4173`, then open `http://localhost:4173/`.

The page uses only local HTML, CSS, and images. Contact buttons open the public [@kozak_lab Instagram profile](https://www.instagram.com/kozak_lab/). The hero photograph is a generated illustration and is labelled on the page. The work section contains photos from Mikołaj's own [e.max crowns and veneers](https://www.instagram.com/kozak_lab/p/C6Lt3WttWBO/), [feldspathic veneers (2024)](https://www.instagram.com/kozak_lab/p/C5WOCHLNJHn/), and [handmade feldspathic veneers (2021)](https://www.instagram.com/kozak_lab/p/COilRUqpZaP/) posts; each card links to its source.

## Journal MVP

The home page has a “Z pracowni” section linking to one article at `artykuly/cyfrowy-workflow-i-ceramika.html`. It is a clearly labelled editorial draft for Mikołaj to review, not a statement that he wrote or approved it. Its factual material claims link to source material; the photograph links to his original post. The article is accessible at its own URL when the static folder is served.

To add another article locally, copy the article HTML file into `artykuly/`, update its title, meta description, headings, body, references, and internal links, then add a linked card in the home page journal section. Check the new page on mobile and desktop and ask Mikołaj to approve the writing before publishing it. A future CMS can store the same fields: slug, title, summary, author, approval status, date, cover image with alt text, body, and sources. No CMS or login is part of this MVP.

The design and content plan is in [PLAN.md](PLAN.md). The three portfolio photographs come from Mikołaj's public Instagram posts and were added at the user's request; each links to its source post. Confirm the full current product list, practical ordering details, and contact preferences before publishing the website. Obtain separate consent before adding patient imagery.
