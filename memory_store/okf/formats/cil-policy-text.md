---
type: format-family
title: "CIL Policy Text format"
description: "Descriptive contract facts for CIL Policy Text."
resource: "cybergym://format/cil-policy-text"
tags: ["cil-policy-text", "round-6", "round-16"]
okf_support: 13
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 6 Factual Contract

### Schema / Invariants
- CIL policy text uses parenthesized declarations. A classpermission declaration can be populated by classpermissionset rules, and classpermissionset bodies name class/permission pairs. Optional blocks can be disabled during resolution when a contained declaration or rule fails to resolve.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 16 Factual Contract

### Schema / Invariants
- CIL policy text is S-expression based. Classpermissions must be declared before classpermissionset definitions. A classpermissionset accepts either a direct class/permissions pair or a single named classpermission/classpermissionset reference, not a nested list of named references. Optional blocks are removed when they contain unresolved references.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.

## Round 17 Factual Contract

### Schema / Invariants
- CIL policies require enough global scaffolding for classorder, sidorder, user/role/type declarations, and allow rules before compilation continues into reset logic.
- Optional blocks may be removed when unresolved symbols remain inside them.
- A classcommon association links a class to a common permission set and survives as semantic state beyond simple text parsing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 18 Factual Contract

### Schema / Invariants
- CIL policy text is parenthesized S-expression-like declarations. A minimal policy needs class/permission, sid/user/role/type, allow, and context scaffolding before optional blocks and blockinherit declarations are semantically processed.

### Harness Links
- [[libfuzzer-raw-cil-policy]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.

## Round 27 Factual Contract

- CIL policy text is parenthesized S-expression syntax.
- A minimal compile path needs class and classorder declarations plus SID, user, role, type, sensitivity, category, role/type, user/role, userlevel, userrange, and SID context scaffolding.
- Classpermission macro parameters can be supplied either by a named classpermission or by an inline anonymous class/permission tuple; classpermissionset rules populate a classpermission from class/permission pairs.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 29 Factual Contract

### Schema / Invariants
- CIL policy text is an S-expression policy language. A minimal compile path needs class and classorder declarations, SID and sidorder declarations, user, role, type, role/type and user/role relations, category and sensitivity ordering, sensitivity-category mapping, user levels/ranges, a SID context, and at least one allow-style rule. A filename typetransition is represented as a typetransition form with source type, target type, object class, filename/name token, and result type. Macro parameters can be declared with flavors such as name/string, type, class, classpermission, level, levelrange, and ipaddr; anonymous classpermission and level-like arguments are accepted by the call-argument builder but are not valid filename-name datums.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 30 Factual Contract

### Schema / Invariants
- CIL policy text is an S-expression language. A small valid carrier needs class/classorder, SID/sidorder, user, role, type, category/categoryorder, sensitivity/sensitivityorder, sensitivity-category mapping, allow, role-type, user-role, user level/range, and SID context declarations before semantic rules such as optional blocks and validatetrans are processed. Constraint expressions accept operands such as transition type operands and either a single symbol or a list on the right side; nested non-string members in that right-side list violate the list-string invariant.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.

## Round 38 Factual Contract

### Schema / Invariants
- CIL policy input is S-expression text. A compact policy still needs coherent declarations and ordering for classes, security identifiers, users, roles, types, levels, categories, ranges, and at least one permission use so compile and policydb construction run. Class maps declare map permissions; class mappings bind those map permissions to concrete class-permission sets. Optional blocks can be disabled when later resolution fails.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
