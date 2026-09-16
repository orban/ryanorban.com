---
title: SLEEP — Open Data Protocols
date: 2013-07-02
categories:
  - open-data
  - protocols
  - data-formats
  - dat
  - binary-storage
description: SLEEP (Seekable Lightweight Error-free Efficient Protocol) is an open binary data storage format with built-in indexing for random access and integrity verification. Created as part of the dat project ecosystem for distributing open datasets efficiently.
params:
  source: pinboard
  sourceUrl: http://www.dataprotocols.org/en/latest/sleep.html
---

## Summary

SLEEP (Seekable Lightweight Error-free Efficient Protocol) is a binary data storage format specification from the Open Data Protocols project. It was designed as part of the dat ecosystem — Max Ogden's effort to create a Git-like distributed version control system for datasets. SLEEP defines how to store tabular data with built-in indexing so that consumers can seek to specific rows without reading the entire file, and verify integrity via a Merkle tree structure.

The core idea: most open data formats (CSV, JSON Lines) don't support efficient random access or integrity proofs without loading the full file. SLEEP addresses this by prepending a header and B-tree index that enables O(log n) seeks to any row, plus a hash tree that allows partial file verification — you can download and verify a subset of rows without trusting the server or downloading everything.

This was an early component in the dat project's vision of a dataset distribution protocol analogous to BitTorrent but append-only and version-controlled. The format itself didn't gain broad adoption — later, the ecosystem evolved toward Hypercore Protocol — but the design ideas (seekable indexes, Merkle integrity proofs for tabular data) influenced subsequent decentralized data infrastructure work.

## Key points

- Seekable binary format: O(log n) random access to rows via embedded B-tree index — enables streaming partial datasets from remote servers.
- Merkle tree integrity: hash proofs for subsets of rows — you can verify a downloaded slice without trusting the source.
- Part of the dat protocol ecosystem: Max Ogden's Git-for-data project, later evolved into Hypercore Protocol.
- Contrasts with CSV/JSON Lines: those formats require full-file reads for any aggregation; SLEEP enables true random access and distributed verification.

[Original](http://www.dataprotocols.org/en/latest/sleep.html)
