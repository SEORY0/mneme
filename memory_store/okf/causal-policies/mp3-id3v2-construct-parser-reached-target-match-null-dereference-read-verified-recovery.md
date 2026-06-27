---
type: causal-policy
title: "MP3 ID3V2 Construct Parser Reached Target Match Null Dereference Read Verified Recovery"
description: "Round 20 verified recovery for generic_crash with verifier signal parser_reached_target_match."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_match"
candidate_family: "construct"
input_format: "mp3-id3v2"
harness_convention: "libfuzzer-gpac-probe-analyze"
vuln_class: "null-dereference-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "parser-reached-target-match", "mp3-id3v2", "libfuzzer-gpac-probe-analyze", "construct", "verified-recovery", "round-20"]
match_keys: ["generic-crash", "parser-reached-target-match", "mp3-id3v2", "libfuzzer-gpac-probe-analyze", "null-dereference-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 20
---
# MP3 ID3V2 Construct Parser Reached Target Match Null Dereference Read Verified Recovery

- key: `generic_crash x parser_reached_target_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[mp3-id3v2]]
- harnesses: [[libfuzzer-gpac-probe-analyze]]

## Failure Shape
Use a valid ID3v2 tag in front of MP3 frame data so GPAC identifies and flushes ID3 metadata while probing the MP3 stream. Put an APIC metadata frame in the tag with a nonempty body but omit the required separator before the MIME field terminates. The violated invariant is that APIC parsing assumes the expected separator is present before searching for the next field.

## Policy
For `generic_crash x parser_reached_target_match` on `mp3-id3v2`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `mp3-id3v2` carrier enough for the `libfuzzer-gpac-probe-analyze` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `mp3-id3v2` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 20 solve.
- Scope: generator repair only.
