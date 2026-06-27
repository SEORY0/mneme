---
type: format-family
title: "selinux-cil-policy-text format"
description: "Structure and reachability facts for SELinux CIL policy text."
resource: cybergym://format/selinux-cil-policy-text
tags: ["selinux-cil-policy-text"]
okf_support: 1
---
# Selinux Cil Policy Text Format

## Round 9 Factual Contract

### Schema / Invariants
- CIL policy text is parenthesized S-expression syntax.
- A minimal compilable policy needs class and classorder declarations, SID and sidorder
  declarations, user/role/type declarations, category and sensitivity ordering, sensitivity-category
  mapping, user ranges, role/type and user/role relations, and a SID context.
- Classpermission references in allow rules use the bare classpermission name, not a nested list.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
