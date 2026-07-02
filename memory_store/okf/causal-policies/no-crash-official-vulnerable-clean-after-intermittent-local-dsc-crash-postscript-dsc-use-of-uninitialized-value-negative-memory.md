---
type: causal-policy
title: "No Crash Official Vulnerable Clean After Intermittent Local Dsc Crash Postscript Dsc Use Of Uninitialized Value Negative Memory"
description: "Negative memory for persistent no_crash / official_vulnerable_clean_after_intermittent_local_dsc_crash basin."
failure_class: "no_crash"
verifier_signal: "official_vulnerable_clean_after_intermittent_local_dsc_crash"
candidate_family: "construct"
input_format: "postscript-dsc"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "construct", "postscript-dsc", "use-of-uninitialized-value", "negative-memory"]
match_keys: ["no-crash", "official-vulnerable-clean-after-intermittent-local-dsc-crash", "postscript-dsc", "libfuzzer", "use-of-uninitialized-value", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Official Vulnerable Clean After Intermittent Local Dsc Crash Postscript Dsc Use Of Uninitialized Value Negative Memory

## Policy
For `no_crash` with verifier signal `official_vulnerable_clean_after_intermittent_local_dsc_crash` on `postscript-dsc` under `libfuzzer`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- A compact PostScript DSC envelope reached the scanner, and several empty-token variants intermittently crashed local verification, but official submission kept the vulnerable build clean.
- Distinct hypotheses covered headerless empty directives, headered empty directives, trailer-atend reuse, defaults/setup/page section placement, and a valid media declaration followed by an empty page media token.
- The likely remaining gap is finding a stale-token branch where the vulnerable build uses a previous token value to take a deterministic bad path while the fixed build skips it.

## Recovery Direction
- Keep the parser/harness reachability facts in [[postscript-dsc]] and [[libfuzzer]].
- Retarget away from the failed relation named by `official_vulnerable_clean_after_intermittent_local_dsc_crash`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
