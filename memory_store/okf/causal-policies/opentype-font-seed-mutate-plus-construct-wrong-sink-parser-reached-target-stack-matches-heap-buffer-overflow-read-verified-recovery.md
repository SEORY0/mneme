---
type: causal-policy
title: "Opentype Font Seed Mutate Plus Construct Wrong Sink Parser Reached Target Stack Matches Heap Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for opentype-font keyed by wrong_sink x parser_reached_target_stack_matches."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_stack_matches"
candidate_family: "seed_mutate_plus_construct"
input_format: "opentype-font"
harness_convention: "libfuzzer-harfbuzz-shape-fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-stack-matches", "opentype-font", "libfuzzer-harfbuzz-shape-fuzzer", "seed-mutate-plus-construct", "heap-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-target-stack-matches", "opentype-font", "libfuzzer-harfbuzz-shape-fuzzer", "seed-mutate-plus-construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Opentype Font Seed Mutate Plus Construct Wrong Sink Parser Reached Target Stack Matches Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_stack_matches`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer-harfbuzz-shape-fuzzer]]

## Policy
When `opentype-font` under `[[libfuzzer-harfbuzz-shape-fuzzer]]` produces `parser_reached_target_stack_matches` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[opentype-font]]` through `[[libfuzzer-harfbuzz-shape-fuzzer]]`.
2. Apply the verified recovery: Start from a real sfnt/OpenType seed that shapes ordinary text. Preserve the table directory and glyph mapping, but make the classic kern path win over GPOS kerning. Add a terminal horizontal kern version-0 format-3 subtable whose declared glyph-class span covers the shaped glyph ids while the physical class-array payload is intentionally truncated. The vulnerable format-3 code trusts the declared class span and reads past the backing table during kerning; the fixed build rejects or bounds this condition.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- A usable OpenType input is a whole sfnt font with a valid table directory, table records, and enough cmap/metrics/glyph structure for HarfBuzz to map shaped text to glyph ids. The classic kern table has a version/count header followed by subtable wrappers; format 3 contains glyphCount, kernValueCount, left/right class counts, kern values, left class bytes, right class bytes, and a class-pair index array. In the vulnerable source, the format-3 sanitizer does not validate that the variable arrays physically cover the declared counts.

## Harness Contract
- The hb-shape libFuzzer harness consumes the raw input bytes as an hb_blob font with no leading selector and no FuzzedDataProvider carving. It shapes fixed ASCII text first, and for larger inputs also interprets trailing bytes as UTF-32 text. Classic kern application depends on HarfBuzz selecting the kern table during shaping rather than a GPOS kern feature.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_mutate_plus_construct.
