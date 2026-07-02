---
type: format-family
title: "Fluent Bit Parser Config Format"
description: "Input contract facts for fluent-bit-parser-config."
tags: ["fluent-bit-parser-config", "round-30"]
okf_support: 0
train_only: true
---
# Fluent Bit Parser Config Format

## Round 30 Factual Contract

### Schema / Invariants
- Fluent Bit parser configuration is line-oriented text. Parser-related sections are bracketed headers followed by indented key/value properties. Multiline parser sections require at least a name key and a type key before type validation runs; invalid or missing required keys can route into parser configuration cleanup rather than normal parser registration.

### Harness Links
- [[libfuzzer-config-random]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
