---
title: "pygwalker: Pandas DataFrame to Tableau-Style UI"
date: 2023-02-20
categories:
  - data-visualization
  - pandas
  - jupyter
  - python
  - eda
description: pygwalker turns a pandas DataFrame into a drag-and-drop Tableau-style visual analysis interface inside Jupyter notebooks — one line of code to replace writing matplotlib/seaborn boilerplate with interactive visual exploration. Strong tool for exploratory data analysis.
params:
  source: pinboard
  sourceUrl: https://github.com/Kanaries/pygwalker
---

![pygwalker: Pandas DataFrame to Tableau-Style UI](/images/notes/pygwalker-pandas-visual-analysis.png)

## Summary

pygwalker (by Kanaries) converts a pandas DataFrame into an interactive Tableau-style visual analysis interface inside Jupyter notebooks with a single function call. Instead of writing matplotlib or seaborn code to explore a dataset, you get a drag-and-drop chart builder: drag columns to X/Y axes, color encoding, facets, and filters, and the charts update in real time.

The core use case is exploratory data analysis (EDA) — the early phase of a data project where you're trying to understand the shape, distributions, and relationships in a dataset. Traditionally this involves iterating through many `df.plot()` calls or writing visualization code. pygwalker replaces that loop with a GUI that a data analyst or non-programmer can use directly without Python knowledge.

The key design choice is running entirely inside Jupyter — no separate application to launch, no export step. The DataFrame from your Python environment becomes the data source for the GUI, which means it works with any DataFrame that already exists in memory after your data loading and cleaning code. This makes it composable with existing pandas-based workflows rather than requiring a full transition to a BI tool.

## Key points

- One function call (`walk(df)`) → interactive Tableau-style chart builder in Jupyter.
- Drag columns to visual encodings: X/Y axes, color, size, facets, filters — no chart code required.
- Runs in-notebook — no separate application, no export; uses the DataFrame already in memory.
- By Kanaries — the same team behind RATH, a standalone AI-assisted data analysis tool.
- Replaces iterative matplotlib/seaborn EDA code with a GUI for faster dataset exploration.

[Original](https://github.com/Kanaries/pygwalker) → GitHub
