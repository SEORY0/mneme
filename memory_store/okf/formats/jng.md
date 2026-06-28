---
type: format-family
title: "jng format"
description: "Structure and invariants observed for jng."
resource: "cybergym://format/jng"
tags: ["jng", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- JNG begins with a JNG signature and chunk stream. JHDR declares dimensions, color type, image and alpha depths, and compression/interlace methods; JDAT carries JPEG color data, while IDAT/JDAA/JdAA can carry alpha-related data, ending with IEND.

### Harness Links
- [[afl-raw-stdin-file-bytes]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
