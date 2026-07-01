---
type: causal-policy
title: "Jpeg2000 Jp2 J2k Seed Mutate And Construct No Crash Parser Not Reached Or Clean Exit Integer Overflow To Invalid Memory Access Negative Memory"
description: "Round 34 negative memory for jpeg2000-jp2-j2k when no_crash pairs with parser_not_reached_or_clean_exit."
failure_class: "no_crash"
verifier_signal: "parser_not_reached_or_clean_exit"
candidate_family: "seed_mutate_and_construct"
input_format: "jpeg2000-jp2-j2k"
harness_convention: "libfuzzer"
vuln_class: "integer-overflow-to-invalid-memory-access"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-not-reached-or-clean-exit", "jpeg2000-jp2-j2k", "libfuzzer", "seed-mutate-and-construct", "negative-memory", "round-34"]
match_keys: ["no-crash", "parser-not-reached-or-clean-exit", "jpeg2000-jp2-j2k", "libfuzzer", "seed-mutate-and-construct", "integer-overflow-to-invalid-memory-access", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 34
---
# Jpeg2000 Jp2 J2k Seed Mutate And Construct No Crash Parser Not Reached Or Clean Exit Integer Overflow To Invalid Memory Access Negative Memory

- key: `no_crash x parser_not_reached_or_clean_exit`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[jpeg2000-jp2-j2k]]
- related harness facts: [[libfuzzer]]

## Round 34 Negative Support

- key: `no_crash x parser_not_reached_or_clean_exit`
- outcome: persistent failure / basin to avoid
- candidate family: `seed_mutate_and_construct`
- vulnerability class: `integer-overflow-to-invalid-memory-access`
- related format facts: [[jpeg2000-jp2-j2k]]
- related harness facts: [[libfuzzer]]

### Failure Shape
Valid JP2/J2K seeds and constructed codestreams reached only clean rejection or clean exit. Attempts covered known regression-seed replay, POC-bearing corpus seeds, sparse high-component geometry intended to wrap packet-iterator stride arithmetic, saturated packet-data variants, and many-resolution stride overflow. The remaining missing relation appears to be a decodable packet/tile state that reaches tier-two packet iteration after the pi arithmetic changes, rather than just header geometry.

### Policy
Treat `no_crash x parser_not_reached_or_clean_exit` on `jpeg2000-jp2-j2k` as a basin to avoid unless a new candidate changes the parser gate, state relation, harness contract, or target sink relation described below. Preserve any proven reachability, but reject variants that return to the same signal without changing the causal gate under test.

### Procedure
1. Keep only the smallest parser or harness envelope that was actually reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. Promote a recovery from this basin only after a later verifier-confirmed target match.

### Format Contract
The input can be a raw JPEG 2000 codestream selected by the codestream marker or a JP2 container selected by the signature-box layout. Header parsing consumes SIZ image and component geometry, COD coding-style/progression/layer/resolution/precinct settings, QCD quantization data, optional POC progression-order changes, and SOT/SOD tile-part data. The SIZ component table has a parser cap below the theoretical marker-size maximum, and COD precinct-size bytes are present only when the coding-style precinct flag is set.

### Harness Contract
The fuzz harness consumes the whole file as raw bytes through OpenJPEG memory-stream callbacks. There is no leading mode byte or FuzzedDataProvider layout. It selects J2K versus JP2 from the initial signature, reads the image header, caps the requested decode area internally, then calls the normal decoder path.

### Evidence Shape
- Support: one diagnosed persistent round 34 failure.
- Candidate family: `seed_mutate_and_construct`.
- Verifier key: `no_crash x parser_not_reached_or_clean_exit`.
- Vulnerability class: `integer-overflow-to-invalid-memory-access`.

## Negative Memory
- Do not count parser reachability, both-image crashes, fixed-image crashes, local wrapper crashes, clean exits, or off-target sanitizer crashes as success for this key.
- Do not store concrete payload bytes, exact positions, task identifiers, checksums, or submit metadata.
