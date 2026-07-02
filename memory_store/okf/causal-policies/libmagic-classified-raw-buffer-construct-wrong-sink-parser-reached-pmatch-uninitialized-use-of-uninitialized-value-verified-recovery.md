---
type: causal-policy
title: "Libmagic Classified Raw Buffer Construct Wrong Sink Parser Reached Pmatch Uninitialized Use Of Uninitialized Value Verified Recovery"
description: "Round 32 server-verified recovery for libmagic-classified-raw-buffer keyed by wrong_sink x parser_reached_pmatch_uninitialized."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_pmatch_uninitialized"
candidate_family: "construct"
input_format: "libmagic-classified-raw-buffer"
harness_convention: "libfuzzer"
vuln_class: "use-of-uninitialized-value"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-pmatch-uninitialized", "libmagic-classified-raw-buffer", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery", "round-32"]
match_keys: ["wrong-sink", "parser-reached-pmatch-uninitialized", "libmagic-classified-raw-buffer", "libfuzzer", "construct", "use-of-uninitialized-value", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 32
---
# Libmagic Classified Raw Buffer Construct Wrong Sink Parser Reached Pmatch Uninitialized Use Of Uninitialized Value Verified Recovery

- key: `wrong_sink x parser_reached_pmatch_uninitialized`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[libmagic-classified-raw-buffer]]
- related harness facts: [[libfuzzer]]

## Policy
When `libmagic-classified-raw-buffer` under `[[libfuzzer]]` produces `parser_reached_pmatch_uninitialized` from `wrong_sink`, keep the parser-reaching envelope and retarget the causal invariant that the official verifier accepted. Local sink labels are advisory once the vulnerable image fails and the fixed image stays clean or the server reports target match.

## Procedure
1. Preserve the harness and format contract that reached the parser: `[[libmagic-classified-raw-buffer]]` through `[[libfuzzer]]`.
2. Apply the verified recovery: Feed a minimal text-like raw buffer that satisfies a compiled libmagic regex rule, causing FILE_REGEX handling to call regexec with one match slot and then consume pmatch fields. The vulnerable build accepts a successful regex result with match fields left uninitialized.
3. Keep mutations narrow around the gate/invariant relation rather than rebuilding unrelated carriers or adding broad random noise.
4. If local labels report a non-target sink while the parser branch is reached, submit one minimized candidate before discarding it.
5. Reject both-image crashes, fixed-image crashes, parser rejection, and clean exits as non-success even when they look close locally.

## Format Contract
- The file-magic harness classifies raw input bytes directly through libmagic's compiled rules. Parser selection is rule-driven; text-like buffers can reach regex and search rules without a normal file container. Regex rules copy a bounded search slice and NUL-terminate it before calling regexec.

## Harness Contract
- The libFuzzer entrypoint passes the whole non-empty input buffer to magic_buffer. There is no leading selector, marker delimiter, checksum, length envelope, or FuzzedDataProvider split.

## Negative Memory
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.
- Do not treat parser reachability alone as success without the official target-match signal.
- Do not repeat a clean-exit or both-image-crash basin once the verifier has characterized it.

## Evidence Shape
- Support: one server-verified Round 32 solve.
- Candidate family: construct.
