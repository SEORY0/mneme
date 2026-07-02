---
type: causal-policy
title: "TIFF Construct From Valid Seed Generic Crash PTIF TIFF Read Crash Official Target Match Segmentation Fault Alpha Disassociation Verified Recovery"
description: "Round 32 server-verified recovery for tiff keyed by generic_crash x ptif_tiff_read_crash_official_target_match."
failure_class: "generic_crash"
verifier_signal: "ptif_tiff_read_crash_official_target_match"
candidate_family: "construct-from-valid-seed"
input_format: "tiff"
harness_convention: "libfuzzer"
vuln_class: "segmentation-fault-alpha-disassociation"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "ptif-tiff-read-crash-official-target-match", "tiff", "libfuzzer", "construct-from-valid-seed", "segmentation-fault-alpha-disassociation", "verified-recovery", "round-32"]
match_keys: ["generic-crash", "ptif-tiff-read-crash-official-target-match", "tiff", "libfuzzer", "construct-from-valid-seed", "segmentation-fault-alpha-disassociation", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# TIFF Construct From Valid Seed Generic Crash PTIF TIFF Read Crash Official Target Match Segmentation Fault Alpha Disassociation Verified Recovery

- key: `generic_crash x ptif_tiff_read_crash_official_target_match`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[tiff]]
- related harness facts: [[libfuzzer]]

## Policy
When `tiff` under `[[libfuzzer]]` produces `ptif_tiff_read_crash_official_target_match` from `generic_crash`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[tiff]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Start from a valid tiny LogLuv TIFF carrier and preserve the SGILog compression/body relationship. Coherently advertise an associated alpha extra sample by updating the sample-count metadata and the per-sample descriptor arrays, while keeping the non-RGB photometric interpretation. This reaches ReadTIFFImage's LogLuv import path with image matte state set; the vulnerable build disassociates alpha for a non-RGB photometric image, while the fixed build avoids that disassociation and exits cleanly.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- TIFF reachability depends on a valid endian header, image-file-directory table, baseline geometry tags, compression tag, photometric interpretation, strip offset/byte-count metadata, SamplesPerPixel, BitsPerSample, SampleFormat, and ExtraSamples alpha metadata. For this bug family, plain grayscale or palette alpha samples can parse cleanly; the crashing relation is a non-RGB LogLuv transfer path combined with associated alpha metadata.

## Harness Contract
- The GraphicsMagick coder fuzzer selects the PTIF coder, which aliases into the TIFF coder. It passes the submitted raw bytes as an image blob, forces the coder name, reads the image through Magick++, and may write the image back if the selected coder has encoder support. There is no FuzzedDataProvider split or external argv-controlled file format beyond the raw TIFF-family bytes.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct-from-valid-seed.
