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

## Round 29 Factual Contract

### Schema / Invariants
- The input is a single TPM2 command buffer. Multi-byte fields are big-endian. The command envelope contains a tag, a total-size field that must equal the full buffer length, a command selector, command handles, an authorization-session byte count, one password-session record, and command parameters. The define-space parameters contain a sized auth value followed by a sized NV public structure; the NV public structure contains an NV handle, hash algorithm, NV attributes, a sized auth policy, and a data-size field.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
