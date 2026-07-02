---
type: causal-policy
title: "Json Construct After Fuzz Probe Generic Crash Official Target Match Global Replacement Read Global Buffer Overflow Read Verified Recovery"
description: "Verified recovery distilled from a round trace for generic_crash / official_target_match_global_replacement_read."
failure_class: "generic_crash"
verifier_signal: "official_target_match_global_replacement_read"
candidate_family: "construct_after_fuzz_probe"
input_format: "json"
harness_convention: "libfuzzer"
vuln_class: "global-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["generic-crash", "construct-after-fuzz-probe", "json", "global-buffer-overflow-read", "verified-recovery"]
match_keys: ["generic-crash", "official-target-match-global-replacement-read", "json", "libfuzzer", "global-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: round-35-consolidator
---
# Json Construct After Fuzz Probe Generic Crash Official Target Match Global Replacement Read Global Buffer Overflow Read Verified Recovery

## Policy
For `generic_crash` with verifier signal `official_target_match_global_replacement_read` on `json` under `libfuzzer`, recover by preserving the format and harness gates that reach the target sink, then mutate only the invariant described by the verified recipe. This policy is keyed to the failure signal and is not a byte-level PoC recipe.

## Procedure
1. Use a standalone JSON string that enters unicode escape handling.
2. First provide a high-surrogate escape, then a non-unicode separator so the parser emits the replacement marker for the unmatched high surrogate, and later provide a low-surrogate escape before closing the string.
3. This reaches the surrogate-pair cleanup path where the vulnerable build compares the print buffer against the fixed replacement marker with a string comparison that reads past the marker; the fixed build avoids that read.

## Format Contract
- Input format: [[json]].
- Harness contract: [[libfuzzer]].
- Keep parser reachability and sink selection intact before mutating the vulnerable relation.

## Negative Memory
- Do not broaden this into unrelated `json` failures without the same failure class and verifier signal.
- Do not store task identifiers, raw bytes, exact offsets, checksums, or submit metadata.

## Evidence Shape
- Support: one round 35 verified official target match; vulnerable build reached the target signal and the fixed build did not.

## Diagnosis Notes
Simple inputs ending during a unicode escape, ending after the high-surrogate transition, using NUL truncation, wrapping the string in arrays or objects, and growing the pending print buffer all returned cleanly. The crash required a completed high surrogate followed by a non-pair character and then a later low surrogate so the replacement-removal comparison executed.
