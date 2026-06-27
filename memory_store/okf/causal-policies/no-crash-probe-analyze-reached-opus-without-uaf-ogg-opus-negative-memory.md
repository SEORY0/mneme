---
type: causal-policy
title: "No Crash Probe Analyze Reached Opus Without Uaf Ogg Opus Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal probe_analyze_reached_opus_without_uaf."
failure_class: "no_crash"
verifier_signal: "probe_analyze_reached_opus_without_uaf"
candidate_family: "construct"
input_format: "ogg-opus"
harness_convention: "libfuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "probe-analyze-reached-opus-without-uaf", "ogg-opus", "negative-memory", "round-20"]
match_keys: ["no-crash", "probe-analyze-reached-opus-without-uaf", "ogg-opus"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Probe Analyze Reached Opus Without Uaf Ogg Opus Negative Memory

- key: `no_crash x probe_analyze_reached_opus_without_uaf`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[ogg-opus]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `ogg-opus` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Bare Opus configuration bytes did not route to the parser. A valid two-page Ogg Opus envelope was recognized by GPAC as an Opus audio stream, but valid, duplicate-sequence, and malformed-continuation variants did not trigger the use-after-free. The missing condition is likely a broken Ogg page sequence that is still accepted deeply enough to create and then invalidate stream/filter state.

## Negative Policy
When retrieval matches `no_crash x probe_analyze_reached_opus_without_uaf`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[ogg-opus]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
