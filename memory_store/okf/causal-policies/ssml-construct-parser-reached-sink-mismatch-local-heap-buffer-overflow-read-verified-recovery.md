---
type: causal-policy
title: "Ssml Construct Parser Reached Sink Mismatch Local Heap Buffer Overflow Read Verified Recovery"
description: "Round 22 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_local."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_local"
candidate_family: "construct"
input_format: "ssml"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-sink-mismatch-local", "ssml", "libfuzzer", "construct", "verified-recovery", "round-22"]
match_keys: ["wrong-sink", "parser-reached-sink-mismatch-local", "ssml", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 22
---
# Ssml Construct Parser Reached Sink Mismatch Local Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_sink_mismatch_local`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ssml]]
- harnesses: [[libfuzzer]]

## Failure Shape
Feed raw SSML text containing a tag opener that begins normal markup parsing but never provides the terminating syntax the SSML parser expects. The harness adds a string terminator after the input, and the vulnerable parser advances its UTF-8 decoder past the allocated copy while scanning the malformed tag.

## Policy
For `wrong_sink x parser_reached_sink_mismatch_local` on `ssml`, preserve the parser and harness gates first, then change the causal invariant identified by the verified recovery. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `ssml` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `ssml` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 22 solve after 1 attempts.
- Scope: generator repair only.
