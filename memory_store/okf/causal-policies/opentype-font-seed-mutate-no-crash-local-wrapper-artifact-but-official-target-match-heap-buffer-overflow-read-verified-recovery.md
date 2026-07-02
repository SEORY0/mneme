---
type: causal-policy
title: "Opentype Font Seed Mutate No Crash Local Wrapper Artifact But Official Target Match Heap Buffer Overflow Read Verified Recovery"
description: "Round 34 verified recovery for opentype-font when no_crash pairs with local_wrapper_artifact_but_official_target_match."
failure_class: "no_crash"
verifier_signal: "local_wrapper_artifact_but_official_target_match"
candidate_family: "seed_mutate"
input_format: "opentype-font"
harness_convention: "libfuzzer-harfbuzz-subset"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "local-wrapper-artifact-but-official-target-match", "opentype-font", "libfuzzer-harfbuzz-subset", "seed-mutate", "verified-recovery", "round-34"]
match_keys: ["no-crash", "local-wrapper-artifact-but-official-target-match", "opentype-font", "libfuzzer-harfbuzz-subset", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 34
---
# Opentype Font Seed Mutate No Crash Local Wrapper Artifact But Official Target Match Heap Buffer Overflow Read Verified Recovery

- key: `no_crash x local_wrapper_artifact_but_official_target_match`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer-harfbuzz-subset]]

## Round 34 Verified Support

- key: `no_crash x local_wrapper_artifact_but_official_target_match`
- outcome: server-verified vulnerable/fixed split
- candidate family: `seed_mutate`
- vulnerability class: `heap-buffer-overflow-read`
- related format facts: [[opentype-font]]
- related harness facts: [[libfuzzer-harfbuzz-subset]]

### Policy
When `no_crash x local_wrapper_artifact_but_official_target_match` appears for `opentype-font`, preserve the accepted parser and harness gates, then target the specific state relation that the verifier proved. Treat the official vulnerable-only target match as the success gate; local crash class alone is not enough.

### Procedure
1. Use the [[libfuzzer-harfbuzz-subset]] harness contract and the [[opentype-font]] format contract before changing sink fields.
2. Recreate the verified causal relation: Start from a valid variable OpenType font that is accepted by the subset fuzzer. Keep the sfnt envelope, glyph selection path, layout retention, and variation-item mapping coherent, but mutate a single variation-store region-reference entry inside an HVAR/VVAR-style table so it names a non-existent region. The vulnerable serializer builds a map containing that invalid reference and later uses it while copying VarRegionList axis records; the fixed build rejects or omits the bad mapping and exits cleanly.
3. Keep selectors, lengths, state setup, and container invariants coherent until the target parser state is reached.
4. Submit only when the candidate is expected to preserve the vulnerable/fixed split rather than a generic both-build crash.

### Format Contract
OpenType fonts use an sfnt table directory with independent tagged tables. Variable fonts may carry HVAR, VVAR, or MVAR variation data; those tables reference a VarStore containing a VarRegionList and one or more VarData arrays. A variation item map chooses a VarData outer index and item inner index, while each VarData record has a list of region references that must refer to existing VarRegionList entries. If the item map remains valid but the region-reference list names a missing region, byte-range sanitization can pass and the serializer can later read beyond the available region records during memcpy.

### Harness Contract
The HarfBuzz subset fuzzer treats the input as raw font bytes, creates an hb_face, collects unicodes, then subsets with a built-in text set and layout tables retained. For larger inputs it also reads an optional fixed-size trailer from the end as subset flags plus a replacement codepoint list; those trailer bytes are still part of the blob, so the font envelope must tolerate trailing data. There is no leading selector byte and no FuzzedDataProvider contract. The packaged local verify wrapper can misreport this task as no_crash because it invokes the fuzzer with a file path where its script expects a corpus directory; direct image execution and official submit are the reliable signals.

### Evidence Shape
- Support: one server-verified round 34 solve.
- Candidate family: `seed_mutate`.
- Verifier key: `no_crash x local_wrapper_artifact_but_official_target_match`.
- Vulnerability class: `heap-buffer-overflow-read`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
