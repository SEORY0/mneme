---
type: causal-policy
title: "Zlib Deflate Construct Plausible Parser Crash Confirmed By Submit Use Of Uninitialized Value Verified Recovery"
description: "Round 23 verified recovery for generic_crash with verifier signal plausible_parser_crash_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "plausible_parser_crash_confirmed_by_submit"
candidate_family: "construct"
input_format: "zlib-deflate"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "plausible-parser-crash-confirmed-by-submit", "zlib-deflate", "libfuzzer", "construct", "verified-recovery", "round-23"]
match_keys: ["generic-crash", "plausible-parser-crash-confirmed-by-submit", "zlib-deflate", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 23
---
# Zlib Deflate Construct Plausible Parser Crash Confirmed By Submit Use Of Uninitialized Value Verified Recovery

- key: `generic_crash x plausible_parser_crash_confirmed_by_submit`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[zlib-deflate]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a valid zlib wrapper and a fixed-Huffman deflate block whose first emitted item is a length/distance pair with the maximum distance symbol that maps to the vulnerable zero base. Avoid producing a prior literal so the zero-distance copy reads from the current output cursor before initialized bytes exist.

## Policy
For `generic_crash x plausible_parser_crash_confirmed_by_submit` on `zlib-deflate`, preserve the format recognition, harness contract, and parser reachability gates before varying the causal invariant. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `zlib-deflate` carrier enough for the `libfuzzer` harness to reach the observed parser path.
2. Keep envelope fields minimal and internally consistent so verifier feedback remains tied to the target relation.
3. Apply the verified invariant from the failure shape before broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `zlib-deflate` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 23 solve after 6 attempts.
- Scope: generator repair only.
