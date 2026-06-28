---
type: format-family
title: "cyclonedds-xml-config format"
description: "Structure and invariants for the cyclonedds-xml-config input format."
tags: ["cyclonedds-xml-config", "round-14"]
okf_support: 1
---
# Schema
## Identification
Factual format observations distilled from verifier traces. These are descriptive facts only and carry no success-rate claim.

## Round 14 Factual Contract

### Schema / Invariants
- Network partitions are XML elements under Partitioning/NetworkPartitions with Name, Address, and optional Interface attributes; partition mappings can refer to a network partition by name. Attribute matching is tolerant of case in common examples.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
