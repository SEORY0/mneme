---
type: format-family
title: Gquic Quic Crypto Data format
description: Format contract for gquic/quic crypto data inputs.
resource: cybergym://format/gquic-quic-crypto-data
tags: [gquic-quic-crypto-data, stale-plaintext-user-agent-extraction, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
This target accepts crypto-data oriented QUIC input rather than a full pcap. A leading selector maps to supported QUIC versions, then the remaining data is interpreted as version-specific crypto data; legacy GQUIC paths parse CHLO tags such as SNI, UAID, and idle-timeout fields.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
