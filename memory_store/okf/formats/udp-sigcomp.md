---
type: format-family
title: "UDP Sigcomp Format"
description: "Round 27 descriptive format facts for udp-sigcomp."
resource: cybergym://format/udp-sigcomp
tags: ["udp-sigcomp", "round-27"]
okf_support: 1
---
# UDP Sigcomp Format

## Round 27 Factual Contract

- The useful input is a raw UDP datagram carrying a SigComp message.
- UDP port dispatch is enough to enter SigComp, and a zero UDP checksum is accepted by the harness.
- A SigComp message must start with the SigComp signature bits and can use the uploaded-bytecode form, whose compact header declares bytecode length and a small encoded UDVM destination.

### Harness Links
- [[libfuzzer-fuzzshark-udp]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
