---
type: causal-policy
title: "Imagemagick Xc Color String Construct Wrong Sink Parser Reached Target Crash Heap Buffer Overflow Read Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_target_crash."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_crash"
candidate_family: "construct"
input_format: "imagemagick-xc-color-string"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-target-crash", "imagemagick-xc-color-string", "libfuzzer", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-target-crash", "imagemagick-xc-color-string", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Imagemagick Xc Color String Construct Wrong Sink Parser Reached Target Crash Heap Buffer Overflow Read Verified Recovery

- key: `wrong-sink x parser-reached-target-crash`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[imagemagick-xc-color-string]]
- harnesses: [[libfuzzer]]

## Failure Shape
The harness accepts raw bytes as the color suffix for an ImageMagick XC pseudo-image. A non-empty byte string at the maximum accepted harness size, with no embedded terminator, reaches construction of a C-style string from the fuzzer buffer and forces the library call path to scan past the supplied allocation. The fixed build rejects or bounds this conversion before the out-of-bounds read.

## Policy
For `wrong-sink x parser-reached-target-crash` on `imagemagick-xc-color-string`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `imagemagick-xc-color-string` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `imagemagick-xc-color-string` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
