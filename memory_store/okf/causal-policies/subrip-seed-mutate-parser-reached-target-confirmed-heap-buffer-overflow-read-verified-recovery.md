---
type: causal-policy
title: "Subrip Seed Mutate Parser Reached Target Confirmed Heap Buffer Overflow Read Verified Recovery"
description: "Round 15 server-verified recovery for subrip keyed by generic_crash x parser_reached_target_confirmed."
failure_class: "generic_crash"
verifier_signal: "parser_reached_target_confirmed"
candidate_family: "seed_mutate"
input_format: "subrip"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "parser-reached-target-confirmed", "subrip", "libfuzzer", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery", "round-15"]
match_keys: ["generic_crash", "parser_reached_target_confirmed", "subrip", "libfuzzer", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Subrip Seed Mutate Parser Reached Target Confirmed Heap Buffer Overflow Read Verified Recovery

- key: `generic_crash x parser_reached_target_confirmed`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[subrip]]
- related harness facts: [[libfuzzer]]

## Policy
When `subrip` under `libfuzzer` reaches `parser_reached_target_confirmed` from `generic_crash`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Preserve a real SubRip cue envelope so subtitle type detection and cue parsing succeed, then
   mutate cue text to contain malformed closing markup. A broken closing tag followed by another
   malformed closing tag and intervening text drives the markup repair routine into a stale cursor
   adjustment and out-of-bounds read.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- SubRip cues use a numeric cue id, a timestamp range line, one or more text lines, and a blank-line
  cue terminator. The GStreamer parser escapes text, selectively unescapes supported inline tags, and
  then repairs malformed supported closing tags before emitting subtitle text.

## Harness Contract
- The libFuzzer bytes are passed to the GStreamer discoverer target as a file-like input. The file
  must look enough like a subtitle stream for type detection to select SubRip; there is no leading
  selector and no FuzzedDataProvider layout.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: seed_mutate.
