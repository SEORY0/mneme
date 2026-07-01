---
type: format-family
title: "Wget Config format"
description: "Round 8 descriptive format facts for wget-config."
resource: cybergym://format/wget-config
tags: ["wget-config", "round-8"]
okf_support: 1
---
# Wget Config Format

## Round 8 Factual Contract

### Schema / Invariants
- The input is a wget2 configuration file, not a URL. The parser accepts directive/value records with several separators; include directives may route path strings through glob expansion and tilde handling.

### Harness Links
- [[afl-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Schema / Invariants
- The input is a wget2 configuration file made of directive/value records. The parser accepts directive values after whitespace, equals, or comma separators. Include directives recurse through read_config_expand and call glob with tilde expansion and directory marking; several filename-valued options can also invoke shell-style tilde expansion, but broad filename-option variants were clean here.

### Harness Links
- [[honggfuzz-file]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
