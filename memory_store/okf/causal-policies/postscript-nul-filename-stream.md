---
type: causal-policy
title: PostScript NUL Filename Stream Recovery
description: Failure-keyed recovery for PostScript stream operation crashes caused by a decoded empty-leading filename object.
failure_class: generic_crash
verifier_signal: sanitizer_crash
candidate_family: construct
input_format: postscript
harness_convention: libfuzzer
vuln_class: null-pointer-dereference
access_scope: generate
success_count: 1
confidence: medium
tags: [generic_crash, sanitizer_crash, postscript, filename_decode, stream_operation]
match_keys: [generic_crash, sanitizer_crash, postscript, filename_decode, stream_operation]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For PostScript file or stream tasks, a crash may require a syntactically valid program where filename decoding produces a logically unusable object while the source string remains non-empty. The recovery is to preserve program validity and immediately consume the opened object through a stream operation.

## Procedure
1. Build a minimal valid PostScript program rather than a raw fragment.
2. Put the malformed condition inside the filename string decoding path.
3. Keep the string non-empty at the language level while making the decoded first character unusable for the lower stream layer.
4. Invoke a stream operation immediately so the broken open result is dereferenced before unrelated interpreter cleanup.
5. Avoid large programs; a compact open-then-stream sequence gives the verifier the clearest signal.

## Negative Memory
- Do not mutate PDF wrappers for this shape; the causal gate is PostScript filename decoding.
- Do not rely on undefined operators or syntax errors, which stop before the stream object path.
- Do not add unrelated file-system paths or environment-specific names.

## Evidence Shape
- Support: 1 server-verified round observation.
- Scope: generator repair for PostScript filename and stream-object bugs.
