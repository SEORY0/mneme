---
type: causal-policy
title: "Opentype Font Seed Mutate Wrong Sink Parser Reached Target Stack Path In Coverage Serialization Stack Use After Return Read Verified Recovery"
description: "Server-verified recovery for opentype-font when wrong_sink pairs with parser_reached_target_stack_path_in_coverage_serialization."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack_path_in_coverage_serialization"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer-harfbuzz-subset"
vuln_class: "stack-use-after-return-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack-path-in-coverage-serialization", "opentype-font", "libfuzzer-harfbuzz-subset", "seed-mutate", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-target-stack-path-in-coverage-serialization", "opentype-font", "libfuzzer-harfbuzz-subset", "seed-mutate", "stack-use-after-return-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Opentype Font Seed Mutate Wrong Sink Parser Reached Target Stack Path In Coverage Serialization Stack Use After Return Read Verified Recovery

- key: `wrong_sink x parser_reached_target_stack_path_in_coverage_serialization`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer-harfbuzz-subset]]

## Policy
When `wrong_sink x parser_reached_target_stack_path_in_coverage_serialization` appears for `opentype-font`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-harfbuzz-subset` harness contract and the `opentype-font` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Start from a valid OpenType font whose GSUB table contains a SingleSubst lookup with a uniform glyph delta. Preserve the sfnt envelope and add the subset-fuzzer trailer so the harness-selected text includes glyphs covered by that substitution. With layout retained by the harness flags, subsetting chooses the compact SingleSubst serialization path and serializes a mapped coverage iterator whose lifetime is invalid.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[opentype-font]]. OpenType fonts use an sfnt table directory with independent tables such as cmap and GSUB. A GSUB SingleSubst lookup maps covered glyphs by either a uniform delta or explicit substitutes; preserving the font envelope and selecting covered codepoints lets the subsetter rebuild the affected lookup. Extra trailing bytes are tolerated by the font parser and can still be consumed by the fuzz harness as control data.

## Harness Contract
Use [[libfuzzer-harfbuzz-subset]]. The HarfBuzz subset libFuzzer target treats the input as raw font bytes for the hb_blob. When enough bytes are present, a fixed-size tail trailer is also carved from the same input: a flags byte immediately before a small array of native-endian codepoints. There is no leading mode selector or FuzzedDataProvider split.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: seed_mutate.
- Verifier key: `wrong_sink x parser_reached_target_stack_path_in_coverage_serialization`.
- Vulnerability class: `stack-use-after-return-read`.
- Recovery summary: Start from a valid OpenType font whose GSUB table contains a SingleSubst lookup with a uniform glyph delta. Preserve the sfnt envelope and add the subset-fuzzer trailer so the harness-selected text includes glyphs covered by that substitution. With layout retained by the harness flags, subsetting chooses the compact SingleSubst serialization path and serializes a mapped coverage iterator whose lifetime is invalid.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
