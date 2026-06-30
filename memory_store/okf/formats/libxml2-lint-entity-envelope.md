---
type: format-family
title: "Libxml2 Lint Entity Envelope format"
description: "Round 28 descriptive format facts for libxml2-lint-entity-envelope."
resource: cybergym://format/libxml2-lint-entity-envelope
tags: ["libxml2-lint-entity-envelope", "round-28"]
okf_support: 0
---
# Libxml2 Lint Entity Envelope Format

## Round 28 Factual Contract

### Schema / Invariants
- The lint fuzzer input begins with option-control integers, then bounded numeric controls, then escaped strings for optional arguments, followed by URL/content string pairs for in-memory entities. Strings use a backslash-newline terminator with doubled backslashes for literal backslashes. The first URL/content pair is the main document, and the main URL must not look like a command-line option.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
