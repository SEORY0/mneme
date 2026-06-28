---
type: causal-policy
title: "Sip Message Construct Sink Mismatch But Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 23 verified recovery for wrong_sink with verifier signal sink_mismatch_but_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "sink_mismatch_but_official_target_match"
candidate_family: "construct"
input_format: "sip-message"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "sink-mismatch-but-official-target-match", "sip-message", "libfuzzer", "construct", "verified-recovery", "round-23"]
match_keys: ["wrong-sink", "sink-mismatch-but-official-target-match", "sip-message", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Sip Message Construct Sink Mismatch But Official Target Match Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x sink_mismatch_but_official_target_match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[sip-message]]
- harnesses: [[libfuzzer]]

## Failure Shape
Construct a syntactically plausible SIP request with the required start line and common routing/identity headers, then end with a header-like line that is not line-terminated. The parser enters its error-reporting path and treats a non-NUL-terminated slice as a printable string, causing an over-read in the vulnerable build.

## Policy
For `wrong_sink x sink_mismatch_but_official_target_match` on `sip-message`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `sip-message` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `sip-message` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 1 attempts.
- Scope: generator repair only.
