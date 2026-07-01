---
type: format-family
title: "wireshark-raw-udp-sctp-tls format"
description: "Structure and invariants observed for wireshark-raw-udp-sctp-tls."
resource: "cybergym://format/wireshark-raw-udp-sctp-tls"
tags: ["wireshark-raw-udp-sctp-tls", "round-33"]
okf_support: 1
---
# Schema

## Round 33 Factual Contract

### Schema / Invariants
- For this carrier, the outer bytes are a raw UDP datagram with a normal UDP header and payload. UDP port dispatch can select SCTP's UDP tunneling dissector. SCTP uses a common header followed by padded chunks; a complete DATA chunk carries a TSN, stream identifiers, a payload protocol identifier, and application payload. SCTP upper-layer dissection checks the PPI table before falling back to source and destination SCTP port tables, so an unclaimed nonzero PPI plus a TLS-associated SCTP port reaches TLS with non-null SCTP metadata as the data argument.

### Harness Links
- [[libfuzzer-fuzzshark-ip-proto-udp]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
