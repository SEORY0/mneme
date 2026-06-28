---
type: format-family
title: "Tpm2 Command Buffer format"
description: "Descriptive contract facts for tpm2 command buffer."
resource: "cybergym://format/tpm2-command-buffer"
tags: ["tpm2-command-buffer", "round-17"]
okf_support: 1
train_only: true
---
# Schema
## Identification
Descriptive facts promoted from round traces; not a verified recovery policy.

## Round 17 Factual Contract

### Schema / Invariants
- The harness input is a TPM2 command buffer with a command tag, total-size field, command code, and optional command parameters.
- Multi-byte fields are big-endian and the declared command size must match the supplied buffer.

### Harness Links
- [[libfuzzer-libtpms-process-command]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
