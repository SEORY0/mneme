---
type: causal-policy
title: "Zip Construct Parser Reached Vul Only Zip Mem Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 25 verified recovery for wrong_sink with verifier signal parser_reached_vul_only_zip_mem_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_vul_only_zip_mem_read"
candidate_family: "construct"
input_format: "zip"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-vul-only-zip-mem-read", "zip", "libfuzzer", "construct", "verified-recovery", "round-25"]
match_keys: ["wrong_sink", "parser_reached_vul_only_zip_mem_read", "zip", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 25
---
# Zip Construct Parser Reached Vul Only Zip Mem Read Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_vul_only_zip_mem_read`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[zip]]
- harnesses: [[libfuzzer]]

## Failure Shape
Construct a ZIP-like archive where the end-of-central-directory record is found before the declared central directory, while the central directory itself lies later in the buffer and passes size checks against the total archive size. This underflows the computed archive-start offset and makes the in-memory reader believe offsets beyond the backing buffer are valid. A central-directory entry whose local-header offset points just beyond the buffer then triggers an out-of-bounds read during header validation; the fixed build rejects the inconsistent archive start.

## Policy
For `wrong_sink x parser_reached_vul_only_zip_mem_read` on `zip`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `zip` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `zip` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
ZIP readers locate the EOCD by scanning backward, then read central-directory size, central-directory offset, entry count, and per-file central-directory headers. Central-directory entries include file metadata and a local-header offset; local headers are validated before extraction.

## Harness Contract
The miniz zip fuzzer treats the raw input as an in-memory ZIP archive, initializes the ZIP reader, iterates non-directory files, validates headers, reads filenames and file stats, and attempts extraction for stored or deflated entries. There is no extra harness carving.

## Evidence Shape
- Support: 1 server-verified round 25 solve after 2 attempts.
- Scope: generator repair and retargeting only.
