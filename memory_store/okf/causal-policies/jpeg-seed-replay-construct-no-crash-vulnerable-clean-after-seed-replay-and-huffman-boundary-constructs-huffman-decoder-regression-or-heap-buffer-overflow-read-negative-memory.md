---
type: "negative-memory"
title: "Jpeg Seed Replay Construct No Crash Vulnerable Clean After Seed Replay And Huffman Boundary Constructs Huffman Decoder Regression Or Heap Buffer Overflow Read Negative Memory"
description: "Round 38 negative memory for no_crash with verifier signal vulnerable_clean_after_seed_replay_and_huffman_boundary_constructs."
failure_class: "no_crash"
verifier_signal: "vulnerable_clean_after_seed_replay_and_huffman_boundary_constructs"
candidate_family: "seed_replay+construct"
input_format: "jpeg"
harness_convention: "libfuzzer"
vuln_class: "huffman-decoder-regression-or-heap-buffer-overflow-read"
access_scope: "generate"
success_count: 0
failure_count: 1
confidence: "medium"
tags: ["no-crash", "vulnerable-clean-after-seed-replay-and-huffman-boundary-constructs", "jpeg", "libfuzzer", "seed-replay-construct", "huffman-decoder-regression-or-heap-buffer-overflow-read", "negative-memory", "round-38"]
match_keys: ["no_crash", "vulnerable_clean_after_seed_replay_and_huffman_boundary_constructs", "jpeg", "libfuzzer", "huffman-decoder-regression-or-heap-buffer-overflow-read", "negative-memory", "seed_replay+construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "medium"
train_only: true
round: 38
---
# Jpeg Seed Replay Construct No Crash Vulnerable Clean After Seed Replay And Huffman Boundary Constructs Huffman Decoder Regression Or Heap Buffer Overflow Read Negative Memory

- key: `no_crash x vulnerable_clean_after_seed_replay_and_huffman_boundary_constructs`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Valid JPEG seeds and constructed minimal JPEGs reached or were accepted by the wrapper but did not produce a vulnerable-image sanitizer exit. Attempts covered in-repository decompressor bug seeds, long Huffman-code tables, stuffed and unstuffed marker-like entropy, invalid long-code fallback, and AC symbols using the maximum byte value while preserving marker, table, frame, and scan gates.

## Observed Basin
- Failure trajectory classes: no_crash.
- Official confirmation: no server target match for this basin.

## Policy
Treat `no_crash x vulnerable_clean_after_seed_replay_and_huffman_boundary_constructs` on `[[jpeg]]` under `[[libfuzzer]]` as a basin to avoid unless a new candidate changes the parser gate, state relation, or sink relation described above. Preserve any proven reachability, but reject variants that return to the same clean-exit, off-target-crash, wrapper-mismatch, usage-only, timeout, both-image-crash, or fixed-image-crash behavior.

## Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing relation from the verifier signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same `vulnerable_clean_after_seed_replay_and_huffman_boundary_constructs` basin.
4. Promote a recovery from this basin only after a later official target match.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `vulnerable_clean_after_seed_replay_and_huffman_boundary_constructs`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, timeouts, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 38 after 101 attempts.
- Candidate family: seed_replay+construct.
- Scope: generator repair and basin avoidance only.
