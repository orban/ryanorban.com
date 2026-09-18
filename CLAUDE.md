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
├── posts/                 # Essays (full articles)
│   ├── _index.md          # Section title only ("Writing")
│   └── stop-testing-agents-like-deterministic-code.md
└── notes/                 # TIL-style short notes
    └── _index.md
```

### Layout Overrides

Everything in `layouts/` shadows the theme module. There are twenty files, in four groups.

**"Working Record" — a separate design, on the homepage, `/about/`, `/posts/` and the essays:**

- `layouts/partials/record/shell.html` — a returning partial, and the only definition of
  which pages are record pages. Returns `.on` (uses the record shell) and `.ownsTitle`
  (the body supplies its own `<h1>`, so the running head demotes to a `<p>`). Three ways
  in: the homepage by kind, `layout: "record"` in front matter, and the `posts` section.
  `baseof.html` and `head.html` both read it, because they have to agree — a record body
  with `custom.css` inlined renders as unstyled prose.
- `layouts/_default/baseof.html` — forks the theme's shell. For a record page it emits the
  `working-record-site` body, skip link, record header/nav, and record footer; nav anchors
  are in-page on the homepage and root-relative elsewhere. The `else` branch is a copy of
  the theme's non-record body and must stay in sync with it (see Pitfalls).
- `layouts/_default/home.html` — the entire homepage. All homepage copy lives here, not in
  `content/_index.md`, which is frontmatter only.
- `layouts/_default/record.html` — the template `layout: "record"` selects. Thin on
  purpose: it emits `.Content` and nothing else, so a record page authors its own rows.
  `/about/` is the only page using it.
- `layouts/posts/single.html` — an essay. Title, date on the spine, then `.Content` in a
  `.record-prose` container. Keeps `partial "page/meta"` for backlinks and the graph.
- `layouts/posts/list.html` — `/posts/`. Reuses `posts/single.html`'s header and the
  homepage's `.record-writing-list` rows. **Keep the `.Paginate` call**: it is what makes
  Hugo emit the `/posts/page/1/` alias, and that URL is in the pre-migration baseline, so
  a plain `range` fails `validate_site.py`.

**Hugo 0.158+ compatibility fixes:**

- `layouts/partials/head.html` — fixes deprecated `site.Author` → `site.Params.author.name`;
  also owns the font preload and the record/non-record inline CSS branch
- `layouts/partials/head/math.html` — adds `$...$` inline math delimiter, removes broken SRI hashes
- `layouts/partials/svg/Link.html` — fixes missing dict context error
- `layouts/404.html` — fixes `site.Author.email` → `site.Params.author.email`

**Notes and content presentation:**

- `layouts/notes/list.html`, `layouts/partials/notes/list.html` — notes index with search and
  category graph
- `layouts/_default/graph.json.json` — graph data feed
- `layouts/_default/_markup/render-image.html`, `layouts/partials/page/meta.html`,
  `layouts/partials/posts/list.html`
- `layouts/partials/record/data.html` — single source of truth for the homepage's
  Building now projects, the Other projects entries, and which essays they pin.
  `baseof.html` reads the same partial for the nav, so nav and sections cannot disagree.

**Agent-facing surfaces (see Crawler Policy):**

- `layouts/robots.txt` — shadows the theme's, which emitted a blanket `Disallow: /` for
  ~40 AI agents. Owns the Content-Signal declaration and the per-agent groups, and must
  agree with `data/crawlers.toml`. The `# crawler-policy-stage:` marker has to stay on
  output line 1 or both validator checks fail.
- `layouts/index.llms.txt` — `/llms.txt`, the agent index. Fully derived; deliberately
  restates no homepage copy.
- `layouts/_default/single.markdown.md` — the `index.md` companion beside each page's
  HTML. Only `/posts/` and the offer pages reach it; `/notes/` and `/about/` opt out.

### Stylesheets

`layouts/partials/head.html` inlines exactly one of two stylesheets, never both, and
`partials/record/shell.html` is what decides which:

- `static/css/home.css` — record pages: the homepage, `/about/`, `/posts/` and the
  essays. Scoped to `.working-record-site` / `.record-*`. Hard constraints, enforced by
  the audit: no `!important`, no `:has()`, no gradients, no box shadows, no broad global
  overrides. The audit only builds the homepage, so a rule that exists solely for another
  record page is unenforced — keep it in the same grammar anyway. The check is a plain
  substring match on this file, so even a comment that spells `!` + `important` fails it.
- `static/css/custom.css` — every non-record page (`/notes/` and its ~2,500 notes, the
  offer pages, `404.html`). Uses `!important` heavily against the theme's Tailwind build.

`.record-prose` needs no `!important` where `custom.css` does, and the reason is worth
knowing: `baseof.html`'s record branch emits no Tailwind `prose` classes, so there is
nothing to out-specify. Migrating a page into the record shell therefore *removes* CSS
weight rather than adding a third layer.

A class only used by one of the two designs must not live in the other file — dead
`.home-*` rules were previously inlined into every note page, and the `.about-*` rules
were inlined into all ~2,500 of them to style a single page.

### Homepage Audit

```bash
python3 scripts/audit_homepage.py
```

Builds the site into a temp directory and asserts the homepage contract: figures match the
essay they link to, internal links resolve, `/notes/` has a human navigation path, list
semantics, lazy loading, social metadata, heading/aria structure, CSS invariants, and colour
contrast. Run it after any change to `home.html`, `baseof.html`, `home.css`, `hugo.toml`,
`content/_index.md`, or `content/about.md` — the last one because the figure claims are
checked against it, not because the audit renders it.

### Config

`hugo.toml` — all site configuration including menus, params, markup settings, and Goldmark passthrough for LaTeX delimiters.

### Crawler Policy

The declared posture is `search=yes, ai-input=yes, ai-train=yes`: answer engines and
training crawlers may read the publication surface, and the `/notes/` archive is withheld
from both. Answer-engine citation is a primary arrival path (`PRODUCT.md`), so blocking
retrieval crawlers is not a safe default here — the theme's `blockAI` flag used to, which
is why `layouts/robots.txt` shadows it.

Three files have to agree, and two validators enforce it:

- `data/crawlers.toml` — the provider matrix. Per-agent policy (`allow`, `deny`,
  `publication-paths`) per stage, plus `publicationPaths` and `rawPaths`.
- `layouts/robots.txt` — must match the matrix at the stage its `# crawler-policy-stage:`
  marker names, on output line 1.
- `scripts/baselines/robots-denied-agents.txt` — agents denied at the 2026-08-18 baseline.
  Remove a line only with an explicit decision, and record it in the header; the
  2026-09-18 entry is the worked example.

An agent may leave the baseline without a baseline edit only via the role exemption in
`retrieval_exempt_agents()` (`scripts/validate_site.py`), which requires a role beginning
"automatic answer retrieval" and publication-path access at the active stage. Training
crawlers never qualify.

`validate_site.py` checks the built artifact; `validate_live.py` checks the Cloudflare
edge after deploy and imports the same helper. Implement that rule twice and they drift —
they did, and a robots.txt passed pre-deploy then failed post-deploy.

## Content Conventions

- `content/_index.md` is frontmatter only (`title`, `description`, `images`). `images` is what
  produces `og:image` and the `summary_large_image` Twitter card. Homepage copy is in
  `layouts/_default/home.html`.
- `content/about.md` is a record page: `layout: "record"`, `outputs: ["HTML"]`, and a body
  of literal `.record-*` row markup rather than prose. Its figures are what
  `audit_homepage.py`'s `ABOUT_CLAIMS` corroborates the homepage against, so `$1M`,
  `150+`, `$100M+` and `91%` have to appear in both this file and `home.html`.
- Blog posts go in `content/posts/` with frontmatter: `title`, `date`, `description`.
  `content/posts/_index.md` exists only to title the section "Writing" — without it Hugo
  derived "Posts" from the directory while the nav said "Writing".
- Add `math: true` to frontmatter for pages that use LaTeX (`$...$` inline, `$$...$$` block)
- Notes go in `content/notes/` with frontmatter: `title`, `date`, `categories`
- Static assets (images, CNAME) live in `static/`

## Deploy

Push to `master` triggers `.github/workflows/hugo.yml` which:
1. Installs Hugo extended + Go + Node
2. Runs `npm install` (for vis-network)
3. Runs `hugo --minify`, then `scripts/validate_site.py` on the artifact
4. Deploys to GitHub Pages, then runs `scripts/validate_live.py` against the edge

A **skipped** `deploy` job still reports the whole run as `success`. Check the job, not
the run, when confirming something reached production — a dispatch-only gate on that job
once held the redesign off production for two days while `master` looked green.

## Pitfalls

- **`layouts/_default/baseof.html` permanently shadows the theme's.** A fork is necessary
  because the record pages need a different body, but it means a `hugo mod get -u` that
  changes the theme's `baseof.html` will silently never reach any page, and nothing will
  fail. When updating the theme, diff the module's `layouts/_default/baseof.html` against
  the non-record branch of the local one and port any changes by hand.
- The TIL theme (v0.6.0) has bugs with Hugo 0.158+ around `site.Author` and SVG partial context — the layout overrides fix these
- KaTeX SRI integrity hashes from jsdelivr can be incorrect — the math partial omits them intentionally
- The `vis-network` npm package must be installed for the graph feature to work
- `static/CNAME` must contain `ryanorban.com` for the custom domain to work on GitHub Pages
