---
name: Ryan Orban — Homepage
description: A portrait-led record page that proves stochastic-AI-evaluation expertise with one seeded, labelled 100-run trial figure beside the portrait.
colors:
  paper-ground: "#f3efe6"
  paper-figure: "#faf8f2"
  ink: "#1f241f"
  ink-mid: "#4d554c"
  ink-muted: "#5f675e"
  accent-green: "#3b7350"
  accent-green-dark: "#2c5a3d"
  accent-green-soft: "#7ea87a"
  line: "#d9d5c8"
  line-dark: "#b9b5a6"
typography:
  display:
    fontFamily: "Instrument Serif, Georgia, serif"
    fontSize: "clamp(3.6rem, 6.6vw, 6rem)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "-0.035em"
  lede:
    fontFamily: "Instrument Serif, Georgia, serif"
    fontSize: "clamp(1.45rem, 2.2vw, 1.85rem)"
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: "normal"
  headline:
    fontFamily: "Instrument Serif, Georgia, serif"
    fontSize: "clamp(2.5rem, 5vw, 4.35rem)"
    fontWeight: 400
    lineHeight: 0.98
    letterSpacing: "-0.025em"
  title:
    fontFamily: "Instrument Serif, Georgia, serif"
    fontSize: "clamp(2.3rem, 4vw, 3.4rem)"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "normal"
  subhead:
    fontFamily: "Geist Sans, Geist, system-ui, -apple-system, sans-serif"
    fontSize: "1.15rem"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  body:
    fontFamily: "Geist Sans, Geist, system-ui, -apple-system, sans-serif"
    fontSize: "0.96rem"
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: "normal"
  label:
    fontFamily: "JetBrains Mono, ui-monospace, monospace"
    fontSize: "0.67rem"
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: "0.075em"
rounded:
  none: "0"
spacing:
  container-max: "1180px"
  container-inset: "3rem"
  container-inset-mobile: "1.5rem"
  section-y: "clamp(3.5rem, 7vw, 6rem)"
  rail-label: "9rem"
  rail-label-dense: "6.5rem"
components:
  contact-email:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0.55rem 0.85rem"
  contact-email-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.paper-ground}"
  nav-link:
    textColor: "{colors.ink-mid}"
    typography: "{typography.label}"
  nav-link-hover:
    textColor: "{colors.accent-green-dark}"
---

# Design System: Ryan Orban — Homepage

## Overview

**Creative North Star: "The Cleared Bar"**

This is a portrait-led record page for a technical executive deciding, in seconds, whether to hand someone ownership of a consequential system. The direction is confirmed as the category standard played straight: the craft level of brycesandlund.com, harshakaranth.com, coopershea.com, and madhuribhavana.com, with no smuggled quirk. What earns it that standing isn't the type system alone — a warm paper ground, one muted green accent, a serif/sans/mono three-family split — but the single device that carries the product's actual claim: a seeded, labelled 100-run trial figure sitting beside the portrait in the first viewport, showing that one pass and a hundred passes are different kinds of evidence. Everything else in the system is restraint in service of that one figure reading clearly.

The system is flat and rectilinear by rule: zero shadows, zero gradients, zero border-radius, enforced by `scripts/audit_homepage.py`. Depth comes only from a two-weight hairline vocabulary and a paper/ground contrast, never from elevation effects. Motion is likewise rationed to exactly one authored moment — the trial cells drawing in on load — rather than distributed across hovers and transitions as decoration.

**Key Characteristics:**
- Warm paper ground with a single muted green accent; no second hue anywhere, including in the trial figure's fail state.
- Three type families, three fixed roles: serif asserts, sans explains, mono measures and labels.
- One recurring layout idea — a fixed-width mono rail label beside flexible content — reused across section headers, record rows, the writing list, metrics, and contact.
- Flat, hairline-bordered, square-cornered; depth by paper contrast, never by shadow.
- One authored motion (the trial cells drawing in); every other transition is a plain, fast state change.

## Colors

A warm paper ground and near-black ink carry the page; one muted green accent marks record and proof, never decoration.

### Primary
- **Cleared Green** (`#3b7350`): the timeline's accent ticks, record-row label spans, and the sole accent color in the system — used sparingly, as a marker rather than a fill.
- **Cleared Green Dark** (`#2c5a3d`): the hover/focus state for every accent-carrying element and link.

### Neutral
- **Paper Ground** (`#f3efe6`): the page background.
- **Paper Figure** (`#faf8f2`): the surface for the one framed, elevated element (the trial figure card) — barely lighter than the ground, not a shadow.
- **Ink** (`#1f241f`): headings, primary text, and the border/fill color for the bordered email tag.
- **Ink Mid** (`#4d554c`): body copy color throughout.
- **Ink Muted** (`#5f675e`): mono labels, captions, timestamps, footer text.
- **Line** (`#d9d5c8`): the lighter of the two hairline weights — internal and soft dividers.
- **Line Dark** (`#b9b5a6`): the heavier hairline weight — structural borders (portrait frame, trial-figure frame, header underline, rows' opening rule).
- **Selection Green** (`#7ea87a`): text-selection background only; not used as a UI color.

### Named Rules
**The One Hue Rule.** Exactly one accent hue exists, and it never gains a sibling. The trial figure's fail cells are ink-filled, not a second color — a system that needs two hues to say pass/fail hasn't earned the accent yet.

**The Two-Weight Hairline Rule.** Every rule on the page is 1px solid, in one of exactly two colors: `line` for soft/internal dividers, `line-dark` for structural ones. No third weight, no shadows standing in for a third.

## Typography

**Display Font:** Instrument Serif (with Georgia, serif fallback)
**Body Font:** Geist Sans (variable weight, with system-ui fallback)
**Label/Mono Font:** JetBrains Mono (with ui-monospace fallback)

**Character:** the serif carries every claim the page makes — the name, the lede, section headlines, project names — set large and tight-leaded; the sans stays quiet in the body; the mono is reserved entirely for things that measure (labels, timestamps, metrics keys, nav).

### Hierarchy
- **Display** (400, `clamp(3.6rem, 6.6vw, 6rem)`, line-height 0.9, letter-spacing −0.035em): the `<h1>` name, once per page.
- **Lede** (400 serif, `clamp(1.45rem, 2.2vw, 1.85rem)`, line-height 1.18, color ink-mid, max-width 24rem): the single-sentence claim beside the portrait.
- **Headline** (400 serif, `clamp(2.5rem, 5vw, 4.35rem)`, line-height 0.98, letter-spacing −0.025em, max-width 20ch): the record/work/writing/contact section headings.
- **Title** (400 serif, `clamp(2.3rem, 4vw, 3.4rem)`, line-height 1): project names (Moirai, Cerberus).
- **Subhead** (600 sans, 1.15rem / 1.05rem, letter-spacing −0.02em): record-row and writing-list `<h3>`s — the only sans-serif heading weight in the system.
- **Body** (400 sans, 0.88–0.98rem, line-height 1.55–1.7, color ink-mid, capped 40–49rem measure): paragraph copy throughout.
- **Label** (500 mono, 0.62–0.72rem, letter-spacing 0.04–0.075em, uppercase, color ink-muted): rail labels, nav, timestamps, metrics keys, footer.

### Named Rules
**The Three-Family Rule.** Exactly three families, exactly one role each: serif for anything that asserts (names, headlines, the lede), sans for anything that explains (body, sub-heads), mono for anything that labels or measures (rail labels, timestamps, metrics, nav). Never let a family cross into another's role.

## Layout

The page is a single centered column, `min(100% - 3rem, 1180px)` (`min(100% - 1.5rem, 1180px)` under 680px). The hero is a three-column grid — portrait (~0.82fr), name and lede (1fr), trial figure (~0.92fr) — that collapses to two columns under 1000px (the trial figure spans both, and its cell grid widens from 10 to 20 columns to stay legible at the wider single row) and further reflows under 680px, where the portrait shares a row with the name and the lede and trial figure drop to full width below.

Each section uses the same rhythm: `clamp(3.5rem, 7vw, 6rem)` top padding, `clamp(2.5rem, 5vw, 4rem)` bottom, closed with a light hairline `border-bottom`, and `scroll-margin-top: 1.5rem` so anchor-nav targets (`#record #work #writing #contact`) don't land under nothing. Two-column content grids (record rows, project cards) collapse to one column under 1000px; the record's final "Now" row always spans the full width, so the record closes on the present regardless of column count.

### Named Rules
**The Rail-Label Rule.** One layout idea repeats everywhere: a fixed-width mono label column beside a flexible content column — 9rem in section headers, the writing list, metrics, and the contact block; 6.5rem in record rows; 7.5rem in the trial figure's read-out. Any new record-style listing reuses this grid rather than inventing a new one.

## Elevation & Depth

Flat, by rule and by audit: `scripts/audit_homepage.py` greps the stylesheet for `box-shadow` and `gradient(` and fails the build if either appears. Depth is conveyed only two ways — the two-weight hairline border vocabulary, and the near-imperceptible shift from `paper-ground` to the slightly lighter `paper-figure` for the one framed surface on the page (the trial figure card).

### Named Rules
**The No-Shadow Rule.** No `box-shadow` anywhere; the audit enforces it. A surface reads as "elevated" only by moving to `paper-figure` inside a hairline frame, never by shadow.

## Shapes

Every corner is square; `border-radius` is not set anywhere in the stylesheet. Borders are always 1px solid hairlines, in `line` or `line-dark` only. The portrait and its footer-rail thumbnail carry the system's only image treatment: a 1px `line-dark` border, `object-fit: cover`, and a slight desaturation (`saturate(0.72) contrast(1.02)`) rather than a full-color, full-bleed crop.

### Named Rules
**The Zero-Radius Rule.** `border-radius` is never set; every frame, tag, and card is a hard rectangle.

## Components

### Trial Figure (signature component)
A bordered `paper-figure` card holding, in order: a head line (run count + bar percentage), a grid of cells standing for each seeded run, a `<dl>` read-out (naive single-run reading, the full-sample reading, and the verdict against the bar), and a caption with the real pass/fail count and a link. Pass cells render as an outlined, unfilled `paper-figure` cell (border `line-dark`); fail cells render solid `ink` — the one-hue restraint applied inside the figure itself, not just across the palette. Cells draw in over 240ms (`cubic-bezier(0.16, 1, 0.3, 1)`), staggered 9ms apart left to right — the page's one authored motion, replaced by an instant final state under `prefers-reduced-motion`.

### Timeline Strip (signature component)
A wrapping flex row of career entries, each carrying its own 2px `accent-green` top-border "tick" pulled up 1px into the strip's bounding hairlines. The trailing entry is a plain link (no tick), pushed to the far edge on wide layouts and to its own full-width row on phones.

### Ruled Facts List
`<dl>` read-outs (the trial figure's verdict rows, each project's metrics) share the rail-label grid, a hairline top border, and baseline-aligned rows; numeric values use tabular figures.

### Bordered Email Tag
The contact email is a mono, hard-cornered rectangle with a 1px `ink` border. On hover/focus it inverts to filled `ink` background and `paper-ground` text over 160ms ease-out — the only fill-inverting interactive element in the system.

### Navigation
Mono, uppercase, `ink-mid` by default, `accent-green-dark` on hover, no underline; wraps onto its own rows under 680px. A sitewide `2px accent-green-dark` focus-visible outline (3px offset) covers nav and every other interactive element.

## Do's and Don'ts

### Do:
- **Do** keep exactly one accent hue (green); express any other state — failure, muted, disabled — through the ink/paper/line neutrals, never a second color.
- **Do** reuse the rail-label grid (9rem label / flexible content, 6.5rem dense variant) for any new record-style listing; it's the system's one recurring layout idea.
- **Do** reserve Instrument Serif for anything that asserts and JetBrains Mono for anything that labels or measures; never run body prose in mono or a headline in sans.
- **Do** keep hairlines to exactly two weights (`line`, `line-dark`) and reuse them structurally rather than adding a third.
- **Do** move a rail label or mono byline to *after* its heading on narrow viewports, never before it — the confirmed phone-width reflow order for section headers, record rows, and the writing list.
- **Do** self-host every font; PRODUCT.md commits the homepage to zero third-party font requests.

### Don't:
- **Don't** add a `box-shadow`, `gradient`, or `border-radius`; the audit script rejects all three.
- **Don't** treat the trial figure's exact seed, run count, or pass/fail split as a system value — the template computes it live at build time; a future surface earns its own seed rather than copying this one's numbers.
- **Don't** invent a second accent color to express a state the ink/paper neutrals can already carry — see the trial figure's ink-filled fail cells.
- **Don't** carry a homepage-only device onto interior pages without re-running this pass. About, Writing, and Bookmarks still run on `static/css/custom.css` and are explicitly out of scope for this system; extend it deliberately rather than assuming it already applies.
