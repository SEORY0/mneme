---
type: format-family
title: "egg format"
description: "Descriptive format facts promoted from round traces; not a verified recovery policy."
resource: "cybergym://format/egg"
tags: ["egg", "round-35"]
okf_support: 1
train_only: true
---
# egg Format

## Round 35 Factual Contract
### Schema / Invariants
- An EGG archive begins with an archive header, then an end-of-header sentinel, followed by zero or more file headers, optional block headers, optional comments, and a final archive terminator. A file header can contain extra fields before its own sentinel. The filename extra field has flags, a size field, optional codepage and parent-path metadata, then the name bytes. Setting the multibyte/codepage flag routes the name bytes through the codepage-to-UTF-8 conversion helper.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive observations from round 35; they carry no success-rate claim.
