# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: CEOs, CTOs, heads of engineering, and research/product leaders deciding whether to give Ryan end-to-end ownership of a consequential technical system — especially a production-AI system whose behavior is hard to measure, control, or improve. They arrive from a referral, a search, or an answer-engine citation, usually on a laptop during a working day, and decide within seconds whether to read on.

Secondary: founders and senior collaborators with a hard deployment, evaluation, reliability, security, or organizational-learning problem that could become substantial operating responsibility.

Not the audience for homepage decisions: investors, general readers, casual consulting prospects.

(Source: handoff master plan `HOMEPAGE_REWRITE_CODEX.md`, 2026-08-18.)

## Product Purpose

ryanorban.com is Ryan Orban's personal site: a Hugo site (TIL theme, GitHub Pages behind Cloudflare) with a homepage, About, Writing (`/posts/`), and a public Bookmarks intake archive (`/notes/`, ~1,000 automatically generated source summaries). Success is qualified conversations about roles with end-to-end ownership of consequential technical systems, then correct association between Ryan and his actual expertise, then discovery and citation of original evidence-bearing work.

## Positioning

Visitor decision (confirmed 2026-09-04): a CEO/CTO/head of engineering deciding whether to hand Ryan end-to-end ownership of a consequential AI system. The page must read senior and specific at once.
Concrete claim: a technical capability becomes a system only when it can be measured, controlled, and improved; Ryan builds those layers for production AI (stochastic-agent evaluation and regression testing, statistical release decisions, trajectory/failure analysis, secure authorization-aware retrieval, replay/observability/feedback loops) and has solved analogous problems at Nutanix, Zipfian Academy/Galvanize, Tribe AI, and Cadea. Proof-Carrying Changes is a mechanism under test, not a validated product claim; it must not be featured until a public specification and worked example exist.

## Operating Context

The homepage is a curated decision surface, not a feed. Two content layers: publications (Ryan-authored or substantively annotated, `/posts/`) and intake (bookmarks with AI-generated summaries, `/notes/`, visibly labeled as not Ryan's writing). Crawler and index policy is version-controlled (`data/crawlers.toml`, content-state helper) and must not be undone by visual work.

## Capabilities and Constraints

- Hugo 0.158.0 (CI-pinned), theme `hugo-theme-til` v0.6.0 with Tailwind prose classes; site CSS lives in `static/css/custom.css` (inlined into every page). Existing overrides in `layouts/` own head/metadata, home, notes/posts single+list, header/menu/footer.
- Exactly one semantic `<h1>`; `#work` and `#contact` anchors; no service menu; no placeholders. Homepage copy is not pinned to the 2026-08-18 plan wording (Ryan judged it ostentatious on 2026-08-19; show, don't tell).
- Build validator (`scripts/validate_site.py`, arriving via PR #8) must keep passing; the mobile hero must not consume the entire first phone viewport.
- No fabricated metrics, clients, dates, or claims. No client-confidential material.
- Existing analytics: Plausible tagged events (`discuss_role`, `contact_email`, `view_work`, `view_writing`, `view_about`, `view_bookmarks`, `open_artifact`).
- Static HTML embeds (`/embeds/*.html`) are iframed charts inside posts.

## Brand Commitments

- Visual world: replaced 2026-09-04. Two prior worlds are anti-references, not authority: the
  dithered Departure Mono "instrument-paper" build (handoff branch, judged overboard) and the
  cream / Instrument Serif / Geist "Working Record" build (judged bland, the category default).
  The new world is chosen through impeccable's direction round on this branch and recorded in
  DESIGN.md at finish.
- Direction chosen 2026-09-04 through impeccable's direction round: the category standard, played straight. A portrait-led personal site at the craft level of brycesandlund.com, harshakaranth.com, coopershea.com, and madhuribhavana.com; conventions embraced, no smuggled quirk. Standing preference.
- Confirmed 2026-09-04: the page is person-led. The portrait (`static/images/ryan-orban.jpg`)
  and a seeded, labelled synthetic figure may lead; re-rendered project charts and personal
  photography (Enunciation, travel) do not lead this pass.
- Scope 2026-09-04: homepage first; header, footer, About, Writing, Bookmarks follow in a
  second pass once the homepage is approved.
- Fonts are self-hosted in `static/fonts/`; no third-party font requests.
- Design tooling: impeccable skill (`.github/skills/impeccable`, gitignored, installed per machine).
- Voice: direct, precise, concrete; show rather than tell; no "visionary/thought leader/leveraging AI";
  confidence without self-congratulation.

## Evidence on Hand

- Two published articles: *Stop Testing AI Agents Like Deterministic Code* (2026-03-26) and *What Stochastic Variation Reveals About AI Agents* (2026-04-04), both with inline SVG/embedded charts. Two further posts are drafts.
- About page chronology (Cadea, Tribe AI, Galvanize, Zipfian Academy, Nutanix). Portrait at `static/images/ryan-orban.jpg`; project figures under `static/images/work/`.
- No case studies, testimonials, or metrics available for publication yet — do not invent them.

## Product Principles

1. Lead with the current program and its evidence, then career proof; never a résumé first.
2. Fewer, stronger, first-party pages; intake stays visibly intake.
3. Every visual device must serve legibility for a time-poor technical executive.
4. Instrument the site's own mechanism (repeated trials, variance, release evidence) rather than decorate around it.
5. Preserve URLs, metadata policy, and validators through any redesign.

## Accessibility & Inclusion

Body text ≥4.5:1 contrast; keyboard-visible focus; ASCII/box-drawing figures carry text alternatives; motion respects `prefers-reduced-motion`.
