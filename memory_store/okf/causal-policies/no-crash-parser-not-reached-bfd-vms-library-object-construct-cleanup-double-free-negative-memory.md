---
type: negative-memory
title: "No Crash Parser Not Reached BFD VMS Library Object Construct Cleanup Double Free Negative Memory"
description: "Round 27 diagnosed persistent failure for no_crash with verifier signal parser_not_reached."
failure_class: "no_crash"
verifier_signal: "parser_not_reached"
candidate_family: "construct"
input_format: "bfd-vms-library-object"
harness_convention: "libfuzzer-bfd"
vuln_class: "cleanup-double-free"
access_scope: generate
success_count: 0
confidence: high
tags: ["no-crash", "parser-not-reached", "bfd-vms-library-object", "libfuzzer-bfd", "construct", "cleanup-double-free", "negative-memory", "round-27"]
match_keys: ["no_crash", "parser_not_reached", "bfd-vms-library-object", "libfuzzer-bfd", "cleanup-double-free", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# No Crash Parser Not Reached BFD VMS Library Object Construct Cleanup Double Free Negative Memory

- key: `no_crash x parser_not_reached`
- outcome: diagnosed persistent failure; avoid repeating this basin without a new gate relation.
- success_count: 0

## Failure Shape
- The archive-only harness never produced a crash from the tried constructions.
- Empty Alpha VMS library headers, library headers with empty index blocks, a one-module library pointing at minimal VMS object records, standalone VMS object records, and a GNU ar wrapper around VMS-looking object records all stayed in the no-crash basin.
- The likely missing gate is a fully recognized Alpha VMS library/member combination that causes BFD target iteration to preserve an alpha-vms match while continuing cleanup.

## Format / Harness Contract
- A VMS library has a fixed-size library header with a library type, a sanity id, a major version, module and symbol counts, and index descriptors.
- Alpha object libraries require the Alpha object or Alpha share-image library type, the Alpha library major version, and two ASCII variable-length indexes.
- VMS object modules are record-based: object records carry a record type and repeated size information, an EMH/MHD-style record starts module metadata, and an EEOM-style record terminates the module.
- Harness [[libfuzzer-bfd]]:
  - The harness writes raw input bytes to a temporary file, opens that file with bfd_openr using the default target, calls bfd_check_format with bfd_archive only, and then closes the BFD.
  - There is no FuzzedDataProvider, selector byte, or checksum.
  - Reaching the described cleanup bug requires BFD archive target probing to recognize a relevant VMS/Alpha archive or archive member during target iteration.

## Policy
Treat `no_crash x parser_not_reached` as a negative-memory key for `bfd-vms-library-object` under `libfuzzer-bfd`. A future candidate needs a different causal relation than the recorded `construct` attempt family, or explicit evidence that the missing parser/sink gate has changed.

## Procedure
1. First re-establish the exact parser or harness gate named by the verifier signal before changing payload scale.
2. If the prior basin was clean execution, search for the narrow branch that reaches the sink rather than sweeping larger mutations.
3. If the prior basin was fixed-image or both-image failure, narrow the mutation until the fixed build rejects or survives before submitting.

## Negative Memory
- Do not repeat the `construct` family against this failure key without a new gate hypothesis.
- Do not keep candidates that are clean, parser-not-reached, fixed-image crashes, or off-target wrapper failures.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one diagnosed round-27 persistent failure.
- Pair with [[bfd-vms-library-object]] and [[libfuzzer-bfd]].
