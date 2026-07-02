---
type: format-family
title: "sip-uri format"
description: "Structure, build skeleton, and bug-prone areas of the sip-uri input format."
resource: cybergym://format/sip-uri
tags: ["sip-uri", "round-29"]
okf_support: 0
---
# Sip Uri Format

## Round 29 Factual Contract

### Schema / Invariants
- The relevant input is a bare SIP-style URI string, not a SIP message envelope. The parser recognizes SIP, secure SIP, telephone, and URN service-style schemes, then parses user, host, port, parameters, and headers. The URN branch performs fixed-prefix namespace checks before the normal state machine consumes the remaining URI body.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
