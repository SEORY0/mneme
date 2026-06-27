---
type: format-family
title: Sddl String With Access Mask format
description: Format contract for sddl-string-with-access-mask inputs.
resource: cybergym://format/sddl-string-with-access-mask
tags: [sddl-string-with-access-mask, compile-time-missing-declaration, round-11]
okf_support: 1
train_only: true
---
# Schema
## Structure
The runtime input expected by the harness is a NUL-terminated SDDL security descriptor string with trailing bytes. The final bytes are also interpreted as a little-endian requested-access mask. SDDL descriptors can include owner, group, DACL, ACE type, rights, object GUIDs, and SIDs.

## Invariants
- Preserve the parser-recognition gates before mutating the vulnerability-specific relation.
- Prefer one causal field relation at a time; unrelated corruption weakens verifier attribution.

## Harness Links
- [[libfuzzer-samba-sddl-access-check]]

## Notes
- These are factual format observations only; they carry no success-rate claim.
