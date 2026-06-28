---
type: format-family
title: rawspeed-camera-file-or-jpeg-container format
description: Structure and reachability facts for rawspeed-camera-file-or-jpeg-container inputs.
tags: [rawspeed-camera-file-or-jpeg-container]
okf_support: 0
---
# Rawspeed Camera File Or Jpeg Container Format

## Round 10 Factual Contract

### Schema / Invariants
- The target bug is in lossless JPEG SOF parsing where component count must be consistent with row geometry before later row access. Reaching it likely requires a recognizable camera container that selects an LJPEG decoder and carries coherent image dimensions, strip data, and component metadata.

### Harness Links
- [[afl-libfuzzer-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
