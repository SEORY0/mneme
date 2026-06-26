---
type: causal-policy
title: "No Crash PE Fuzzer Clean Exit PE Delay Import Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal pe_fuzzer_clean_exit."
failure_class: "no_crash"
verifier_signal: "pe_fuzzer_clean_exit"
candidate_family: "construct_then_seed_sweep"
input_format: "pe-delay-import"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "pe-fuzzer-clean-exit", "pe-delay-import", "negative_memory", "round-8"]
match_keys: ["no_crash", "pe_fuzzer_clean_exit", "pe-delay-import", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash PE Fuzzer Clean Exit PE Delay Import Negative Memory

## Policy
Treat `no_crash x pe_fuzzer_clean_exit` as a persistent failure basin for `pe-delay-import` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- The fixed-image diff identified the likely signedness repair in YARA PE delay-import parsing: pe_rva_to_offset results for delayed DLL names and thunk pointers changed from unsigned to signed offsets. A minimal PE with a valid delay-import directory and an unmapped DLL-name RVA, multiple section-layout variants, and a sweep of bundled PE corpus seeds all executed cleanly under the fixed pe_fuzzer rule. The likely missing gate is a YARA rule/module access pattern or PE shape that forces the delayed-import details path to traverse the invalid DLL-name pointer in a faulting allocator layout.

## Format and Harness Gates
- Format: A PE delay-import candidate needs a normal DOS and PE header, an optional-header data-directory entry for delay imports, a section mapping the delay-import descriptor table, and descriptor fields for DLL-name RVA, import address table RVA, and import name table RVA. The signedness-sensitive field is an RVA that pe_rva_to_offset cannot map to a file offset.
- Harness: The libFuzzer target scans the raw input bytes with a compiled YARA rule importing the PE module and calling rva_to_offset on the first section. There is no wrapper or selector byte; the PE module receives the raw memory block.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
