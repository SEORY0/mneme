---
type: causal-policy
title: "Isobmff MP4 Seed Mutate Parser Reached Heap Use After Free In Sample Entry Teardown Heap Use After Free Verified Recovery"
description: "Round 26 verified recovery for wrong_sink with verifier signal parser_reached_heap_use_after_free_in_sample_entry_teardown."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_heap_use_after_free_in_sample_entry_teardown"
candidate_family: "seed_mutate"
input_format: "isobmff-mp4"
harness_convention: "libfuzzer-file-wrapper"
vuln_class: "heap-use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-heap-use-after-free-in-sample-entry-teardown", "isobmff-mp4", "libfuzzer-file-wrapper", "seed-mutate", "verified-recovery", "round-26"]
match_keys: ["wrong_sink", "parser_reached_heap_use_after_free_in_sample_entry_teardown", "isobmff-mp4", "libfuzzer-file-wrapper", "heap-use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 26
---
# Isobmff MP4 Seed Mutate Parser Reached Heap Use After Free In Sample Entry Teardown Heap Use After Free Verified Recovery

- key: `wrong_sink x parser_reached_heap_use_after_free_in_sample_entry_teardown`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[isobmff-mp4]]
- harnesses: [[libfuzzer-file-wrapper]]

## Failure Shape
Start from a valid MP4 seed with an audio sample entry and preserve the outer BMFF box hierarchy. Wrap the codec descriptor inside a QuickTime-style wave child so the sample entry field points at a nested child, then add a narrowly malformed following child to force audio-sample-entry fallback scanning. The fallback deletes the descriptor through the sample-entry child list even though the wave owner still retains it, and later box teardown reuses the freed child.

## Policy
For `wrong_sink x parser_reached_heap_use_after_free_in_sample_entry_teardown` on `isobmff-mp4`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `seed_mutate` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `isobmff-mp4` carrier and `libfuzzer-file-wrapper` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `isobmff-mp4` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
ISO BMFF boxes use big-endian size and four-character type headers, with container sizes that must remain consistent up the moov/trak/mdia/minf/stbl/stsd chain. Audio sample entries contain fixed sample-entry and audio fields followed by child boxes such as esds or QuickTime wave. A wave child can itself contain codec configuration boxes, and malformed sibling boxes can force the audio sample-entry fallback that scans raw child payload for a descriptor box.

## Harness Contract
The GPAC fuzz harness writes the raw input bytes to a temporary file and opens it with the ISO media reader in dump/read mode. There is no leading mode selector and no FuzzedDataProvider splitting; the payload must be a file-like MP4/BMFF object that reaches gf_isom_open_file.

## Evidence Shape
- Support: 1 server-verified round 26 solve after 9 attempts.
- Scope: generator repair and retargeting only.
