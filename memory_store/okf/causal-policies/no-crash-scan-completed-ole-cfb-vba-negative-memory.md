---
type: causal-policy
title: "No Crash Scan Completed Ole Cfb Vba Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal scan_completed."
failure_class: "no_crash"
verifier_signal: "scan_completed"
candidate_family: "seed_mutate"
input_format: "ole-cfb-vba"
harness_convention: "libfuzzer"
vuln_class: "buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "scan-completed", "ole-cfb-vba", "negative_memory", "round-8"]
match_keys: ["no_crash", "scan_completed", "ole-cfb-vba", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Scan Completed Ole Cfb Vba Negative Memory

## Policy
Treat `no_crash x scan_completed` as a persistent failure basin for `ole-cfb-vba` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Scratch CFB construction and real OLE document seeds scanned cleanly. Mutating high-level CFB size fields did not reach a VBA module stream with the missing size checks, so the scanner likely stayed in generic container parsing or skipped VBA extraction.

## Format and Harness Gates
- Format: OLE Compound File inputs use a fixed file signature, sector allocation tables, directory entries, and named streams. VBA reachability requires a coherent storage tree with module streams rather than just a valid CFB header.
- Harness: The ClamAV scanfile fuzzer writes the raw input to a temporary file and invokes the normal scanner with broad parse options enabled. The harness does not carve fields from the byte stream.

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
