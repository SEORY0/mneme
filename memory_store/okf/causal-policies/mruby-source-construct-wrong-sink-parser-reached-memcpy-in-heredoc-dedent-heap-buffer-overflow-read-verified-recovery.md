---
type: "causal-policy"
title: "Mruby Source Construct Wrong Sink Parser Reached Memcpy In Heredoc Dedent Heap Buffer Overflow Read Verified Recovery"
description: "Round 38 verified recovery for wrong_sink with verifier signal parser_reached_memcpy_in_heredoc_dedent."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_memcpy_in_heredoc_dedent"
candidate_family: "construct"
input_format: "mruby-source"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: "generate"
success_count: 1
confidence: "high"
tags: ["wrong-sink", "parser-reached-memcpy-in-heredoc-dedent", "mruby-source", "libfuzzer", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-38"]
match_keys: ["wrong_sink", "parser_reached_memcpy_in_heredoc_dedent", "mruby-source", "libfuzzer", "heap-buffer-overflow-read", "verified-recovery", "construct"]
allowed_scopes: ["generate"]
forbidden_fields: ["raw_poc_bytes", "task_id", "exact_offset", "checksum", "submit_metadata"]
evidence_level: "high"
train_only: true
round: 38
---
# Mruby Source Construct Wrong Sink Parser Reached Memcpy In Heredoc Dedent Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_memcpy_in_heredoc_dedent`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[mruby-source]]
- related harness facts: [[libfuzzer]]

## Failure Shape
Use raw Ruby source that forms a valid squiggly heredoc, then make one logical heredoc line exceed the parser token-buffer capacity before an escaped newline continuation. Keep the heredoc terminator valid so the compiler reaches dedent handling; the vulnerable build records continuation split state beyond the truncated token length and later copies from that inconsistent range, while the fixed build exits cleanly.

## Policy
When `wrong_sink x parser_reached_memcpy_in_heredoc_dedent` appears for `[[mruby-source]]` under `[[libfuzzer]]`, preserve every recognition, length, selector, allocation-state, lifetime, and checksum-equivalent gate needed to reach the target parser before changing the sink-specific relation. Treat vulnerable/fixed divergence from the official verifier as the success gate; local parser reachability and local crash labels are supporting signals only.

## Procedure
1. Start from the `[[mruby-source]]` format contract and `[[libfuzzer]]` harness contract; keep the accepted envelope, dispatch selectors, declared lengths, and state setup coherent until parser reachability is stable.
2. Recreate the causal relation described in the failure shape before broad mutation or seed sweeping.
3. Change one invariant at a time: selector-to-subparser, declared length-to-available data, count-to-record body, lifetime/ownership state, allocation-size relation, or sanitizer-specific sink relation.
4. Submit only candidates where the vulnerable image reaches the target relation and the fixed image exits cleanly, rejects the relation, or otherwise avoids the target crash.

## Verifier Contract
This policy is ranked by one official target match. Re-rank or quarantine it if later use returns only clean exits, wrong sinks, wrapper-specific crashes, or fixed-image crashes.

## Negative Memory
- Do not corrupt the outer `[[mruby-source]]` recognition gate while retargeting this signal.
- Do not count parser reachability, both-image crashes, local wrapper crashes, clean exits, or fixed-image crashes as success.
- Do not store payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Evidence Shape
- Support: server-verified round 38 solve after 2 attempts.
- Candidate family: construct.
- Official split: vulnerable exit 1, fixed exit 0, target_match True.
- Scope: generator repair and retargeting only.
