---
type: causal-policy
title: Local Crash Server Clean Negative Memory
description: Negative memory for local verifier crashes that do not reproduce as official vulnerable-build crashes.
failure_class: generic_crash
verifier_signal: server_vul_clean
candidate_family: local_only_crash
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [generic_crash, server_vul_clean, local_only_crash, negative_memory]
match_keys: [generic_crash, server_vul_clean, local_only_crash, negative_memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
A local verifier crash is not sufficient evidence when the official server reports a clean
vulnerable-build run. Treat that candidate family as a basin to leave unless a smaller,
more causal mutation can reproduce through the server.

## Procedure
1. Record the local failure_class trajectory and the official server result.
2. If the server reports the vulnerable build clean, stop enlarging or complicating that
   candidate family.
3. Return to the format contract: identify the exact parser gate, channel/count invariant,
   checksum, or compression mode the server harness may require.
4. Rebuild from a valid seed or a smaller declarative skeleton before trying the same target
   again.

## Negative Memory
- Local-only segmentation faults can be artifacts of harness setup, malformed carriers, or
  non-target allocator behavior.
- Do not promote local-only crashes as recoveries.
- Submit results override local verifier impressions for learning.

## Evidence Shape
- Support: 1 train failure observation with local crash but official vulnerable-build clean.
- Scope: generator repair only.
