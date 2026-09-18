---
title: "Bookmarks"
description: "A public archive of saved links with automatically generated source summaries."
# 2,520 notes, each an automatically generated summary of someone else's writing. They
# get HTML only: markdown companions here would add 2,520 files to the artifact for an
# archive that data/crawlers.toml already withholds from crawlers as rawPaths.
#
# _target scopes this to kind: page. Without it the cascade also applies to this section
# page and strips /notes/index.xml and /notes/index.json, which validate_site.py reports
# as a regression against the baseline.
cascade:
  - _target:
      kind: page
    outputs: ["HTML"]
---
