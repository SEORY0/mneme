---
type: causal-policy
title: "Fiff Wrapped Dng Ljpeg Construct Generic Crash Coarse Crash Official Target Match Use Of Uninitialized Value Verified Recovery"
description: "Round 30 verified recovery for generic_crash with verifier signal coarse_crash_official_target_match."
failure_class: "generic_crash"
verifier_signal: "coarse_crash_official_target_match"
candidate_family: "construct"
input_format: "fiff-wrapped-dng-ljpeg"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: medium
tags: ["generic-crash", "coarse-crash-official-target-match", "fiff-wrapped-dng-ljpeg", "libfuzzer", "construct", "verified-recovery", "round-30"]
match_keys: ["generic-crash", "coarse-crash-official-target-match", "fiff-wrapped-dng-ljpeg", "libfuzzer", "use-of-uninitialized-value"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 30
---
# Fiff Wrapped Dng Ljpeg Construct Generic Crash Coarse Crash Official Target Match Use Of Uninitialized Value Verified Recovery

- key: `generic-crash x coarse-crash-official-target-match`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[fiff-wrapped-dng-ljpeg]]
- harnesses: [[libfuzzer]]

## Failure Shape
Wrap a structurally valid DNG/TIFF image in the Fuji FIFF carrier expected by the active parser harness. The embedded DNG declares a lossless-JPEG-compressed tile with coherent image dimensions, tile offsets, byte counts, bit depth, and component count. The embedded LJpeg stream itself is syntactically valid, with matching DHT, SOF3, and SOS component/table declarations, but its frame covers fewer rows than the DNG tile or slice claims. The vulnerable build returns from decode with part of the image buffer still uninitialized; the fixed build rejects or handles the frame/tile size mismatch.

## Policy
For `generic-crash x coarse-crash-official-target-match` on `fiff-wrapped-dng-ljpeg`, preserve the parser and harness gates first, then mutate only the causal invariant described by the verified trace. Prefer `construct` while this format and harness contract are present.

## Procedure
1. Preserve the `fiff-wrapped-dng-ljpeg` carrier enough for the `libfuzzer` harness to reach the parser path.
2. Keep unrelated envelope fields minimal and stable so verifier feedback stays tied to the target sink.
3. Apply the verified invariant from the failure shape rather than random broad mutation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image rejects or avoids it.

## Verifier Contract
The local class may remain coarse. Treat the official vulnerable-versus-fixed target match as the confirmation gate for this policy.

## Negative Memory
- Do not corrupt the outer `fiff-wrapped-dng-ljpeg` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser reachability, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve(s), including round 30.
- Scope: generator repair only.
