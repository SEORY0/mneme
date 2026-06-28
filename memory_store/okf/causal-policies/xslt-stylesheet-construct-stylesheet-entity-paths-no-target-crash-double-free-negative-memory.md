---
type: causal-policy
title: Xslt Stylesheet Stylesheet Entity Paths No Target Crash Negative Memory
description: Negative memory for xslt stylesheet candidates that ended in no_crash with verifier signal `stylesheet_entity_paths_no_target_crash`.
failure_class: no_crash
verifier_signal: stylesheet_entity_paths_no_target_crash
candidate_family: construct
input_format: xslt stylesheet
harness_convention: libfuzzer
vuln_class: double-free
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, stylesheet-entity-paths-no-target-crash, xslt-stylesheet, libfuzzer, construct, double-free, negative-memory]
match_keys: [no-crash, stylesheet-entity-paths-no-target-crash, xslt-stylesheet, libfuzzer, construct, double-free, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `stylesheet_entity_paths_no_target_crash`` for `xslt stylesheet` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `stylesheet_entity_paths_no_target_crash`.
2. Stop repeating the dead-end basin: Entity-containing stylesheet probes parsed and transformed successfully but did not leave an entity node in the stylesheet ownership graph in a way that caused duplicate cleanup. The missing condition is likely a narrower stylesheet tree shape or import/include ownership transition where an entity reference node survives parsing without normal substitution and is then freed through both stylesheet and document teardown.
3. Rebuild around `[[xslt-stylesheet]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.
