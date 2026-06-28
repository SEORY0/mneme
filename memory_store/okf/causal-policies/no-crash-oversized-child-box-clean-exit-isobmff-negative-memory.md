---
type: causal-policy
title: "No Crash Oversized Child Box Clean Exit Isobmff Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal oversized_child_box_clean_exit."
failure_class: "no_crash"
verifier_signal: "oversized_child_box_clean_exit"
candidate_family: "construct_then_seed_mutate"
input_format: "isobmff"
harness_convention: "libfuzzer-afl-file-wrapper"
vuln_class: "missing-invalid-file-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "oversized-child-box-clean-exit", "isobmff", "negative_memory", "round-8"]
match_keys: ["no_crash", "oversized_child_box_clean_exit", "isobmff", "libfuzzer-afl-file-wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Oversized Child Box Clean Exit Isobmff Negative Memory

## Policy
Treat `no_crash x oversized_child_box_clean_exit` as a persistent failure basin for `isobmff` under `libfuzzer-afl-file-wrapper`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- The oversized child-box relation was reached repeatedly: constructed containers and a mutated in-repo MP4 seed produced the parser warning that a child box was larger than its container, but the vulnerable build only logged invalid sizing or missing movie-header diagnostics and exited cleanly. Adding a minimal movie header and mutating a real MP4 preserved parser reachability but still did not turn the missing-error condition into a sanitizer crash or official target match.

## Format and Harness Gates
- Format: ISOBMFF boxes use a big-endian size followed by a four-character type. Container boxes such as moov contain child boxes whose declared sizes are counted against the parent remaining size. A valid MP4-family envelope normally starts with an ftyp box and a moov box; the moov box usually contains an mvhd movie header before track or metadata children.
- Harness: The fuzz target writes the raw input bytes to a temporary file and calls gf_isom_open_file in read-dump mode, then closes the movie if opening succeeds. The input is a complete file image; there is no selector byte or FuzzedDataProvider carving.

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
