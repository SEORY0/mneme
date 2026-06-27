---
type: format-family
title: selinux-binary-policy format
description: Format contract for selinux-binary-policy.
resource: cybergym://format/selinux-binary-policy
tags: [selinux-binary-policy]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `selinux-binary-policy` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The target format is a compiled SELinux binary policy, not CIL text. policydb_read expects the
  binary policy header and serialized symbol tables, then validates classes, roles, types, users,
  booleans, constraints, conditional lists, contexts, genfs data, and datum arrays.

### Harness Links
- [[libfuzzer-binpolicy]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
