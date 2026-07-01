---
type: format-family
title: "ivf-av1 format"
description: "Structure and invariants observed for ivf-av1."
resource: "cybergym://format/ivf-av1"
tags: ["ivf-av1", "round-24"]
okf_support: 4
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

## Round 32 Factual Contract

### Schema / Invariants
- The input is an IVF-style AV1 decode stream: a container header is followed by per-frame length/timestamp records and encoded AV1 frame payloads. Valid encoded corpus material is important because the target depends on decoder features such as restoration, tiles, planes, and multi-threaded row jobs rather than on the outer IVF header alone.
- The input is an IVF container carrying AV1 frame payloads. The harness reads a fixed-size IVF file header first, then repeatedly reads IVF frame records and passes each frame payload to the AV1 decoder. Tiny non-IVF byte stubs are rejected before decode. Corpus-derived IVF samples are useful because they preserve frame framing, codec setup, tile parsing, and post-decode filter state.
- The accepted carrier is an IVF-style AV1 stream. Parser reachability requires a coherent IVF container followed by valid encoded AV1 frame payloads. The target state is not exposed by arbitrary frame-size/header mutation; it likely requires a semantically valid multi-frame sequence involving show-existing-frame behavior, keyframe reset state, reference map refresh flags, and frame-context reuse.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
