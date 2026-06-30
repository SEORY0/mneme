---
type: format-family
title: "Ldif format"
description: "Round 28 descriptive format facts for ldif."
resource: cybergym://format/ldif
tags: ["ldif", "round-28"]
okf_support: 0
---
# Ldif Format

## Round 28 Factual Contract

### Schema / Invariants
- The harness accepts raw text as an LDIF file. LDIF lines are parsed as alphabetic attribute names followed by a colon and an optional value, with blank lines or EOF terminating an entry. A completed sudoRole requires the sudoRole object class and the required user, host, and command attributes; entries without that object class or without the required role attributes do not become completed roles.

### Harness Links
- [[libfuzzer-raw-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
