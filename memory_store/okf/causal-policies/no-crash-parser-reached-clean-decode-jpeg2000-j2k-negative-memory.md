---
type: causal-policy
title: "No Crash Parser Reached Clean Decode Jpeg2000 J2k Negative Memory"
description: "Round 8 negative memory for no_crash with verifier signal parser_reached_clean_decode."
failure_class: "no_crash"
verifier_signal: "parser_reached_clean_decode"
candidate_family: "seed_sweep"
input_format: "jpeg2000-j2k"
harness_convention: "afl-file-wrapper"
vuln_class: "heap-allocation-size-error"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-clean-decode", "jpeg2000-j2k", "negative_memory", "round-8"]
match_keys: ["no_crash", "parser_reached_clean_decode", "jpeg2000-j2k", "afl-file-wrapper", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 8
---
# No Crash Parser Reached Clean Decode Jpeg2000 J2k Negative Memory

## Policy
Treat `no_crash x parser_reached_clean_decode` as a persistent failure basin for `jpeg2000-j2k` under `afl-file-wrapper`. Preserve any reachability it proved, but do not keep mutating the same field basin unless the next verification changes the signal.

## Diagnosed Dead End
- The official J2K seed corpus reached the OpenJPEG codestream parser and decompressor but decoded cleanly. The attempted seeds did not combine HT block decoding with component dimensions and codeblock buffer sizing that violate the allocation-size invariant.

## Format and Harness Gates
- Format: The harness expects a raw JPEG 2000 codestream beginning with the codestream marker and structured marker segments such as image/component sizing and coding style. HT decode behavior depends on coding style and codeblock/component geometry, not on a container wrapper.
- Harness: The AFL-style file wrapper passes the entire file to the OpenJPEG J2K decompression fuzzer. It reads the header, bounds the decode area, and then decodes; no leading selector byte or separate metadata file is used.

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
