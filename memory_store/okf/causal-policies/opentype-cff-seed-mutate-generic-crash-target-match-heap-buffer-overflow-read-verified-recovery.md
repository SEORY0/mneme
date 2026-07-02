---
type: causal-policy
title: "Opentype Cff Seed Mutate Generic Crash Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for opentype-cff keyed by generic_crash x target_match."
failure_class: "generic_crash"
verifier_signal: "target_match"
candidate_family: "seed_mutate"
input_format: "opentype-cff"
harness_convention: "libfuzzer-harfbuzz-shape-fuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "target-match", "opentype-cff", "libfuzzer-harfbuzz-shape-fuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "target-match", "opentype-cff", "libfuzzer-harfbuzz-shape-fuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Opentype Cff Seed Mutate Generic Crash Target Match Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opentype-cff]]
- related harness facts: [[libfuzzer-harfbuzz-shape-fuzzer]]

## Policy
When `opentype-cff` under `[[libfuzzer-harfbuzz-shape-fuzzer]]` produces `target_match` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[opentype-cff]]` through `[[libfuzzer-harfbuzz-shape-fuzzer]]`.
2. Apply the verified recovery: Start from a valid CFF1 seac regression font. Preserve the sfnt envelope and CFF indexes, then change the explicit charset mapping into a compact range charset that still covers the declared glyph population but omits the base or accent SID needed by a composite seac glyph. Keep the CFF table as the final declared font table and use the harness trailer to select a composite glyph for the face/font extents API, forcing seac resolution through the malformed charset.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- OpenType/CFF inputs are complete sfnt fonts with a table directory and a CFF table containing header, Name INDEX, Top DICT INDEX, String INDEX, Global Subrs, charset, Private DICT, and CharStrings. CFF charset format 0 stores explicit SIDs after .notdef; compact range charset formats cover glyphs by SID ranges. seac charstrings resolve base and accent standard-encoding values back through charset SID lookup while computing extents.

## Harness Contract
- The selected HarfBuzz shape fuzzer consumes the whole file as a raw font blob. It creates an hb_face and hb_font, shapes fixed text, copies the final input bytes as UTF-32 text for a second shaping pass, and passes the last UTF-32 word as the glyph/codepoint selector to miscellaneous face/font APIs including glyph extents. There is no FuzzedDataProvider split or leading mode byte.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_mutate.
