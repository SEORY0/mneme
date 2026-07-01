---
type: causal-policy
title: "Opentype Aat Mort Font Seed Mutate Construct Wrong Sink Parser Reached Heap Buffer Overflow Read Verified Recovery"
description: "Round 32 server-verified recovery for opentype-aat-mort-font keyed by wrong_sink x parser_reached."
failure_class: "wrong_sink"
verifier_signal: "parser_reached"
candidate_family: "seed_mutate_construct"
input_format: "opentype-aat-mort-font"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached", "opentype-aat-mort-font", "libfuzzer", "seed-mutate-construct", "heap-buffer-overflow-read", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached", "opentype-aat-mort-font", "libfuzzer", "seed-mutate-construct", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Opentype Aat Mort Font Seed Mutate Construct Wrong Sink Parser Reached Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[opentype-aat-mort-font]]
- related harness facts: [[libfuzzer]]

## Policy
When `opentype-aat-mort-font` under `[[libfuzzer]]` produces `parser_reached` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[opentype-aat-mort-font]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Start from a valid in-repo AAT contextual font seed so the sfnt directory, cmap, glyph data, and shaping path are accepted. Remove the extended AAT substitution table so the obsolete AAT substitution table is selected, then add a compact obsolete contextual subtable whose state machine sanitizes but whose declared subtable body ends before the substitution-table offset field. Shape-time construction of the contextual driver reads that missing offset field in the vulnerable build; the fixed build rejects the incomplete contextual table.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- AAT mort/morx inputs are complete sfnt fonts with normal table records. HarfBuzz prefers the extended AAT substitution table when present and falls back to the obsolete table only when the extended table is absent, so a mort-targeting PoC must ensure the obsolete table is the selected AAT substitution source. A mort table contains a table header, one or more chains, chain feature records, and chain subtables. A contextual subtable embeds an obsolete state table followed by a substitution-table offset field. The obsolete state table can be made sanitizable with a degenerate class/state arrangement even when the contextual subtable body omits the later substitution-table offset field.

## Harness Contract
- The active binary is HarfBuzz hb-shape-fuzzer. It treats the entire PoC as raw font bytes, creates an hb_blob, hb_face, and hb_font, shapes fixed ASCII text, then uses trailing input bytes as UTF-32 text for a second shaping pass before running miscellaneous face APIs. There is no pcap/archive wrapper and no FuzzedDataProvider split.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: seed_mutate_construct.
