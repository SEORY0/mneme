---
type: causal-policy
title: "No Crash Mruby Script Mruby Script Reached Clean Exit Negative Memory"
description: "Negative memory for no_crash with mruby_script_reached_clean_exit on mruby-script inputs."
failure_class: no_crash
verifier_signal: mruby_script_reached_clean_exit
candidate_family: construct
input_format: mruby-script
harness_convention: libfuzzer-mruby-load-string
vuln_class: semantic-method-placement
access_scope: generate
success_count: 0
confidence: medium
tags: [no-crash, mruby-script-reached-clean-exit, mruby-script, semantic-method-placement, negative_memory]
match_keys: [no-crash, mruby-script-reached-clean-exit, mruby-script, semantic-method-placement]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
# No Crash Mruby Script Mruby Script Reached Clean Exit Negative Memory

- key: `no_crash x mruby_script_reached_clean_exit`
- outcome: persistent failure basin
- success_count: 0
- failure_count: 1
- formats: [[mruby-script]]

## Dead End
A direct script invoking Kernel#p executed successfully and printed output, but did not crash. The described issue appears semantic/debugger-related rather than a memory-safety path reachable by simply calling the method under the load-string fuzzer.

## Avoid
Do not repeat the same candidate family when the verifier signal matches this key. Treat broad seed mutation, wrapper usage paths, both-image crashes, parser-clean exits, or local-only crashes as evidence that the current surface is not the target differential.

## Recovery Direction
Preserve only independently validated format or harness reachability facts. Re-enter generation by first satisfying the harness contract and the earliest format gate, then use a different target-specific invariant instead of enlarging or randomly mutating the failed family.
