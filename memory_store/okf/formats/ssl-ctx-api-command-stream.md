---
type: format-family
title: "Ssl Ctx Api Command Stream Format"
description: "Input contract facts for ssl-ctx-api-command-stream."
tags: ["ssl-ctx-api-command-stream", "round-30"]
okf_support: 0
train_only: true
---
# Ssl Ctx Api Command Stream Format

## Round 30 Factual Contract

### Schema / Invariants
- The input is a compact SSL_CTX API command stream: each command begins with an operation selector, and some operations then consume additional bytes as fixed-width integers, length-prefixed strings, or the remaining byte slice. Signature algorithm lists are textual colon-separated names or key-plus-hash elements and are expected by the library parser to be C-string terminated.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
