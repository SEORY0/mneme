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

## Round 14 Factual Contract

### Schema / Invariants
- CIL is parenthesized policy text. Map classes are declared with classmap and classmapping, kernel classes with class, common permission sets with common, and classcommon links a kernel class to a common permission set.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 38 Factual Contract

### Schema / Invariants
- CIL policy text is S-expression based. A minimal policy scaffold needs class and permission declarations, class ordering, SID ordering and context, user/role/type/category/sensitivity declarations and ordering, sensitivity/category linkage, user level/range, role/type membership, and user-role linkage before optional policy constructs are accepted. Optional blocks, tunable conditionals, macro declarations, and macro calls are nested S-expression forms whose bodies are resolved by staged compiler passes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
