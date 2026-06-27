---
type: format-family
title: "DNS Response"
description: "Round 19 factual format contract for dns-response."
resource: cybergym://format/dns-response
tags: ["dns-response", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# DNS Response

## Round 19 Factual Contract

- DNS responses begin with a fixed-size header containing question and answer counts, followed by encoded names and typed resource records with class, TTL, declared RDATA length, and type-specific payload. The GLib resolver parser walks the question and answer sections and dispatches typed RDATA parsing for records such as address, service, mail-exchanger, authority, and text records.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
