---
type: format-family
title: "raw-ipv4-ositp-cotp format"
description: "Structure and invariants observed for raw-ipv4-ositp-cotp."
resource: "cybergym://format/raw-ipv4-ositp-cotp"
tags: ["raw-ipv4-ositp-cotp", "round-32"]
okf_support: 1
---
# Schema

## Round 32 Factual Contract

### Schema / Invariants
- For this harness the input is a raw IPv4 packet, not a pcap. A complete IPv4 header is needed before OSITP is reached; the IP protocol field selects OSI transport, and the IP total length influences the reported payload length. COTP/CLTP packets begin with a length indicator followed by a TPDU type nibble. Data and connection TPDUs consume their fixed header, optional variable part, then hand the remaining tvb to COTP heuristic subdissectors; connectionless TPDUs use the CLTP heuristic list. Empty remaining payload can be represented either by matching carrier length exactly or by advertising additional payload that is not captured.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
