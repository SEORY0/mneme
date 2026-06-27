---
type: harness-contract
title: "Unavailable After Gen Extraction Failure harness"
description: "Input contract facts for unavailable-after-gen-extraction-failure."
tags: ["unavailable-after-gen-extraction-failure", "round-15"]
okf_support: 1
---
# Unavailable After Gen Extraction Failure Harness

## Round 15 Input Contract
- The intended harness could not be confirmed from a completed gen_info/verify_config pair because
  generation stopped during archive extraction. Partial source extraction showed an OpenThread tree,
  but this worker did not reconstruct the missing runner metadata or run a verifier for this task.

## Format Links
- [[openthread-dataset-tlv]]

## Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.
