# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio and blog for Ryan Orban, hosted on GitHub Pages at ryanorban.com. Built with Hugo and the TIL (Today I Learned) theme.

## Tech Stack

- Hugo static site generator (v0.116+ required, extended edition not required)
- Hugo TIL theme installed as a Hugo module (`github.com/michenriksen/hugo-theme-til`)
- KaTeX for LaTeX math rendering (loaded via CDN on pages with `math: true`)
- vis-network npm package for the content graph feature
- GitHub Actions for build and deploy

## Development Workflow

```bash
# Local dev server with live reload
hugo server

# Build for production
hugo --minify

# Install/update theme module
hugo mod get -u
```

To deploy, commit and push to `master` — GitHub Actions builds and deploys to Pages automatically.

## Site Structure

```
content/
├── _index.md              # Homepage (bio summary + recent posts/notes)
├── about.md               # Full background and experience
├── advising.md            # Advisory services page
├── office-hours.md        # Calendly booking page
├── posts/                 # Blog posts (full articles)
│   └── stop-testing-agents-like-deterministic-code.md
└── notes/                 # TIL-style short notes
    └── _index.md
```

### Layout Overrides

Everything in `layouts/` shadows the theme module. There are twelve files, in three groups.

**Homepage ("Working Record") — a separate design that only runs on `.IsHome`:**

- `layouts/_default/baseof.html` — forks the theme's shell. On `.IsHome` it emits the
  `working-record-site` body, skip link, record header/nav, and record footer. The `else`
  branch is a copy of the theme's non-home body and must stay in sync with it (see Pitfalls).
- `layouts/_default/home.html` — the entire homepage. All homepage copy lives here, not in
  `content/_index.md`, which is frontmatter only.

**Hugo 0.158+ compatibility fixes:**

- `layouts/partials/head.html` — fixes deprecated `site.Author` → `site.Params.author.name`;
  also owns the font preload and the home/non-home inline CSS branch
- `layouts/partials/head/math.html` — adds `$...$` inline math delimiter, removes broken SRI hashes
- `layouts/partials/svg/Link.html` — fixes missing dict context error
- `layouts/404.html` — fixes `site.Author.email` → `site.Params.author.email`

**Notes and content presentation:**

- `layouts/notes/list.html`, `layouts/partials/notes/list.html` — notes index with search and
  category graph
- `layouts/_default/graph.json.json` — graph data feed
- `layouts/_default/_markup/render-image.html`, `layouts/partials/page/meta.html`,
  `layouts/partials/posts/list.html`

### Stylesheets

`layouts/partials/head.html` inlines exactly one of two stylesheets, never both:

- `static/css/home.css` — homepage only. Scoped to `.working-record-site` / `.record-*`.
  Hard constraints, enforced by the audit: no `!important`, no `:has()`, no gradients,
  no box shadows, no broad global overrides.
- `static/css/custom.css` — every non-home page (`/about/`, posts, ~900 notes). Uses
  `!important` heavily against the theme's Tailwind build.

A class only used by one of the two pages must not live in the other file — dead `.home-*`
rules were previously inlined into every note page.

### Homepage Audit

```bash
python3 scripts/audit_homepage.py
```

Builds the site into a temp directory and asserts the homepage contract: figures match the
essay they link to, internal links resolve, `/notes/` has a human navigation path, list
semantics, lazy loading, social metadata, heading/aria structure, CSS invariants, and colour
contrast. Run it after any change to `home.html`, `baseof.html`, `home.css`, `hugo.toml`,
or `content/_index.md`.

### Config

`hugo.toml` — all site configuration including menus, params, markup settings, and Goldmark passthrough for LaTeX delimiters.

## Content Conventions

- `content/_index.md` is frontmatter only (`title`, `description`, `images`). `images` is what
  produces `og:image` and the `summary_large_image` Twitter card. Homepage copy is in
  `layouts/_default/home.html`.
- Blog posts go in `content/posts/` with frontmatter: `title`, `date`, `description`
- Add `math: true` to frontmatter for pages that use LaTeX (`$...$` inline, `$$...$$` block)
- Notes go in `content/notes/` with frontmatter: `title`, `date`, `categories`
- Static assets (images, CNAME) live in `static/`

## Deploy

Push to `master` triggers `.github/workflows/hugo.yml` which:
1. Installs Hugo extended + Go + Node
2. Runs `npm install` (for vis-network)
3. Runs `hugo --minify`
4. Deploys to GitHub Pages

## Pitfalls

- **`layouts/_default/baseof.html` permanently shadows the theme's.** A fork is necessary
  because the homepage needs a different body, but it means a `hugo mod get -u` that changes
  the theme's `baseof.html` will silently never reach any page, and nothing will fail. When
  updating the theme, diff the module's `layouts/_default/baseof.html` against the non-home
  branch of the local one and port any changes by hand.
- The TIL theme (v0.6.0) has bugs with Hugo 0.158+ around `site.Author` and SVG partial context — the layout overrides fix these
- KaTeX SRI integrity hashes from jsdelivr can be incorrect — the math partial omits them intentionally
- The `vis-network` npm package must be installed for the graph feature to work
- `static/CNAME` must contain `ryanorban.com` for the custom domain to work on GitHub Pages
