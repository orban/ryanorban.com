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

Three theme partials are overridden in `layouts/` to fix Hugo 0.158 compatibility:

- `layouts/partials/head.html` — fixes deprecated `site.Author` → `site.Params.author.name`
- `layouts/partials/head/math.html` — adds `$...$` inline math delimiter, removes broken SRI hashes
- `layouts/partials/svg/Link.html` — fixes missing dict context error
- `layouts/404.html` — fixes `site.Author.email` → `site.Params.author.email`

### Config

`hugo.toml` — all site configuration including menus, params, markup settings, and Goldmark passthrough for LaTeX delimiters.

## Content Conventions

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

- The TIL theme (v0.6.0) has bugs with Hugo 0.158+ around `site.Author` and SVG partial context — the layout overrides fix these
- KaTeX SRI integrity hashes from jsdelivr can be incorrect — the math partial omits them intentionally
- The `vis-network` npm package must be installed for the graph feature to work
- `static/CNAME` must contain `ryanorban.com` for the custom domain to work on GitHub Pages
