---
type: causal-policy
title: "No Crash IAMF Demuxer Reached Clean Parse Or Clean Reject IAMF Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal iamf_demuxer_reached_clean_parse_or_clean_reject."
failure_class: "no_crash"
verifier_signal: "iamf_demuxer_reached_clean_parse_or_clean_reject"
candidate_family: "construct"
input_format: "iamf"
harness_convention: "libfuzzer-ffmpeg-demuxer-iamf"
vuln_class: "descriptor-length-misparse"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "iamf-demuxer-reached-clean-parse-or-clean-reject", "iamf", "negative-memory", "round-20"]
match_keys: ["no-crash", "iamf-demuxer-reached-clean-parse-or-clean-reject", "iamf"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash IAMF Demuxer Reached Clean Parse Or Clean Reject IAMF Negative Memory

- key: `no_crash x iamf_demuxer_reached_clean_parse_or_clean_reject`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[iamf]]
- harnesses: [[libfuzzer-ffmpeg-demuxer-iamf]]

## Dead End
The round 20 attempts for `iamf` under `libfuzzer-ffmpeg-demuxer-iamf` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- IAMF sequence-header and codec-config OBUs reached the demuxer, but AAC DecoderConfigDescriptor variants with descriptor length bytes did not produce a sanitizer signal. The likely missing piece is a descriptor payload that both satisfies the vulnerable parser's shifted gates and leaves malformed AAC-specific configuration for the downstream MPEG-4 audio parser.

## Negative Policy
When retrieval matches `no_crash x iamf_demuxer_reached_clean_parse_or_clean_reject`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[iamf]] and [[libfuzzer-ffmpeg-demuxer-iamf]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
