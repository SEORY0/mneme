---
type: causal-policy
title: ILBM Short Bitmap Header Recovery
description: Recover ILBM bitmap-header overreads by keeping the IFF carrier valid and shortening only the bitmap-header payload.
failure_class: wrong_sink
verifier_signal: sanitizer_crash
candidate_family: construct
input_format: ilbm
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong_sink, sanitizer_crash, ilbm, iff, short_chunk]
match_keys: [wrong_sink, sanitizer_crash, ilbm, short_bitmap_header]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For IFF-style ILBM loaders, preserve the envelope and chunk walk until the bitmap-header decoder is selected. The trigger is a bitmap-header chunk whose declared payload is shorter than the fixed header structure copied by the parser.

## Procedure
1. Build a valid IFF-style ILBM carrier.
2. Include the chunk sequence needed to enter bitmap-header decoding.
3. Make the bitmap-header chunk payload shorter than the fixed structure the decoder expects.
4. Keep outer chunk sizes coherent enough for the loader to reach that chunk.
5. Avoid mutating image data while diagnosing bitmap-header overreads.

## Negative Memory
- Do not corrupt the IFF carrier before the bitmap-header chunk.
- Do not overgrow chunks when the invariant is a short fixed-structure read.
- Do not remove the ILBM form selector.
