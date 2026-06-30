---
type: negative-memory
title: "Generic Crash Parser Reached But Fixed Build Not Clean Official Rejected Miff Negative Memory"
description: "Round 28 negative memory for generic_crash with verifier signal parser_reached_but_fixed_build_not_clean_official_rejected."
failure_class: "generic_crash"
verifier_signal: "parser_reached_but_fixed_build_not_clean_official_rejected"
candidate_family: "construct"
input_format: "miff"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["generic-crash", "parser-reached-but-fixed-build-not-clean-official-rejected", "miff", "libfuzzer", "construct", "use-of-uninitialized-value", "negative-memory", "round-28"]
match_keys: ["generic_crash", "parser_reached_but_fixed_build_not_clean_official_rejected", "miff", "libfuzzer", "use-of-uninitialized-value", "negative_memory", "construct", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 28
---
# Generic Crash Parser Reached But Fixed Build Not Clean Official Rejected Miff Negative Memory

- key: `generic_crash x parser_reached_but_fixed_build_not_clean_official_rejected`
- outcome: negative memory
- success_count: 0
- failure_count: 1
- formats: [[miff]]
- harnesses: [[libfuzzer]]

## Dead-End Shape
The successful parser envelope was a MIFF header selecting Zip compression and the version-dependent deflate reader. Empty or underfilled deflate streams reached the vulnerable reader and often produced local uninitialized-use or generic crashes, but the same malformed family also made the fixed build exit non-clean under official comparison. Version-zero continuous streams, documented length-prefixed Zip chunks, PseudoClass index imports, DirectClass imports, multi-image pushback carriers, and a raw short-payload MIFF control did not produce a stable vulnerable-only official target match.

## Policy
For `generic_crash x parser_reached_but_fixed_build_not_clean_official_rejected` on `miff`, avoid replaying the observed dead end. This negative memory is co-equal with positive policies and should redirect generation before another official submission. Treat `construct` as useful only if it changes the missing gate, state relation, or sink path.

## Procedure
1. When this failure key repeats, preserve only the descriptive reachability facts and retarget the missing invariant before another official submission.
2. Do not spend attempts on candidates that are clean, rejected before the target path, fixed-build-crashing, or wrapper-only reproductions in this same shape.
3. Prefer a different construction family or a deeper harness/format contract when the verifier signal repeats without new parser-depth evidence.

## Format Contract
- Format [[miff]]: MIFF uses an ASCII key-value header with id, class, dimensions, depth, optional colors, optional colorspace, and compression attributes, followed by a header terminator and then binary payload. PseudoClass images carry a colormap before pixel data; DirectClass RGB derives row bytes from width, depth, matte state, and colorspace. In the Zip reader, version-zero inputs are handled as a continuous zlib stream with a computed per-row read budget, while later Zip form uses length-prefixed compressed chunks. The reader imports a row after inflate reports stream end even when the output row is underfilled, which can leave the import buffer partly or wholly uninitialized.
- Harness [[libfuzzer]]: The GraphicsMagick MIFF coder fuzzer passes the raw libFuzzer bytes directly as a Magick blob, forces the MIFF coder name, reads the image, catches Magick exceptions, and then writes the decoded image back to a MIFF blob when reading succeeds. There is no leading mode byte, no file carving, and no FuzzedDataProvider split; read-side corruption that still returns an image can surface later in the write-back path.

## Negative Memory
- Do not promote this trace as a recovery unless a later verifier run flips the target relation.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.
- Preserve descriptive format and harness facts separately from this causal negative policy.

## Evidence Shape
- Support: one diagnosed round-28 persistent failure.
- Scope: generator repair and retargeting only.
