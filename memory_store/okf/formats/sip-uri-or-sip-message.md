---
type: format-family
title: "sip uri or sip message format"
description: "Descriptive format contract facts for sip uri or sip message."
tags: ["sip-uri-or-sip-message", "round-18"]
okf_support: 1
train_only: true
---
# SIP Uri Or SIP Message Format

## Round 18 Factual Contract

### Schema / Invariants
- SIP URIs carry scheme, user, host, optional port, and parameters. IPv6 hosts use bracketed address syntax, and AOR construction may include or drop the scheme and port depending on caller options.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
