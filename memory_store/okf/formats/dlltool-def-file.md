---
type: format-family
title: "Dlltool Def File Format"
description: "Round 26 descriptive structure and invariant facts for dlltool-def-file."
tags: ["dlltool-def-file", "round-26"]
okf_support: 1
train_only: true
---
# Dlltool Def File Format

## Round 26 Factual Contract

### Schema / Invariants
- The relevant input is a textual dlltool .def file. Keywords such as an exports section select grammar contexts where quoted strings are accepted as identifiers. The flex quoted-string rule can match embedded NUL bytes because it is scanning file bytes, while C string duplication stops at the first NUL.

### Harness Links
- [[libfuzzer-tempfile]]

### Notes
- These are descriptive facts only; they carry no success-rate claim.
