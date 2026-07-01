---
type: harness-contract
title: "Libfuzzer Http2 Socket"
description: "Round 36 factual harness contract for libfuzzer-http2-socket."
tags: ["libfuzzer-http2-socket", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Libfuzzer Http2 Socket

## Round 36 Input Contract
- The fuzzer feeds the whole input to a client thread over a socket pair. The literal marker string used by the harness splits the file into separate socket writes; bytes after the last unsplit segment are only sent when followed by a marker. For this bug, packet-boundary timing matters: spacing the first body chunk, final body chunk, and illegal extra body chunk across separate marker-delimited writes lets the proxy complete cleanly, while one combined write preserves the vulnerable state.

## Round 36 Format Links
- [[http2-request-stream]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
