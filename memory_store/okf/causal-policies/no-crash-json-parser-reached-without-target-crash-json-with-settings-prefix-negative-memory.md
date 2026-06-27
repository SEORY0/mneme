---
type: causal-policy
title: "No Crash JSON Parser Reached Without Target Crash JSON With Settings Prefix Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal json_parser_reached_without_target_crash."
failure_class: "no_crash"
verifier_signal: "json_parser_reached_without_target_crash"
candidate_family: "construct"
input_format: "json-with-settings-prefix"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "json-parser-reached-without-target-crash", "json-with-settings-prefix", "negative-memory", "round-20"]
match_keys: ["no-crash", "json-parser-reached-without-target-crash", "json-with-settings-prefix"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash JSON Parser Reached Without Target Crash JSON With Settings Prefix Negative Memory

- key: `no_crash x json_parser_reached_without_target_crash`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[json-with-settings-prefix]]
- harnesses: [[libfuzzer]]

## Dead End
The round 20 attempts for `json-with-settings-prefix` under `libfuzzer` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- The JSON reader was reached under permissive settings, but constructed probes around Unicode escapes, unterminated strings, comments, single quotes, duplicate keys, trailing commas, and large numeric forms all parsed or failed safely. The missing trigger is likely a narrower reader state transition involving string/comment boundary handling rather than a general malformed JSON envelope.

## Negative Policy
When retrieval matches `no_crash x json_parser_reached_without_target_crash`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[json-with-settings-prefix]] and [[libfuzzer]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
