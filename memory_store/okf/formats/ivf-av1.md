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

## Round 25 Factual Contract

### Schema / Invariants
- The target expects an IVF-style AV1 decode stream: a container header is read first, then frame records are iterated and each frame payload is passed to the AV1 decoder. Historical decoder seeds in the corpus are useful for reaching the parser, but they do not necessarily enable loop filtering or the target frame geometry.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
