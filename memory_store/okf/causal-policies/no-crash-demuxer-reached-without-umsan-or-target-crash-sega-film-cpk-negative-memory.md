---
type: causal-policy
title: "No Crash Demuxer Reached Without Umsan Or Target Crash Sega Film Cpk Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal demuxer_reached_without_umsan_or_target_crash."
failure_class: "no_crash"
verifier_signal: "demuxer_reached_without_umsan_or_target_crash"
candidate_family: "seed_mutate"
input_format: "sega-film-cpk"
harness_convention: "libfuzzer"
vuln_class: "uninitialized-value"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "demuxer-reached-without-umsan-or-target-crash", "sega-film-cpk", "negative-memory", "round-20"]
match_keys: ["no-crash", "demuxer-reached-without-umsan-or-target-crash", "sega-film-cpk"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Demuxer Reached Without Umsan Or Target Crash Sega Film Cpk Negative Memory

- key: `no_crash x demuxer_reached_without_umsan_or_target_crash`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[sega-film-cpk]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `sega-film-cpk` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- A valid in-tree Sega FILM sample and mutations around table truncation, padding, audio-marker style fields, and chunk naming all demuxed or failed cleanly. The source issue appears to require an audio sample record that leaves the keyframe field uninitialized and later causes the demuxer packet path to observe it under sanitizer instrumentation; the tested samples did not make that read observable as a crash.

## Negative Policy
When retrieval matches `no_crash x demuxer_reached_without_umsan_or_target_crash`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[sega-film-cpk]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
