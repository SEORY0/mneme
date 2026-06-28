---
type: format-family
title: Raw Ipv4 Packet Carrying Netbios format
description: Format contract for raw IPv4 packet carrying NetBIOS inputs.
resource: cybergym://format/raw-ipv4-packet-carrying-netbios
tags: [raw-ipv4-packet-carrying-netbios, heap-buffer-overflow-read, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The format is a raw network packet. For UDP name-service traffic, nDPI expects an IPv4/UDP envelope with NetBIOS header counters and then an encoded name. The encoded NetBIOS name uses a leading length-like byte followed by encoded character pairs, and parser trust in that length is the key invariant.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-raw-packet-processor]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
