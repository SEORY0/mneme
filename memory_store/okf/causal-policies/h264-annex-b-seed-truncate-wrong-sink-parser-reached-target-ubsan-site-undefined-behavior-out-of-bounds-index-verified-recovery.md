---
type: causal-policy
title: "H264 Annex B Seed Truncate Wrong Sink Parser Reached Target Ubsan Site Undefined Behavior Out Of Bounds Index Verified Recovery"
description: "Server-verified recovery for h264-annex-b when wrong_sink pairs with parser_reached_target_ubsan_site."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_ubsan_site"
candidate_family: "seed_truncate"
input_format: "h264-annex-b"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "undefined-behavior-out-of-bounds-index"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-ubsan-site", "h264-annex-b", "libfuzzer-ffmpeg-target-decoder", "seed-truncate", "verified-recovery", "round-33"]
match_keys: ["wrong-sink", "parser-reached-target-ubsan-site", "h264-annex-b", "libfuzzer-ffmpeg-target-decoder", "seed-truncate", "undefined-behavior-out-of-bounds-index", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 33
---
# H264 Annex B Seed Truncate Wrong Sink Parser Reached Target Ubsan Site Undefined Behavior Out Of Bounds Index Verified Recovery

- key: `wrong_sink x parser_reached_target_ubsan_site`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[h264-annex-b]]
- related harness facts: [[libfuzzer-ffmpeg-target-decoder]]

## Policy
When `wrong_sink x parser_reached_target_ubsan_site` appears for `h264-annex-b`, preserve the parser and harness gates that were proven by the verifier before mutating the sink-specific relation. Treat official vulnerable-only target match as the success gate, not a local coarse crash label.

## Procedure
1. Use the `libfuzzer-ffmpeg-target-decoder` harness contract and the `h264-annex-b` format contract before changing sink fields.
2. Recreate the causal relation from the verified trace: A real H.264 Annex-B CAVLC conformance stream was reduced to a compact prefix that preserved the SPS/PPS recognition gates and the beginning of an IDR slice. The preserved slice reaches CAVLC residual decoding with a nonzero coefficient token, causing the vulnerable one-before-array VLC table expression to be evaluated while the fixed build remains clean.
3. Keep lengths, dispatch selectors, structural checks, and state setup coherent until the target parser state is reached.
4. Submit only after the fixed image exits cleanly or rejects the relation while the vulnerable image reaches the target sink.

## Format Contract
Use [[h264-annex-b]]. The input is a raw Annex-B elementary H.264 stream made of start-code-delimited NAL units. Parser reachability depended on coherent SPS and PPS records before an IDR slice; the PPS must select CAVLC entropy coding, and the slice residual syntax is interpreted only after macroblock prediction, coded-block-pattern, and quantizer-delta fields are consistent enough for residual decode.

## Harness Contract
Use [[libfuzzer-ffmpeg-target-decoder]]. The FFmpeg decoder libFuzzer harness passes the file bytes directly to the selected H.264 decoder as packet data. There is no FuzzedDataProvider prefix or mode byte. A fixed packet delimiter can split multiple packets, and inputs above the harness threshold reserve a trailing codec-context configuration block, so the successful family kept the candidate compact.

## Evidence Shape
- Support: 1 server-verified round 33 solve.
- Candidate family: seed_truncate.
- Verifier key: `wrong_sink x parser_reached_target_ubsan_site`.
- Vulnerability class: `undefined-behavior-out-of-bounds-index`.
- Recovery summary: A real H.264 Annex-B CAVLC conformance stream was reduced to a compact prefix that preserved the SPS/PPS recognition gates and the beginning of an IDR slice. The preserved slice reaches CAVLC residual decoding with a nonzero coefficient token, causing the vulnerable one-before-array VLC table expression to be evaluated while the fixed build remains clean.

## Negative Memory
- Do not count parser reachability, both-image crashes, local-only wrapper crashes, clean exits, or fixed-image crashes as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.
