---
type: causal-policy
title: "No Crash Sequence File Processed Without Aux Target Sam Bam Cram Sequence Data Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal sequence_file_processed_without_aux_target."
failure_class: "no_crash"
verifier_signal: "sequence_file_processed_without_aux_target"
candidate_family: "construct"
input_format: "sam/bam/cram sequence data"
harness_convention: "libfuzzer"
vuln_class: "out-of-bounds-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "sequence-file-processed-without-aux-target", "sam-bam-cram-sequence-data", "negative_memory", "round-8"]
match_keys: ["no_crash", "sequence_file_processed_without_aux_target", "sam/bam/cram sequence data", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Sequence File Processed Without Aux Target Sam Bam Cram Sequence Data Negative Memory

## Policy
Treat `no_crash x sequence_file_processed_without_aux_target` as a persistent failure basin for `sam/bam/cram sequence data` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Malformed SAM aux text was rejected before BAM aux iteration, and minimal BAM records with empty or truncated aux payloads processed without triggering the vulnerable lookup path. The missing trigger is likely a later view/conversion path that calls aux lookup for a specific tag while the record has an incomplete tag at the end.

## Format and Harness Gates
- Format: Text SAM aux fields must include tag, type, and value syntax or they are rejected early. Binary BAM can carry read records with qname, cigar, sequence, qualities, and trailing aux bytes; aux iteration starts after those variable-length fields.
- Harness: The hts_open fuzzer reads raw file bytes through the HTS memory-file interface and dispatches by file signature. BAM needs a valid binary header and record envelope; there is no separate mode selector.

## Procedure
1. Before retrying this basin, rebuild the carrier around the exact harness contract and confirm parser reachability.
2. Replace the failed mutation family with a more specific invariant that would change the verifier signal.
3. Avoid broad seed mutation, oversized mutation, or off-target crash chasing when this same signal recurs.

## Negative Memory
- Do not promote this basin into a recovery policy until an official vulnerable/fixed verifier target match is observed.
- Do not preserve raw bytes, offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-8 persistent failure trace.
- Scope: generator avoidance and retargeting for the same failure key.
