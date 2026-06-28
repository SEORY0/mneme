---
type: causal-policy
title: "Sony Arw Tiff Construct Parser Reached Arw Decoder Stack Memory Safety Raw Decoder Verified Recovery"
description: "Round 21 verified recovery for wrong-sink with verifier signal parser-reached-arw-decoder-stack."
failure_class: "wrong-sink"
verifier_signal: "parser-reached-arw-decoder-stack"
candidate_family: "construct"
input_format: "sony-arw-tiff"
harness_convention: "libfuzzer"
vuln_class: "memory-safety-raw-decoder"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-arw-decoder-stack", "sony-arw-tiff", "libfuzzer", "construct", "verified-recovery", "round-21"]
match_keys: ["wrong-sink", "parser-reached-arw-decoder-stack", "sony-arw-tiff", "libfuzzer", "memory-safety-raw-decoder"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 21
---
# Sony Arw Tiff Construct Parser Reached Arw Decoder Stack Memory Safety Raw Decoder Verified Recovery

- key: `wrong-sink x parser-reached-arw-decoder-stack`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[sony-arw-tiff]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build a compact TIFF-style Sony RAW carrier with MAKE selecting Sony, a compressed ARW path, strip offset/count fields, bit-depth and image dimensions that select ARWv1, and a minimally odd accepted image height. Keep the strip payload present but small enough that the vulnerable decoder enters raw-image allocation and ARWv1 decoding; the fixed build rejects the odd-height invariant before the vulnerable memory path.

## Policy
For `wrong-sink x parser-reached-arw-decoder-stack` on `sony-arw-tiff`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `sony-arw-tiff` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `sony-arw-tiff` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 21 solve after 6 attempts.
- Scope: generator repair only.
