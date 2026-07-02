---
type: causal-policy
title: "Pdf Encrypt Dictionary Construct Wrong Sink Parser Reached Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 30 verified recovery for wrong_sink with verifier signal parser_reached_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_official_target_match"
candidate_family: "construct"
input_format: "pdf-encrypt-dictionary"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-official-target-match", "pdf-encrypt-dictionary", "libfuzzer", "construct", "verified-recovery", "round-30"]
match_keys: ["wrong-sink", "parser-reached-official-target-match", "pdf-encrypt-dictionary", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Pdf Encrypt Dictionary Construct Wrong Sink Parser Reached Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `wrong-sink x parser-reached-official-target-match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pdf-encrypt-dictionary]]
- harnesses: [[libfuzzer]]

## Failure Shape
Build a minimal renderable PDF with a normal catalog, pages tree, page object, content stream, xref/trailer, and a trailer-referenced Standard encryption dictionary. The key relation is to select an encryption version that installs the widest key length while selecting an older revision that still authenticates through the MD5/RC4 password branch. Supplying the required owner/user strings, permissions, metadata flag, and trailer ID reaches blank-password authentication; the vulnerable build then feeds digest-derived key material wider than the digest actually initialized, while the fixed build rejects or clamps the relation cleanly.

## Policy
For `wrong-sink x parser-reached-official-target-match` on `pdf-encrypt-dictionary`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `pdf-encrypt-dictionary` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `pdf-encrypt-dictionary` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
