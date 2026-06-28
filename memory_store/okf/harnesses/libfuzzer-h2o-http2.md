---
type: harness-contract
title: "Libfuzzer H2o Http2 harness"
description: "Input contract facts for libfuzzer-h2o-http2."
tags: ["libfuzzer-h2o-http2", "round-24"]
okf_support: 1
---
# Libfuzzer H2o Http2 Harness

## Round 24 Factual Contract

### Input Contract
- The harness sends the raw input to an in-process client socket, splitting writes at a textual marker. It registers /chunked-test, /reproxy-test as a reverse proxy to a local Unix-socket upstream, and a file handler for the root path.

### Format Links
- [[http2-frame-stream]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
