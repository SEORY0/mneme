---
type: format-family
title: dns-message format
description: Format contract for dns-message.
resource: cybergym://format/dns-message
tags: [dns-message, "round-16"]
okf_support: 2
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

## Round 16 Factual Contract

### Schema / Invariants
- A DNS message contains a fixed header with section counts, followed by label-encoded names and resource records. SRV records use owner names conventionally shaped as service, protocol, and domain labels, and their rdata contains priority, weight, port, and a target name. Name compression and malformed/truncated labels are relevant to owner-name parsing.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
