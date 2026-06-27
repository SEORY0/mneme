---
type: format-family
title: dns-message format
description: Format contract for dns-message.
resource: cybergym://format/dns-message
tags: [dns-message]
okf_support: 1
train_only: true
---
# Schema
## Structure
Inputs follow the `dns-message` family contract.

## Invariants
- Parser reachability depends on preserving the format gates described below.

## Round 15 Factual Contract

### Schema / Invariants
- The DNS decoder requires a header with query/response direction consistent with the selected decode
  path. Query packets need at least one question and no answer or authority records; labels are
  decoded from question and record fields and may use normal labels or compression pointers.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
