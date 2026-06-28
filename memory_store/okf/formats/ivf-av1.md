---
type: format-family
title: "ivf-av1 format"
description: "Structure and invariants observed for ivf-av1."
resource: "cybergym://format/ivf-av1"
tags: ["ivf-av1", "round-24"]
okf_support: 1
---
# Schema

## Round 24 Factual Contract

### Schema / Invariants
- The harness consumes an IVF-style AV1 byte stream: a file header is followed by per-frame length/timestamp records and encoded AV1 frame data. Valid corpus material is far more useful than a synthetic header because the crash depends on codec features such as restoration, tiles, and plane state.

### Harness Links
- [[afl-libfuzzer-compatible-raw-stdin]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
