---
type: causal-policy
title: ZIP Long Member Name Stack Read Recovery
description: Recover import-path ZIP stack reads by preserving archive validity and lengthening a member filename.
failure_class: wrong_sink
verifier_signal: sanitizer_crash_target_path
candidate_family: construct
input_format: zip
harness_convention: libfuzzer
vuln_class: stack-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong_sink, sanitizer_crash_target_path, zip, long_member_name, import_path]
match_keys: [wrong_sink, sanitizer_crash_target_path, zip, long_member_name]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
When an importer opens archives before model parsing, use a valid ZIP carrier and make the member filename exceed the importer stack buffer while the member still looks plausible for the downstream import path.

## Procedure
1. Build a ZIP archive whose central directory and local header agree.
2. Include one model-like member body sufficient for archive enumeration to continue.
3. Put the mutation in the member filename length, not in archive structure.
4. Keep the filename content ordinary so string construction uses the declared length.
5. Submit sanitizer crashes that occur after archive enumeration reaches the target import path.

## Negative Memory
- Do not corrupt central-directory fields while testing long names.
- Do not use an empty archive; the importer must enumerate a member.
- Do not switch to raw model bytes when the target path is archive member handling.
