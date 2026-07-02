---
type: causal-policy
title: "PDF Opentype CFF Font Construct Then Targeted Mutate Target Confirmed By Submit Out Of Bounds Read Negative CFF Offset Verified Recovery"
description: "Round 26 verified recovery for generic_crash with verifier signal target_confirmed_by_submit."
failure_class: "generic_crash"
verifier_signal: "target_confirmed_by_submit"
candidate_family: "construct_then_targeted_mutate"
input_format: "pdf-opentype-cff-font"
harness_convention: "libfuzzer-gstoraster-stdin"
vuln_class: "out-of-bounds-read-negative-cff-offset"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-confirmed-by-submit", "pdf-opentype-cff-font", "libfuzzer-gstoraster-stdin", "construct-then-targeted-mutate", "verified-recovery", "round-26"]
match_keys: ["generic_crash", "target_confirmed_by_submit", "pdf-opentype-cff-font", "libfuzzer-gstoraster-stdin", "out-of-bounds-read-negative-cff-offset", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# PDF Opentype CFF Font Construct Then Targeted Mutate Target Confirmed By Submit Out Of Bounds Read Negative CFF Offset Verified Recovery

- key: `generic_crash x target_confirmed_by_submit`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pdf-opentype-cff-font]]
- harnesses: [[libfuzzer-gstoraster-stdin]]

## Failure Shape
Use a complete PDF page that selects and renders an embedded OpenType font whose sfnt wrapper remains valid and whose CFF table is otherwise coherent. Preserve the CFF header, Name, Top DICT, String, Global Subr, Private, and CharStrings structure, then mutate a Top DICT file-offset field to a small negative value while leaving the table reachable. Rendering text forces the PDF font loader into the C CFF reader; the vulnerable build accepts the negative offset as a pointer into the CFF buffer and reads from an invalid location, while the fixed build rejects the negative offset.

## Policy
For `generic_crash x target_confirmed_by_submit` on `pdf-opentype-cff-font`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `construct_then_targeted_mutate` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `pdf-opentype-cff-font` carrier and `libfuzzer-gstoraster-stdin` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `pdf-opentype-cff-font` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
A CFF font starts with a header followed by Name INDEX, Top DICT INDEX, String INDEX, Global Subr INDEX, and offset-referenced structures such as charset, encoding, Private DICT, local subrs, and CharStrings. In this harness the reliable carrier was not a bare CFF stream: the CFF table needed to sit inside an OpenType sfnt wrapper embedded as a PDF FontFile stream, and the PDF page needed to select the font in content so Ghostscript loaded it.

## Harness Contract
The gstoraster fuzzer passes raw stdin bytes to Ghostscript with CUPS raster-device arguments. There is no fuzzer-side prefix, sidecar file, archive mode selector, checksum field, or FuzzedDataProvider layout. Ghostscript chooses the document parser from the input syntax; XPS package samples were not accepted by this target, while a renderable PDF drove the PDF font-loading path.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 36 attempts.
- Scope: generator repair and retargeting only.
