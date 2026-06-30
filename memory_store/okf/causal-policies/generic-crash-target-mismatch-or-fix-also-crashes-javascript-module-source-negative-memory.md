---
type: causal-policy
title: "Generic Crash Target Mismatch Or Fix Also Crashes Javascript Module Source Negative Memory"
description: "Round 31 negative memory for generic_crash with verifier signal target_mismatch_or_fix_also_crashes."
failure_class: "generic_crash"
verifier_signal: "target_mismatch_or_fix_also_crashes"
candidate_family: "construct"
input_format: "javascript-module-source"
harness_convention: "libfuzzer-quickjs-module-compile-eval"
vuln_class: "module-linking-cycle-evaluation"
access_scope: generate
success_count: 0
failure_count: 1
confidence: medium
tags: ["generic-crash", "target-mismatch-or-fix-also-crashes", "javascript-module-source", "libfuzzer-quickjs-module-compile-eval", "negative-memory", "round-31"]
match_keys: ["generic-crash", "target-mismatch-or-fix-also-crashes", "javascript-module-source", "libfuzzer-quickjs-module-compile-eval", "module-linking-cycle-evaluation", "negative_memory"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
round: 31
---
# Generic Crash Target Mismatch Or Fix Also Crashes Javascript Module Source Negative Memory

- key: `generic_crash x target_mismatch_or_fix_also_crashes`
- outcome: persistent failure / basin to avoid
- success_count: 0
- failure_count: 1
- related format facts: [[javascript-module-source]]
- related harness facts: [[libfuzzer-quickjs-module-compile-eval]]

## Failure Shape
- Plain JavaScript module source reached the compile/evaluate harness only when the trailing terminator gate was satisfied.
- Static self-cycles through the harness-assigned main module name can crash import binding resolution, but that basin is not patch-specific when the fixed image also exits non-zero.
- Dynamic self-import and async-job variants can produce vulnerable-only crashes, but the observed verifier signal classified them as off-target for the described module-linking target.

## Policy
Treat `generic_crash x target_mismatch_or_fix_also_crashes` for `javascript-module-source` as an off-target or both-image basin unless a new candidate changes the module-linking state relation and proves a fixed-clean official split.

## Procedure
1. Keep the terminator gate and module source parsing intact before testing deeper module graph states.
2. Reject candidates that reproduce self-cycle binding crashes without a fixed-clean official split.
3. Change the causal relation, such as alias preservation, import.meta/module-name binding, async job queue state, or namespace resolution, rather than resubmitting broad self-import variants.

## Format Contract
Use [[javascript-module-source]]; the source must remain an ES module accepted by the harness-specific terminator gate before any module-linking hypothesis is meaningful.

## Harness Contract
Use [[libfuzzer-quickjs-module-compile-eval]]; preserve the compile, bytecode round-trip, import resolution, import.meta setup, evaluation, and job-loop sequence before retargeting module graph state.

## Negative Memory
- Do not resubmit broad self-import, namespace-read, alias-cycle, or async-job variants that return to the same off-target or fixed-crashing basin.
- Do not count parser reachability, vulnerable-only local crashes, both-image crashes, fixed-image crashes, or target-mismatch submissions as success.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: one diagnosed persistent failure from round 31.
- Scope: generator repair and basin avoidance only.
