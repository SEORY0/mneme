---
type: format-family
title: "Libxslt Fuzz Entities"
description: "Round 12 factual format contract for libxslt-fuzz-entities."
resource: cybergym://format/libxslt-fuzz-entities
tags: ["libxslt-fuzz-entities", "format-contract", "round-12"]
okf_support: 10
train_only: true
---
# Libxslt Fuzz Entities

## Round 12 Factual Contract

### Schema / Invariants
- The XSLT fuzzer input starts with a big-endian allocation-limit word followed by escaped string pairs representing URL and entity contents. The first entity is the stylesheet and the second entity is the source document. Strings terminate with the harness escape-newline convention, and backslashes are escaped.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 22 Factual Contract

### Schema / Invariants
- The XSLT fuzzer consumes a big-endian allocation-limit prefix, then a sequence of virtual entities. Each virtual entity is encoded as a URL string and a content string terminated by a backslash-newline marker, with doubled backslashes used for literal backslashes. The first entity is the stylesheet and the second entity is the source XML document.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 27 Factual Contract

- The XSLT fuzz target input begins with a big-endian allocation-limit word.
- The rest is a sequence of escaped URL/content string pairs; each string is terminated by the harness escape-newline marker and literal backslashes are doubled.
- The first pair is the stylesheet, and the second pair is the source XML document.

### Harness Links
- [[libfuzzer-libxslt-entity-framing-with-malloc-limit]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
