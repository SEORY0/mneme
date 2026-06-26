---
type: causal-policy
title: GIF Interlace Pass Table Read Recovery
description: Verified recovery for wrong_sink with sanitizer_crash on gif inputs.
failure_class: wrong_sink
verifier_signal: sanitizer_crash
candidate_family: construct
input_format: gif
harness_convention: libfuzzer
vuln_class: global-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, sanitizer-crash, construct, gif, global-buffer-overflow-read, verified-recovery]
match_keys: [wrong-sink, sanitizer-crash, gif, global-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# GIF Interlace Pass Table Read Recovery

- key: `wrong_sink x sanitizer_crash`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[gif]]

## Failure Shape
Use a syntactically valid GIF envelope with a minimal palette and an interlaced image. The
image data is long enough for decoding to advance beyond the expected interlace passes,
violating the invariant that the pass index stays within the fixed interlace row-
offset/stride tables.

## Policy
For `wrong_sink x sanitizer_crash` on `gif`, preserve the parser and harness gate first, then mutate
only the causal invariant described by the verified trace. Prefer the candidate family `construct`
when the carrier is available because this shape was server-confirmed against vulnerable and fixed
builds.

## Procedure
1. Preserve a syntactically valid GIF header, screen descriptor, and palette relationship.
2. Select interlaced image decoding so the parser enters the pass row-offset and stride table
path.
3. Keep the image compact but provide enough image data for decoding to advance beyond the
expected interlace passes.
4. Retarget wrong-sink sanitizer crashes by shrinking unrelated metadata and preserving only
the interlace pass invariant.

## Verifier Contract
The local signal may remain coarse. Keep candidates that reach the named parser or sink and
use the official vulnerable-versus-fixed comparison as the target-match gate.

## Negative Memory
- Do not corrupt the GIF magic or palette count while trying to reach interlace decoding.
- Do not rely on trailing bytes after the image terminator; the sink is in decoded image
traversal.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve.
- Scope: generator repair only.
