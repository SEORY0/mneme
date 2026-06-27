---
type: causal-policy
title: "No Crash Calendar Parser Reached Clean Reject Or Clean Parse Icalendar Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal calendar_parser_reached_clean_reject_or_clean_parse."
failure_class: "no_crash"
verifier_signal: "calendar_parser_reached_clean_reject_or_clean_parse"
candidate_family: "construct"
input_format: "icalendar"
harness_convention: "libfuzzer-libical_parse_string"
vuln_class: "icalendar-value-parser-boundary"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "calendar-parser-reached-clean-reject-or-clean-parse", "icalendar", "negative-memory", "round-20"]
match_keys: ["no-crash", "calendar-parser-reached-clean-reject-or-clean-parse", "icalendar"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Calendar Parser Reached Clean Reject Or Clean Parse Icalendar Negative Memory

- key: `no_crash x calendar_parser_reached_clean_reject_or_clean_parse`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[icalendar]]
- harnesses: [[libfuzzer-libical-parse-string]]

## Dead End
The round 20 attempts for `icalendar` under `libfuzzer-libical_parse_string` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Valid VCALENDAR/VEVENT wrappers with GEO overflow-style values and several comma-splitting edge cases parsed or rejected cleanly. The attempted properties did not trigger the exact short-lookbehind or coordinate conversion invariant for this build.

## Negative Policy
When retrieval matches `no_crash x calendar_parser_reached_clean_reject_or_clean_parse`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[icalendar]] and [[libfuzzer-libical-parse-string]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
