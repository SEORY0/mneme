---
type: causal-policy
title: "Ultrahdr Encoder Frame Construct Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 25 verified recovery for wrong_sink with verifier signal parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "construct"
input_format: "ultrahdr-encoder-frame"
harness_convention: "libfuzzer-fuzzed-data-provider"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached", "ultrahdr-encoder-frame", "libfuzzer-fuzzed-data-provider", "construct", "verified-recovery", "round-25"]
match_keys: ["wrong_sink", "parser_reached", "ultrahdr-encoder-frame", "libfuzzer-fuzzed-data-provider", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 25
---
# Ultrahdr Encoder Frame Construct Parser Reached Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ultrahdr-encoder-frame]]
- harnesses: [[libfuzzer-fuzzed-data-provider]]

## Failure Shape
Drive the encoder harness onto the raw-image JPEG/R path with generated image planes and control values that make the chroma sampling boundary path process a partial edge region. The parser and encoder state must be coherent enough to reach compression, then the plane geometry violates the row-stride and sampling invariant at the raw-data handoff.

## Policy
For `wrong_sink x parser_reached` on `ultrahdr-encoder-frame`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `ultrahdr-encoder-frame` carrier and `libfuzzer-fuzzed-data-provider` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `ultrahdr-encoder-frame` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
The fuzzer input is not a serialized UltraHDR file. It is a control stream consumed by the harness to synthesize raw image buffers, dimensions, quality, transfer metadata, and encoder mode before invoking the library.

## Harness Contract
The libFuzzer target uses FuzzedDataProvider-style consumption for scalar controls and generated buffers. The effective image data is constructed in memory by the harness, so successful inputs must satisfy the harness control contract rather than file magic or container checks.

## Evidence Shape
- Support: 1 server-verified round 25 solve after 1 attempt.
- Scope: generator repair and retargeting only.
