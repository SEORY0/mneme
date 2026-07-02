---
type: causal-policy
title: "Miff Construct Wrong Sink Parser Reached Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 32 server-verified recovery for miff keyed by wrong_sink x parser_reached_official_target_match."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_official_target_match"
candidate_family: "construct"
input_format: "miff"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-official-target-match", "miff", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-official-target-match", "miff", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Miff Construct Wrong Sink Parser Reached Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[miff]]
- related harness facts: [[libfuzzer]]

## Policy
When `miff` under `[[libfuzzer]]` produces `parser_reached_official_target_match` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[miff]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Use a minimal DirectClass RGB MIFF header selecting Zip compression and version-zero continuous deflate decoding. Declare more than one row, but provide a valid deflate stream that decodes only a strict prefix of the first row and leaves no further compressed input for the following row. The vulnerable reader imports an underfilled row buffer and later write-back consumes the poisoned pixels; the fixed build handles the zero-length continuation row cleanly before poisoned pixels are written.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- MIFF starts with ASCII key/value attributes identifying ImageMagick, class, colorspace, compression, dimensions, and depth, then a header terminator followed by binary payload. DirectClass RGB derives row width from columns, depth, matte state, and colorspace. For Zip compression, version-zero MIFF uses a continuous zlib stream with a computed per-row read budget, while later versions use explicit compressed-chunk lengths. Underfilled deflate output can leave the row import buffer partly uninitialized; PseudoClass carriers consume uninitialized indices earlier but can also trigger fixed-build failures.

## Harness Contract
- The GraphicsMagick MIFF coder fuzzer passes the raw libFuzzer bytes directly as a Magick blob with the MIFF coder forced. There is no leading selector or carved sub-input. Magick exceptions during read are caught; if read returns an image, the harness writes it back to a MIFF blob, so read-side uninitialized pixels can surface during write-back.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.
