---
type: causal-policy
title: "Ffmpeg Dvbsub Packet Stream Construct Parser Reached Clut Entry Index Oob Out Of Bounds Index Write Verified Recovery"
description: "Round 20 verified recovery for wrong_sink with verifier signal parser_reached_clut_entry_index_oob."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_clut_entry_index_oob"
candidate_family: "construct"
input_format: "ffmpeg-dvbsub-packet-stream"
harness_convention: "libfuzzer-ffmpeg-target-decoder"
vuln_class: "out-of-bounds-index-write"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-clut-entry-index-oob", "ffmpeg-dvbsub-packet-stream", "libfuzzer-ffmpeg-target-decoder", "construct", "verified-recovery", "round-20"]
match_keys: ["wrong-sink", "parser-reached-clut-entry-index-oob", "ffmpeg-dvbsub-packet-stream", "libfuzzer-ffmpeg-target-decoder", "out-of-bounds-index-write"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 20
---
# Ffmpeg Dvbsub Packet Stream Construct Parser Reached Clut Entry Index Oob Out Of Bounds Index Write Verified Recovery

- key: `wrong_sink x parser_reached_clut_entry_index_oob`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[ffmpeg-dvbsub-packet-stream]]
- harnesses: [[libfuzzer-ffmpeg-target-decoder]]

## Failure Shape
Build a target-decoder packet stream containing a DVB subtitle CLUT segment with valid segment framing and length accounting. The parser gate is the subtitle sync marker, segment type, page id, and CLUT version/body layout. Trigger by selecting a CLUT entry identifier outside the low-depth table while still providing the color-component fields required for that entry form, so the decoder reaches the table update and violates the entry-index invariant.

## Policy
For `wrong_sink x parser_reached_clut_entry_index_oob` on `ffmpeg-dvbsub-packet-stream`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `ffmpeg-dvbsub-packet-stream` carrier enough for the `libfuzzer-ffmpeg-target-decoder` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `ffmpeg-dvbsub-packet-stream` recognition gate while retargeting this signal.
- Do not treat off-target crashes or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified round 20 solve.
- Scope: generator repair only.
