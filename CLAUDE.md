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
├── posts/                 # Essays (full articles)
│   ├── _index.md          # Section title only ("Writing")
│   └── stop-testing-agents-like-deterministic-code.md
└── notes/                 # TIL-style short notes
    └── _index.md
```

### Layout Overrides

Everything in `layouts/` shadows the theme module. There are twenty-eight files. The site
has one design — the "Working Record" — and one stylesheet; every page renders through
`baseof.html`'s single body. The theme supplies data plumbing, the Tailwind build behind
its own markup, and nothing else visual.

**The shell:**

- `layouts/_default/baseof.html` — the only body. Emits the `working-record-site` body,
  skip link, record header/nav and record footer for every page. Nav anchors are in-page
  on the homepage and root-relative elsewhere; the "where you are" item takes its label
  from the URL segment, never `.Title`, and deep pages resolve up to their section.
- `layouts/partials/record/shell.html` — returns `.ownsTitle`: the page body supplies its
  own `<h1>`, so the running head must not be one. False only for the homepage and
  `/about/`, whose subject is the person. Nothing in the build catches two `<h1>`s off
  the homepage, so this is the guard.
- `layouts/partials/head.html` — fixes deprecated `site.Author` → `site.Params.author.name`;
  owns the font preloads and inlines `home.css`.

**Page templates:**

- `layouts/_default/home.html` — the entire homepage. All homepage copy lives here, not in
  `content/_index.md`, which is frontmatter only.
- `layouts/_default/record.html` — the template `layout: "record"` selects. Thin on
  purpose: emits `.Content` and nothing else, so the page authors its own rows. `/about/`
  is the only page using it.
- `layouts/_default/single.html` — root pages that are not `/about/`. Title and
  `.record-prose`, no date. **No page reaches it today**: `/advising/` and
  `/office-hours/` were the only two and were retired on 2026-09-20. It stays as a guard —
  without it the theme's `_default/single.html` takes over for the next root page added
  and brings a second `<h1>` with it.
- `layouts/posts/single.html` — an essay. Title, date on the spine, `.record-prose`.
- `layouts/posts/list.html` — `/posts/`. **Keep the `.Paginate` call**: it is what makes
  Hugo emit the `/posts/page/1/` alias, and that URL is in the pre-migration baseline, so
  a plain `range` fails `validate_site.py`.
- `layouts/notes/single.html` — a bookmark. Leads with `params.sourceUrl`, because the
  summary is generated and the original is what the reader wants.
- `layouts/notes/list.html`, `layouts/partials/notes/list.html` — the bookmark index, its
  filter chips and its search script.
- `layouts/_default/taxonomy.html` — **both** taxonomy kinds, dispatching to
  `partials/record/term.html` and `partials/record/terms.html` on `.Kind`. Hugo 0.166
  ignores a `term.html` in `_default/` or `layouts/` and only honours
  `layouts/<plural>/term.html`; CI pins 0.158, so the dispatch avoids depending on a
  lookup that differs between the two Hugos that build this site.
- `layouts/_default/graph.html`, `layouts/404.html`.

**Shared partials:**

- `layouts/partials/record/data.html` — single source of truth for the homepage's
  Building now projects, the Other projects entries, and which essays they pin.
  `baseof.html` reads the same partial for the nav, so nav and sections cannot disagree.
- `layouts/partials/page/meta.html`, `layouts/partials/page/list.html` — subjects, tags,
  backlinks and the graph, under a note or an essay.
- `layouts/partials/pagination.html` — renders nowhere today; `/posts/` has one page.
- `layouts/_default/graph.json.json` — the graph data feed.
- `layouts/partials/head/math.html` — adds `$...$` inline math, removes broken SRI hashes.
- `layouts/partials/svg/Link.html` — fixes a missing dict context error in the theme.
- `layouts/_default/_markup/render-image.html`, `layouts/partials/posts/list.html`.

**Agent-facing surfaces (see Crawler Policy):**

- `layouts/robots.txt` — shadows the theme's, which emitted a blanket `Disallow: /` for
  ~40 AI agents. Owns the Content-Signal declaration and the per-agent groups, and must
  agree with `data/crawlers.toml`. The `# crawler-policy-stage:` marker has to stay on
  output line 1 or both validator checks fail.
- `layouts/index.llms.txt` — `/llms.txt`, the agent index. Fully derived; deliberately
  restates no homepage copy.
- `layouts/_default/single.markdown.md` — the `index.md` companion beside each page's
  HTML. Only `/posts/` reaches it; `/notes/` and `/about/` opt out.

### Stylesheets

`static/css/home.css` is the only stylesheet, inlined by `head.html` on every page. Scoped
to `.working-record-site` / `.record-*`. Hard constraints, enforced by the audit: no
`!important`, no `:has()`, no gradients, no box shadows, no broad global overrides.

It needs no specificity overrides because `baseof.html` emits no Tailwind `prose` classes
— there is nothing to out-specify. The deleted `custom.css` leaned on `!important`
constantly for exactly that reason, and it was 1,014 lines inlined into all ~2,500 note
pages. The override war was a property of the theme shell, not the content.

The theme's Tailwind build is still loaded site-wide by `head/css`, because the theme's
own markup — code blocks, the graph widget, heading anchors — carries utility classes.
Do not restyle those from `home.css`; they work as they are.

The audit only builds the homepage, so a rule that exists solely for another page is
unenforced. Keep it in the same grammar anyway. The `!important` check is a plain
substring match on the file, so even a comment that spells it out fails the audit.

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

### Retiring a page

Deleting a `content/` file is not enough for anything in
`scripts/baselines/public-urls.txt`. Three checks fire on it, and they only agree if the
URL keeps serving something: `check_url_manifest` wants an output file,
`check_sitemap` fails any sitemap entry that is a meta refresh, and the baseline
comparison fails any sitemap URL that vanished.

So retire by redirect, not by deletion:

1. Delete the content file.
2. Add the old path to `aliases` on the page that replaces it (`/advising/` and
   `/office-hours/` alias to `content/_index.md`). Hugo writes a meta-refresh stub, which
   keeps the output file and stays out of the sitemap.
3. Add `<source> <target>` to `scripts/baselines/approved-aliases.txt` with the decision
   in a comment. That file is the **only** register of a deliberate departure from the
   baselines — `check_sitemap` reads it to allow the URL out of the sitemap, and it
   re-verifies that the build really serves a redirect there, so a typo'd line exempts
   nothing.
4. If `validate_live.py` names the path explicitly, change the assertion to expect the
   redirect. Don't delete it: a silent 404 on an indexed URL is what it's there to catch.

Do **not** edit `sitemap-urls-2026-08-18.txt` to make a check pass. It's a dated snapshot
of what the site served that day; rewriting it to accommodate a later decision destroys
the record it exists to be.

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

- **`layouts/_default/baseof.html` permanently shadows the theme's, and no longer has a
  branch that resembles it.** A `hugo mod get -u` that changes the theme's shell — its
  body, header, footer or the Tailwind classes on them — reaches no page here and nothing
  fails. That is now intentional rather than a hazard to reconcile: the site does not use
  the theme's design. What a theme update *can* still change under you is the markup the
  theme generates inside the page — code blocks, heading anchors, the graph widget — so
  check those render after one.
- **Hugo's documented template lookup for term pages does not hold on 0.166.** A
  `term.html` in `layouts/_default/` or `layouts/` is silently ignored; only
  `layouts/<plural>/term.html` is picked up. `_default/taxonomy.html` dispatches on
  `.Kind` instead, because CI pins 0.158 and the two must not diverge.
- The TIL theme (v0.6.0) has bugs with Hugo 0.158+ around `site.Author` and SVG partial context — the layout overrides fix these
- KaTeX SRI integrity hashes from jsdelivr can be incorrect — the math partial omits them intentionally
- The `vis-network` npm package must be installed for the graph feature to work
- `static/CNAME` must contain `ryanorban.com` for the custom domain to work on GitHub Pages
