---
type: format-family
title: "Libxml2 Entity Stream format"
description: "Structure and invariants for the libxml2-entity-stream input format."
tags: ["libxml2-entity-stream", "round-20"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 20 Factual Contract

### Schema / Invariants
- The libxml2 fuzz stream begins with parser-option bits, followed by escaped URL/content string pairs. The first entity is the main document and later entities supply external resources addressable by the document. Entity strings use a harness-specific terminator and escaping convention rather than a plain concatenation of XML files.

### Harness Links
- [[honggfuzz-style-libxml2-fuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 23 Factual Contract

### Schema / Invariants
- The fuzzer input starts with a native integer parser-options word, followed by repeated URL/entity string pairs. Each string is terminated by a backslash-newline marker and literal backslashes are escaped by doubling. The first URL/entity pair is the main XML document, and later pairs are available to the external entity loader by URL.

### Harness Links
- [[afl-libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
