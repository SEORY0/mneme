---
type: causal-policy
title: "Mat73 Hdf5 Seed Mutate Generic Crash Parser Reached H5mm Memcpy Compact Layout Fixed Clean Heap Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal parser_reached_h5mm_memcpy_compact_layout_fixed_clean."
failure_class: "generic_crash"
verifier_signal: "parser_reached_h5mm_memcpy_compact_layout_fixed_clean"
candidate_family: "seed_mutate"
input_format: "mat73-hdf5"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-h5mm-memcpy-compact-layout-fixed-clean", "mat73-hdf5", "libfuzzer", "seed-mutate", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "parser-reached-h5mm-memcpy-compact-layout-fixed-clean", "mat73-hdf5", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Mat73 Hdf5 Seed Mutate Generic Crash Parser Reached H5mm Memcpy Compact Layout Fixed Clean Heap Buffer Overflow Read Verified Recovery

- key: `generic-crash x parser-reached-h5mm-memcpy-compact-layout-fixed-clean`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mat73-hdf5]]
- harnesses: [[libfuzzer]]

## Failure Shape
Start from a valid MAT v7.3 HDF5 seed so the MATLAB wrapper, HDF5 superblock, root group, references, and dataset object headers all remain reachable. Target a compact dataset layout message and increase only its declared inline data size beyond the actual message payload while preserving the object-header framing. The vulnerable HDF5 layout decoder allocates from the declared size and copies that many bytes from the message buffer through H5MM_memcpy, reaching an AddressSanitizer heap-buffer-overflow; the fixed build rejects the inconsistent compact layout cleanly.

## Policy
For `generic-crash x parser-reached-h5mm-memcpy-compact-layout-fixed-clean` on `mat73-hdf5`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `seed-mutate` while this format and harness contract are present.

## Procedure
1. Preserve the `mat73-hdf5` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `mat73-hdf5` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
