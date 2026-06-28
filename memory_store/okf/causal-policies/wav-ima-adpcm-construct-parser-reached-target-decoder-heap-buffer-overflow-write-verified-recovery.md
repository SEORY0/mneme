---
type: causal-policy
title: "Wav Ima Adpcm Construct Parser Reached Target Decoder Heap Buffer Overflow Write Verified Recovery"
description: "Round 23 verified recovery for generic_crash with verifier signal parser_reached_target_decoder."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_decoder"
candidate_family: "construct"
input_format: "wav/ima-adpcm"
harness_convention: "afl/libfuzzer file wrapper"
vuln_class: "heap-buffer-overflow-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-target-decoder", "wav-ima-adpcm", "afl-libfuzzer-file-wrapper", "construct", "verified-recovery", "round-23"]
match_keys: ["generic-crash", "parser-reached-target-decoder", "wav-ima-adpcm", "afl-libfuzzer-file-wrapper", "heap-buffer-overflow-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Wav Ima Adpcm Construct Parser Reached Target Decoder Heap Buffer Overflow Write Verified Recovery

- key: `generic_crash x parser_reached_target_decoder`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[wav-ima-adpcm]]
- harnesses: [[afl-libfuzzer-file-wrapper]]

## Failure Shape
Build a RIFF/WAVE file whose fmt chunk selects IMA ADPCM and whose declared block alignment and samples-per-block pass the WAV reader formula, but leave a partial encoded ADPCM group. The decoder still expands a full group of nibbles into the sample buffer, exceeding the allocation derived from the smaller declared sample count.

## Policy
For `generic_crash x parser_reached_target_decoder` on `wav/ima-adpcm`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `wav/ima-adpcm` carrier enough for the `afl/libfuzzer file wrapper` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `wav/ima-adpcm` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 2 attempts.
- Scope: generator repair only.
