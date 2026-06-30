---
type: negative-memory
title: "No Crash Packed And Dynamic ELF DT Hash Rejected Or Timeout Not Target UPX Packed ELF Seed Mutate Invalid DT Hash Handling Negative Memory"
description: "Round 26 negative memory for no_crash with verifier signal packed_and_dynamic_elf_dt_hash_rejected_or_timeout_not_target."
failure_class: "no_crash"
verifier_signal: "packed_and_dynamic_elf_dt_hash_rejected_or_timeout_not_target"
candidate_family: "seed_mutate"
input_format: "upx-packed-elf"
harness_convention: "libfuzzer-file-command-wrapper"
vuln_class: "invalid-dt-hash-handling"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "packed-and-dynamic-elf-dt-hash-rejected-or-timeout-not-target", "upx-packed-elf", "libfuzzer-file-command-wrapper", "seed-mutate", "negative-memory", "round-26"]
match_keys: ["no_crash", "packed_and_dynamic_elf_dt_hash_rejected_or_timeout_not_target", "upx-packed-elf", "libfuzzer-file-command-wrapper", "invalid-dt-hash-handling", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 26
---
# No Crash Packed And Dynamic ELF DT Hash Rejected Or Timeout Not Target UPX Packed ELF Seed Mutate Invalid DT Hash Handling Negative Memory

- key: `no_crash x packed_and_dynamic_elf_dt_hash_rejected_or_timeout_not_target`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[upx-packed-elf]]
- related harness facts: [[libfuzzer-file-command-wrapper]]

## Failure Shape
The successful reachability gate was a real UPX-packed Linux shared-object carrier built from the local corpus with the local UPX source build. Plain dynamic ELF inputs reached only a not-packed rejection, while packed main-program seeds unpacked cleanly but did not expose the target dynamic hash relation. Mutating DT_HASH bucket counts, dynamic table ordering, selected bucket values, chain placement, and a self-cycling chain produced clean CantUnpackException paths or a rejected timeout, not a target sanitizer crash.

## Policy
Treat `no_crash x packed_and_dynamic_elf_dt_hash_rejected_or_timeout_not_target` on `upx-packed-elf` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described below. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, wrapper-mismatch, or both-image-crash basin.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `packed_and_dynamic_elf_dt_hash_rejected_or_timeout_not_target` basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `packed_and_dynamic_elf_dt_hash_rejected_or_timeout_not_target`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, usage banners, clean exits, or fixed-image crashes as success.
- Never store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
UPX packed ELF inputs are complete ELF files with normal ELF headers plus UPX loader and overlay metadata. Main executable packed seeds may have no section table and no dynamic section in the packed carrier. Packed shared-object carriers can preserve a clear PT_DYNAMIC segment with DT_HASH, DT_GNU_HASH, DT_STRTAB, and DT_SYMTAB entries while compressed payload blocks contain the original file data. SYSV DT_HASH begins with bucket and chain counts followed by bucket and chain arrays; UPX also derives table extents from dynamic table ordering when section headers are unavailable.

## Harness Contract
The active runner used the decompression fuzzer: it writes raw input bytes to a temporary file and invokes the UPX decompression command path with an output file argument, then deletes both temporary files. The input must be accepted as UPX-packed before the unpacker runs; ordinary ELF files are reported as not packed. There is no FuzzedDataProvider carving or mode selector in the bytes.

## Evidence Shape
- Support: 1 diagnosed persistent failure from round 26 after 15 attempts.
- Scope: generator repair and basin avoidance only.
