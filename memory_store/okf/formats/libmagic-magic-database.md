---
type: format-family
title: libmagic-magic-database format
description: Structure and reachability facts for libmagic-magic-database inputs.
tags: [libmagic-magic-database]
okf_support: 0
---
# Libmagic Magic Database Format

## Round 10 Factual Contract

### Schema / Invariants
- The active input is a textual magic database, not arbitrary bytes to classify. Rules contain an offset expression, a type/test, a message, and optional annotation lines such as strength adjustments; the loader compiles these into magic entries before dumping or checking them.

### Harness Links
- [[file-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
