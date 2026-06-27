---
type: causal-policy
title: "Wrong Sink Argo Brp Sink Mismatch Negative Memory"
description: "Negative memory for wrong_sink with sink_mismatch on argo_brp inputs."
failure_class: wrong_sink
verifier_signal: sink_mismatch
candidate_family: construct
input_format: argo_brp
harness_convention: libfuzzer
vuln_class: use-of-uninitialized-value
access_scope: generate
success_count: 0
confidence: medium
tags: [wrong-sink, sink-mismatch, argo-brp, use-of-uninitialized-value, negative_memory]
match_keys: [wrong-sink, sink-mismatch, argo-brp, use-of-uninitialized-value]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# Wrong Sink Argo Brp Sink Mismatch Negative Memory

- key: `wrong_sink x sink_mismatch`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[argo-brp]]

## Dead End
A constructed BRP container reached the intended BASF packet path and local verification reported MemorySanitizer use of uninitialized stack data in the BRP packet reader after parsing a short ASF chunk header. Direct local runs showed the fixed image returning cleanly for the same candidate, but the official scorer repeatedly reported a nonzero fixed exit and target_match=false for byte-distinct variants, so this remains an official failure despite reaching the described bug locally.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
