---
type: causal-policy
title: "Pe Coff Bigobj Construct Wrong Sink Parser Reached Comdat Aux Memcpy Heap Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_comdat_aux_memcpy."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_comdat_aux_memcpy"
candidate_family: "construct"
input_format: "pe-coff-bigobj"
harness_convention: "libfuzzer-binutils-bfd-object"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-comdat-aux-memcpy", "pe-coff-bigobj", "libfuzzer-binutils-bfd-object", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-comdat-aux-memcpy", "pe-coff-bigobj", "libfuzzer-binutils-bfd-object", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Pe Coff Bigobj Construct Wrong Sink Parser Reached Comdat Aux Memcpy Heap Buffer Overflow Read Verified Recovery

- key: `wrong-sink x parser-reached-comdat-aux-memcpy`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pe-coff-bigobj]]
- harnesses: [[libfuzzer-binutils-bfd-object]]

## Failure Shape
Construct a minimal PE/COFF bigobj object that BFD recognizes: a valid bigobj-style file header, one COMDAT section, raw section content, and a symbol table. Use a C_FILE symbol whose declared auxiliary-entry count is larger than the physically supplied auxiliary filename data. The COMDAT section gate makes BFD build the COMDAT hash, which swaps the C_FILE auxiliary record and trusts the declared aux count for the extended filename copy; the vulnerable build reads beyond the raw symbol buffer, while the fixed build rejects the inconsistent aux span.

## Policy
For `wrong-sink x parser-reached-comdat-aux-memcpy` on `pe-coff-bigobj`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `pe-coff-bigobj` carrier enough for the `libfuzzer-binutils-bfd-object` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `pe-coff-bigobj` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
