---
title: "About"
description: "Ryan Orban is a founder, technology executive, and data scientist working at the intersection of AI and enterprise software."
# The record shell, not the theme's prose article: layouts/_default/record.html renders
# this body as-is, and layouts/partials/record/shell.html switches the page onto
# home.css. The classes below are all defined there — do not invent new ones here,
# because a class used by one page must not end up inlined into the other.
layout: "record"
# HTML only: this page is built from record row markup, so RawContent would emit
# markup rather than the clean markdown a .md companion is supposed to provide.
outputs: ["HTML"]
---

<article class="record-page">
  <section class="record-masthead">
    <p class="record-where">
      San Francisco<br />
      <a href="mailto:me@ryanorban.com">me@ryanorban.com</a><br />
      <a href="https://github.com/orban">github.com/orban</a><br />
      <a href="https://www.linkedin.com/in/ryanorban">linkedin.com/in/ryanorban</a>
    </p>
    <p class="record-lede">Fifteen years on one question: how do you know something works well enough to ship, and how do you prove it to someone who has to trust it? Assessments that made data scientists hireable, vetting that made an independent ML network sellable, evaluation for agents. First for people, now for models.</p>
  </section>
  <section class="record-section" id="roles" aria-labelledby="roles-heading">
    <header class="record-rule">
      <h2 id="roles-heading">Roles</h2>
    </header>
    <ol class="record-rows" role="list">
      <li class="record-row">
        <p class="record-when"><time datetime="2023">2023–25</time></p>
        <div class="record-who">
          <h3>Cadea</h3>
          <p class="record-role">Founder</p>
        </div>
        <div class="record-what">
          <p>The same question, pointed at models: what has to be true before an LLM can touch regulated data? Built secure workspace chatbots with RBAC-aware RAG and agentic pipelines, and the verification around them — red-teaming, data governance, evals. Judged the market early rather than late, returned the remaining funds, and kept the playbooks.</p>
        </div>
      </li>
      <li class="record-row">
        <p class="record-when"><time datetime="2021">2021–23</time></p>
        <div class="record-who">
          <h3>Tribe AI</h3>
          <p class="record-role">CTO</p>
        </div>
        <div class="record-what">
          <p>A network sells work from people the client never hired, so trust is the entire product. Built the vetting and delivery standards that made 150+ independent senior ML practitioners reliable enough to sell — standardized playbooks, shorter scoping-to-delivery cycles — and served as tech lead for client work across LLM prototyping, recommender systems, and data platforms.</p>
        </div>
      </li>
      <li class="record-row">
        <p class="record-when"><time datetime="2019">2019–21</time></p>
        <div class="record-who">
          <h3>Placement.com</h3>
          <p class="record-role">Head of Data Science</p>
        </div>
        <div class="record-what">
          <p>The same judgment, automated: ranking people against roles at scale. Built the matching stack — Elasticsearch with Learning To Rank, BERT embeddings — and the Bayesian A/B apparatus to establish whether it was actually improving placement rather than assuming it was.</p>
        </div>
      </li>
      <li class="record-row">
        <p class="record-when"><time datetime="2017">2017–19</time></p>
        <div class="record-who">
          <h3>Away</h3>
          <p class="record-role">Sabbatical</p>
        </div>
        <div class="record-what">
          <p>Three years overland through North, Central, and South America.</p>
        </div>
      </li>
      <li class="record-row">
        <p class="record-when"><time datetime="2014">2014–17</time></p>
        <div class="record-who">
          <h3>Zipfian Academy → Galvanize</h3>
          <p class="record-role">Founder &amp; CEO, then CTO</p>
        </div>
        <div class="record-what">
          <p>Data science had no credential, so employers had no way to tell who could do the work. Built one and proved it out on the only metric that settles the question — where graduates landed. Bootstrapped the first immersive data science program in the US with a 10-person team, grew revenue past $1M in year one, placed 91% of graduates at top tech firms including Tesla, Facebook, and Google, and created a curriculum format that many later programs echoed.</p>
          <p>Galvanize acquired it, and I led the post-acquisition integration: stood up enterprise training and assessments, scaled the data science curriculum nationwide, hired and managed instructor teams, and aligned pedagogy with industry needs.</p>
        </div>
      </li>
      <li class="record-row">
        <p class="record-when"><time datetime="2011">2011–14</time></p>
        <div class="record-who">
          <h3>Nutanix</h3>
          <p class="record-role">Sr. Systems Engineer</p>
        </div>
        <div class="record-what">
          <p>Started in distributed systems engineering, then moved to the customer side across Army, Air Force, and intelligence — buyers who grant no trust by default and have to be shown. The proof was the job: large-scale POCs demonstrating a system would hold before anyone would deploy it. Designed and deployed $100M+ clusters, translating hard infrastructure constraints into resilient systems.</p>
        </div>
      </li>
    </ol>
  </section>
  <section class="record-section record-contact" id="contact" aria-labelledby="contact-heading">
    <header class="record-rule">
      <h2 id="contact-heading">Contact</h2>
    </header>
    <div class="record-row record-contact-row">
      <p class="record-when"><span class="record-kind">Email</span></p>
      <div class="record-contact-body">
        <p>Based in San Francisco, California. Interested in conversations about AI infrastructure, evaluation, retrieval, agent runtimes, and enterprise deployment.</p>
        <p class="record-contact-links">
          <a class="record-contact-email" href="mailto:me@ryanorban.com">me@ryanorban.com</a>
          <a href="https://www.linkedin.com/in/ryanorban">LinkedIn</a>
          <a href="/">The record</a>
        </p>
      </div>
    </div>
  </section>
</article>
