---
type: format-family
title: "text-format-protobuf-http-request format"
description: "Structure and invariants for the text-format-protobuf-http-request input format."
tags: ["text-format-protobuf-http-request", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- The fuzzer input is text-format protobuf named HttpProto with required request and reply string fields. The harness copies those strings through C string accessors, so binary protocols containing zero bytes can be truncated before nginx receives them.

### Harness Links
- [[libfuzzer-protobuf-mutator]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
