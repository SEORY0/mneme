---
type: format-family
title: "icu-collation-rule-utf16le format"
description: "Structure, build skeleton, and bug-prone areas of the icu-collation-rule-utf16le input format."
resource: cybergym://format/icu-collation-rule-utf16le
tags: ["icu-collation-rule-utf16le", "round-29"]
okf_support: 0
---
# ICU Collation Rule Utf16le Format

## Round 29 Factual Contract

### Schema / Invariants
- The selected input is an ICU RuleBasedCollator rule string, not a general ICU test file. Rules are UTF-16 code units; '&' introduces a reset, '<' and its variants introduce relations, 'prefix|string' creates contextual mappings, and '/' adds an extension. The parser accepts valid scalar text but rejects unpaired surrogate and noncharacter tailoring strings before the builder path.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
