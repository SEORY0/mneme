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

## Round 36 Factual Contract

### Schema / Invariants
- The file is parsed as text-format protobuf containing request and reply string fields. The request field is used as client-side HTTP bytes and the reply field emulates the upstream response. Binary HTTP/2 frames are a poor fit for this carrier because normal frame encodings include NUL bytes that are not preserved by the harness string handling.

### Harness Links
- [[libprotobuf-mutator-nginx-http-request-fuzzer]]

### Notes
- These facts are descriptive observations from round 36; they carry no success-rate claim.
