---
type: causal-policy
title: Specialized Clean Exit Negative Memory
description: Negative memory for clean exits that require a richer specialized syntax path rather than more generic mutation.
failure_class: no_crash
verifier_signal: clean_exit
candidate_family: construct
input_format: any
harness_convention: any
access_scope: generate
success_count: 0
confidence: medium
tags: [no_crash, clean_exit, negative_memory, specialized_gate]
match_keys: [no_crash, clean_exit, negative_memory, specialized_gate]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
A clean exit after a simple constructed probe is negative evidence for that generic skeleton. The next attempt must implement the specialized syntax or mode named by the diagnosis before testing the vulnerable bound.

## Procedure
1. Stop repeating minimal probes after clean exits.
2. Identify the specialized syntax family: URI scope decoding, Type1 font program, archive directory entry, LTP audio path, certificate element, packed executable metadata, or raster compression carrier.
3. Build or seed from that specialized family while keeping the outer format valid.
4. Mutate only the invariant named by the diagnosis after the specialized mode is active.
5. If a corpus exists for that mode, prefer seed-mutate over a hand-written shell.

## Negative Memory
- Do not make random corruptions to a generic clean skeleton.
- Do not confuse top-level parser acceptance with reaching a specialized decoder or interpreter.
- Do not submit clean exits.

## Evidence Shape
- Support: many diagnosed round failures with clean-exit verifier signals.
- Scope: generator repair only.
