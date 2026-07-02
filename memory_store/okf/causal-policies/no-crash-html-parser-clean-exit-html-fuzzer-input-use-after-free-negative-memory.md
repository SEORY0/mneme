---
type: causal-policy
title: "No Crash Html Parser Clean Exit Html Fuzzer Input Use After Free Negative Memory"
description: "Negative memory for persistent no_crash / html_parser_clean_exit basin."
failure_class: "no_crash"
verifier_signal: "html_parser_clean_exit"
candidate_family: "construct_and_seed_mutate"
input_format: "html-fuzzer-input"
harness_convention: "afl-libfuzzer-compat-html"
vuln_class: "use-after-free"
access_scope: generate
success_count: 0
confidence: medium
tags: ["no-crash", "construct-and-seed-mutate", "html-fuzzer-input", "use-after-free", "negative-memory"]
match_keys: ["no-crash", "html-parser-clean-exit", "html-fuzzer-input", "afl-libfuzzer-compat-html", "use-after-free", "negative-memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
provenance: round-35-consolidator
---
# No Crash Html Parser Clean Exit Html Fuzzer Input Use After Free Negative Memory

## Policy
For `no_crash` with verifier signal `html_parser_clean_exit` on `html-fuzzer-input` under `afl-libfuzzer-compat-html`, treat the recorded family as a basin to avoid until a later verifier-confirmed candidate flips the gate. Preserve the descriptive format/harness facts, but do not promote this into a recovery policy.

## Avoided Basin
- The harness and HTML parser were reachable, but the attempted carriers did not hit the stale-input error relation.
- Plain malformed UTF-8, declared EUC-JP or Shift-JIS conversion errors, a real EUC-JP regression sample with truncation, unterminated DOCTYPE public/system literals, long text followed by parser errors, and recovery/compact/no-implied option modes all completed cleanly.
- The missing gate is likely a narrower push-parser buffer-error or encoding-flush state where the input buffer has moved and an error is reported before input pointers are reset.

## Recovery Direction
- Keep the parser/harness reachability facts in [[html-fuzzer-input]] and [[afl-libfuzzer-compat-html]].
- Retarget away from the failed relation named by `html_parser_clean_exit`; require vulnerable-only official confirmation before promoting any replacement.

## Evidence Shape
- Support: one round 35 persistent failure with concrete diagnosis and no official target match.
