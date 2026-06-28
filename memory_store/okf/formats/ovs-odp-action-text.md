---
type: format-family
title: ovs-odp-action-text format
description: Format contract for ovs-odp-action-text.
resource: cybergym://format/ovs-odp-action-text
tags: [ovs-odp-action-text]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `ovs-odp-action-text` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- OVS ODP action text is a comma-delimited action language. push_nsh accepts named fields such as
  flags, ttl, mdtype, next protocol, service path, service index, and either fixed context words for
  metadata type 1 or a hex md2 field for metadata type 2. The md2 hex is parsed into bytes and padded
  to word alignment before it is serialized into the netlink action.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 25 Factual Contract

### Schema / Invariants
- OVS ODP action text is comma-delimited C-string action syntax. The push_nsh action accepts named fields including metadata type and an md2 hexadecimal metadata field. The md2 text is decoded to bytes, padded to word alignment, and serialized into a nested action attribute.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
