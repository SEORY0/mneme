---
type: causal-policy
title: Wavefront Obj With Mtl Material Parser Not Reliably Reached With Sidecar Negative Memory
description: Negative memory for wavefront-obj-with-mtl candidates that ended in no_crash with verifier signal `material_parser_not_reliably_reached_with_sidecar`.
failure_class: no_crash
verifier_signal: material_parser_not_reliably_reached_with_sidecar
candidate_family: construct|archive_carrier
input_format: wavefront-obj-with-mtl
harness_convention: libfuzzer
vuln_class: out-of-bounds-read
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, material-parser-not-reliably-reached-with-sidecar, wavefront-obj-with-mtl, libfuzzer, construct-archive-carrier, out-of-bounds-read, negative-memory]
match_keys: [no-crash, material-parser-not-reliably-reached-with-sidecar, wavefront-obj-with-mtl, libfuzzer, construct-archive-carrier, out-of-bounds-read, negative-memory]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
Treat `no_crash with verifier signal `material_parser_not_reliably_reached_with_sidecar`` for `wavefront-obj-with-mtl` as evidence that the current carrier reached a clean or wrong harness basin, not the vulnerable invariant. Retarget by preserving only the proven parser gate and changing the missing relation named below.

## Procedure
1. Keep any parser-recognition envelope that reached `material_parser_not_reliably_reached_with_sidecar`.
2. Stop repeating the dead-end basin: The target MTL float parser needs OBJ import to open a material library as a separate stream. Plain OBJ inputs reached the OBJ importer but sidecar MTL files were unavailable. Direct MTL was not selected as a suitable model format. ZIP and self-referential material-path carriers either were treated as generic OBJ content or failed to reopen the intended MTL payload under the memory import harness.
3. Rebuild around `[[wavefront-obj-with-mtl]]` and `[[libfuzzer]]`, then mutate the narrow missing relation instead of adding unrelated padding or broad corruption.
4. Submit only after local verify produces a vulnerable-build crash or a plausible parser-branch wrong-sink crash; clean exits under this signal are not submit candidates.

## Negative Memory
- This is a persistent Round 11 failure basin, not a recovery recipe.
- Do not spend retries on the same carrier shape unless new evidence changes the verifier signal.
- If the harness itself reports usage or setup failure, fix the invocation/carrier contract before mutating vulnerability fields.

## Evidence Shape
- Support: 1 diagnosed Round 11 failed solve attempt.
- Attempts observed: 6.
