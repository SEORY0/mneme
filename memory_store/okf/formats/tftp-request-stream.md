---
type: format-family
title: "Tftp Request Stream"
description: "Round 19 factual format contract for tftp-request-stream."
resource: cybergym://format/tftp-request-stream
tags: ["tftp-request-stream", "format-contract", "round-19"]
okf_support: 0
train_only: true
---

# Tftp Request Stream

## Round 19 Factual Contract

- The TFTP parser accepts a request packet with an operation selector followed by NUL-terminated filename and transfer-mode strings. Completing a request unit is enough to execute the generated done hook that calls the runtime accept hook.
- Harness link: [[libfuzzer]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.
