# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static personal portfolio website for Ryan Orban, hosted on GitHub Pages at ryanorban.com.

## Tech Stack

- Pure HTML5 and CSS3 (no JavaScript frameworks)
- External dependencies loaded via CDN: smooth-scroll, Google Fonts (IBM Plex Sans, Nunito, Permanent Marker, Source Serif Pro), there.today location tracking
- Schema.org microdata for SEO

## Development Workflow

**No build process required.** Edit HTML/CSS files directly.

To test locally, open `index.html` in a browser.

To deploy, commit and push to master - GitHub Pages deploys automatically.

## Site Structure

- `index.html` - Main homepage with professional summary and background
- `style.css` - Global styles with responsive breakpoints at 500px, 700px, and 768px
- `advising/index.html` - Advisory services page
- `office-hours/index.html` - Calendly booking integration
- `images/` - Static assets (headshots, logos)
- `CNAME` - GitHub Pages custom domain configuration

## Styling Conventions

- Mobile-first responsive design using CSS Grid and Flexbox
- Color scheme: light background (#fdfdfd), accent red (#e74646), newsletter highlight (#ffeedb), grays (#555, #666, #777)
- Typography: IBM Plex Sans for body, Permanent Marker for decorative headings
- Monospace elements use system font stack
