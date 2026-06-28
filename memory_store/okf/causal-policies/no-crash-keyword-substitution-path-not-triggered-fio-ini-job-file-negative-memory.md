---
type: causal-policy
title: "No Crash Keyword Substitution Path Not Triggered Fio Ini Job File Negative Memory"
description: "Round 20 negative memory for no_crash with verifier signal keyword_substitution_path_not_triggered."
failure_class: "no_crash"
verifier_signal: "keyword_substitution_path_not_triggered"
candidate_family: "construct_ini"
input_format: "fio ini job file"
harness_convention: "AFL-style fio parseini buffer with trailing type byte"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "keyword-substitution-path-not-triggered", "fio-ini-job-file", "negative-memory", "round-20"]
match_keys: ["no-crash", "keyword-substitution-path-not-triggered", "fio-ini-job-file"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 20
---
# No Crash Keyword Substitution Path Not Triggered Fio Ini Job File Negative Memory

- key: `no_crash x keyword_substitution_path_not_triggered`
- outcome: persistent failure basin to avoid
- success_count: 0
- failure_count: 1
- formats: [[fio-ini-job-file]]
- harnesses: [[afl-style-fio-parseini-buffer-with-trailing-type-byte]]

## Dead End
The round 20 attempts for `fio ini job file` under `AFL-style fio parseini buffer with trailing type byte` did not produce a verified target match. Do not promote these attempts into positive recovery without a future server-verified solve.

## Diagnosed Basin
- Valid global/job ini envelopes with the described keyword in the description option and varied parser type bytes did not trigger the sanitizer. The missing gate appears to be an option parsing shape that passes the full option string into keyword substitution in the vulnerable position.

## Negative Policy
When retrieval matches `no_crash x keyword_substitution_path_not_triggered`, avoid repeating this basin. First re-check the harness contract, format gate, and sink-specific dispatch condition. If the candidate only produces clean execution, wrapper-only crashes, off-target crashes, or an unverified recon state, retarget the carrier or abandon this family rather than scaling the same mutation.

## Retarget Hints
- Preserve factual format and harness gates from [[fio-ini-job-file]] and [[afl-style-fio-parseini-buffer-with-trailing-type-byte]].
- Prefer a different dispatch route or seed family unless new verifier feedback shows the target path is reached.
- Treat generic local crashes, clean exits, and `not_verified` recon states as non-success until official vulnerable-versus-fixed confirmation.

## Evidence Shape
- Support: 1 round 20 failed trace(s) with concrete diagnosis.
- Scope: generator avoidance only.
