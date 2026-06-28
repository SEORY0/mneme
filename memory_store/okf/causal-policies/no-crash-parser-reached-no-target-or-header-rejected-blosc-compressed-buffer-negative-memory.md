---
type: causal-policy
title: "No Crash Parser Reached No Target Or Header Rejected Blosc Compressed Buffer Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal parser_reached_no_target_or_header_rejected."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_or_header_rejected"
candidate_family: "construct_and_seed_mutate"
input_format: "blosc compressed buffer"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-or-header-rejected", "blosc-compressed-buffer", "negative_memory", "round-8"]
match_keys: ["no_crash", "parser_reached_no_target_or_header_rejected", "blosc compressed buffer", "libfuzzer", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Parser Reached No Target Or Header Rejected Blosc Compressed Buffer Negative Memory

## Policy
Treat `no_crash x parser_reached_no_target_or_header_rejected` as a persistent failure basin for `blosc compressed buffer` under `libfuzzer`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- Constructed small Blosc buffers and valid compatibility buffers with compressor-format mutations did not reach the Lizard decompressor bug. The target appears to need a syntactically valid Blosc block whose header selects the Lizard legacy format and whose compressed payload violates a Lizard stream invariant.

## Format and Harness Gates
- Format: The decompression harness expects the Blosc buffer size to agree with the cbytes field and validates nbytes/blocksize before decompression. Compressor selection is encoded in the Blosc header, but merely changing the format bits on a buffer compressed by another codec does not produce a useful Lizard payload.
- Harness: The fuzzer passes raw bytes to the Blosc decompression entrypoint after header validation. There is no external mode selector; the internal Blosc header controls codec and block layout.

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
