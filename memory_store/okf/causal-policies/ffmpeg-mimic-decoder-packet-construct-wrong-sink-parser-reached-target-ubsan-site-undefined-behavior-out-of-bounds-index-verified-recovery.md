---
type: causal-policy
title: "Ffmpeg Mimic Decoder Packet Construct Wrong Sink Parser Reached Target Ubsan Site Undefined Behavior Out Of Bounds Index Verified Recovery"
description: "Server-verified recovery for ffmpeg-mimic-decoder-packet when wrong_sink pairs with parser_reached_target_ubsan_site."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_ubsan_site"
candidate_family: "construct"
input_format: "ffmpeg-mimic-decoder-packet"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "undefined-behavior-out-of-bounds-index"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-ubsan-site", "ffmpeg-mimic-decoder-packet", "libfuzzer-ffmpeg-target-decoder", "construct", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-target-ubsan-site", "ffmpeg-mimic-decoder-packet", "libfuzzer-ffmpeg-target-decoder", "construct", "undefined-behavior-out-of-bounds-index", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# Ffmpeg Mimic Decoder Packet Construct Wrong Sink Parser Reached Target Ubsan Site Undefined Behavior Out Of Bounds Index Verified Recovery

- key: `wrong_sink x parser_reached_target_ubsan_site`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[ffmpeg-mimic-decoder-packet]]
- related harness facts: [[libfuzzer-ffmpeg-target-decoder]]

## Policy
When `wrong_sink x parser_reached_target_ubsan_site` appears for `ffmpeg-mimic-decoder-packet`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-ffmpeg-target-decoder` harness contract and the `ffmpeg-mimic-decoder-packet` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: Construct a raw Mimic decoder packet that satisfies the frame-header gates for an accepted keyframe geometry and a nonzero coefficient stream. In the compressed body, use a VLC symbol whose decoded class asks for a follow-on residual index wider than the lookup row, then provide a minimally out-of-range residual value. Padding the compressed body enough for the decoder's word-swap bitreader is necessary; otherwise the same logical bit pattern can stop before the vulnerable lookup.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[ffmpeg-mimic-decoder-packet]]. Mimic packets for this decoder start with decoder-local numeric frame fields such as quality, dimensions, prediction mode, and coefficient count, followed by a compressed coefficient bitstream. The body is byte-swapped in word-sized chunks before MSB-first bit parsing. VLC symbols encode both run-position movement and how many residual bits are consumed for the next lookup.

## Harness Contract
Use [[libfuzzer-ffmpeg-target-decoder]]. The FFmpeg target decoder harness feeds the file bytes as raw packet data for the selected decoder. It may split tagged multi-packet inputs, but this task can be reached with a single raw packet and does not use FuzzedDataProvider front/back carving. The container wrapper consumes the mounted poc path implicitly.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: construct.
- Verifier key: `wrong_sink x parser_reached_target_ubsan_site`.
- Vulnerability class: `undefined-behavior-out-of-bounds-index`.
- Recovery summary: Construct a raw Mimic decoder packet that satisfies the frame-header gates for an accepted keyframe geometry and a nonzero coefficient stream. In the compressed body, use a VLC symbol whose decoded class asks for a follow-on residual index wider than the lookup row, then provide a minimally out-of-range residual value. Padding the compressed body enough for the decoder's word-swap bitreader is necessary; otherwise the same logical bit pattern can stop before the vulnerable lookup.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
