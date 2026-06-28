---
type: format-family
title: "Sudo Policy Lines format"
description: "Descriptive contract facts for sudo-policy-lines."
resource: "cybergym://format/sudo-policy-lines"
tags: ["sudo-policy-lines", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The policy fuzzer input is line-oriented key/value text.
- Recognized lines populate plugin args, settings, user info, argv, and environment additions.
- The sudoedit seed needs progname and argv lines to request editing behavior; uid/user fields must correspond to a known user or policy evaluation exits early.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
