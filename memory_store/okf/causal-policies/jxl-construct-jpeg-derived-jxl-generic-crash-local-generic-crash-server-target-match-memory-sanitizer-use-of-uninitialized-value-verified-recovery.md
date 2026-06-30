---
type: causal-policy
title: "Jxl Construct Jpeg Derived Jxl Generic Crash Local Generic Crash Server Target Match Memory Sanitizer Use Of Uninitialized Value Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal local_generic_crash_server_target_match."
failure_class: "generic_crash"
verifier_signal: "local_generic_crash_server_target_match"
candidate_family: "construct_jpeg_derived_jxl"
input_format: "jxl"
harness_convention: "libfuzzer"
vuln_class: "memory-sanitizer-use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "local-generic-crash-server-target-match", "jxl", "libfuzzer", "construct-jpeg-derived-jxl", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "local-generic-crash-server-target-match", "jxl", "libfuzzer", "memory-sanitizer-use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Jxl Construct Jpeg Derived Jxl Generic Crash Local Generic Crash Server Target Match Memory Sanitizer Use Of Uninitialized Value Verified Recovery

- key: `generic-crash x local-generic-crash-server-target-match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[jxl]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build a valid JPEG-derived JPEG XL codestream whose frame uses YCbCr chroma subsampling. Use image dimensions that cross decoder group boundaries on both axes so the YCbCr upsampler needs mirrored right and bottom padding from the next group. Keep the codestream otherwise encoder-valid and append neutral djxl_fuzzer tail flags so pixel decoding consumes the affected output.

## Policy
For `generic-crash x local-generic-crash-server-target-match` on `jxl`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct-jpeg-derived-jxl` while this format and harness contract are present.

## Procedure
1. Preserve the `jxl` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `jxl` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
