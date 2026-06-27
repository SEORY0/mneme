---
type: causal-policy
title: "No Crash Parser Reached No Target Crash HLS M3u8 Playlist Text Negative Memory"
description: "Round 9 negative memory for no_crash with verifier signal parser_reached_no_target_crash."
failure_class: "no_crash"
verifier_signal: "parser_reached_no_target_crash"
candidate_family: "construct"
input_format: "HLS M3U8 playlist text"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "parser-reached-no-target-crash", "hls-m3u8-playlist-text", "negative-memory", "round-9"]
match_keys: ["no_crash", "parser_reached_no_target_crash", "HLS M3U8 playlist text", "libfuzzer", "heap-buffer-overflow", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 9
---
# No Crash Parser Reached No Target Crash HLS M3u8 Playlist Text Negative Memory

- key: `no_crash x parser_reached_no_target_crash`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[hls-m3u8-playlist-text]]
- related harness facts: [[libfuzzer]]

## Failure Shape
- Structured HLS playlists reached GPAC's M3U8/DASH parser and filter graph, including key, map,
  media, part, byte-range, long-codec, and long-URI families, but they produced graceful parser or
  filter setup errors.
- Some master-playlist variants spent time in unresolved child-playlist retries rather than target
  parsing.
- The missing trigger is likely a broken low-latency or partial-segment attribute combination that
  is still accepted as a media playlist and then overflows during deeper analysis.

## Policy
Treat `no_crash x parser_reached_no_target_crash` on `HLS M3U8 playlist text` as a basin to avoid unless a new candidate changes the parser gate, state relation, or official target sink. Preserve any proven reachability, but reject variants that return to the same verifier signal without changing the causal gate under test.

## Procedure
1. Keep only the smallest parser or harness envelope that the verifier proved was reached.
2. Identify the missing causal relation from the signal: parser selection, container acceptance, length relation, stateful subobject, allocation state, or official target sink.
3. Change one relation at a time and discard candidates that return to the same clean-exit, off-target-crash, wrong-sink, usage-only, or both-image-crash basin.
4. If a local crash is not an official target match, shrink or discard it before mutating deeper fields.
5. Promote a recovery from this basin only after a later verifier-confirmed target match.

## Format Contract
- M3U8 playlists are line-oriented text beginning with an EXTM3U marker.
- Important tags include target duration, version, media sequence, key attributes, initialization
  map, stream-info entries, media renditions, partial segments, byte ranges, and media segment URI
  lines.
- Attribute values are comma-separated and many URI-like fields require quoted values.

## Harness Contract
- libFuzzer writes the raw bytes to a temporary file, loads it as a GPAC filter source, attaches an
  inspect filter with deep bitstream analysis, runs the filter session, and deletes the file.
- The source probe recognizes M3U8 content from the playlist marker or related manifest detection;
  there is no leading mode selector.

## Negative Memory
- Do not resubmit broad mutations that only reproduce `parser_reached_no_target_crash`.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store raw payload bytes, exact positions, task identifiers, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 9.
- Scope: generator repair and basin avoidance only.
