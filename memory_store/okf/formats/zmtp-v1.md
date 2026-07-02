---
type: format-family
title: "ZMTP V1 Format"
description: "Round 27 descriptive format facts for zmtp-v1."
resource: cybergym://format/zmtp-v1
tags: ["zmtp-v1", "round-27"]
okf_support: 1
---
# ZMTP V1 Format

## Round 27 Factual Contract

- ZMTP v1 is a raw frame stream rather than a file container.
- The unversioned path is selected before the modern greeting path; v1 frames are length-prefixed and carry a flags byte before the body.
- The initial routing-id/message frame must be accepted before later message-body frames exercise allocator behavior.

### Harness Links
- [[libfuzzer-mock-tcp]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
