---
type: format-family
title: "udp-gsmtap-umts-rrc-per format"
description: "Structure and invariants observed for udp-gsmtap-umts-rrc-per."
resource: "cybergym://format/udp-gsmtap-umts-rrc-per"
tags: ["udp-gsmtap-umts-rrc-per", "round-33"]
okf_support: 1
---
# Schema

## Round 33 Factual Contract

### Schema / Invariants
- GSMTAP over UDP has a small fixed header with a payload type and subtype; UMTS RRC subtypes are dispatched directly to generated RRC PER dissectors. The RRC MasterInformationBlock can carry a v690 noncritical extension with a MultiplePLMN list. PLMN identities with optional MCC encode a presence bit for MCC and a mandatory MNC digit sequence.

### Harness Links
- [[afl]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
