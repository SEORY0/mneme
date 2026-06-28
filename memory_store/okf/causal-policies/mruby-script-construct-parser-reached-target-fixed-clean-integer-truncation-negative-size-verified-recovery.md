---
type: causal-policy
title: "Mruby Script Construct Parser Reached Target Fixed Clean Integer Truncation Negative Size Verified Recovery"
description: "Round 15 server-verified recovery for mruby-script keyed by wrong_sink x parser_reached_target_fixed_clean."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_fixed_clean"
candidate_family: "construct"
input_format: "mruby-script"
harness_convention: "libfuzzer-mruby-load-string"
vuln_class: "integer-truncation-negative-size"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-fixed-clean", "mruby-script", "libfuzzer-mruby-load-string", "construct", "integer-truncation-negative-size", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_fixed_clean", "mruby-script", "libfuzzer-mruby-load-string", "integer-truncation-negative-size", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Mruby Script Construct Parser Reached Target Fixed Clean Integer Truncation Negative Size Verified Recovery

- key: `wrong_sink x parser_reached_target_fixed_clean`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[mruby-script]]
- related harness facts: [[libfuzzer-mruby-load-string]]

## Policy
When `mruby-script` under `libfuzzer-mruby-load-string` reaches `parser_reached_target_fixed_clean` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Provide valid mruby source that executes Kernel sprintf. Use a literal precision field larger
   than the destination int range on a string conversion, so the parser accepts the numeric field
   in the wider integer type and then truncates it before the string precision copy. This reaches
   the sprintf implementation and violates the invariant that precision must remain nonnegative and
   representable after parsing.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- The input is plain mruby source text. Syntactically valid Ruby code is required to reach runtime
  methods. sprintf format strings parse flags, width, precision, and conversion type; literal numeric
  width and precision are parsed differently from star-supplied runtime arguments.

## Harness Contract
- The harness copies raw bytes into a newly allocated NUL-terminated source string, opens a fresh
  mruby state, calls mrb_load_string, then closes the state. There is no filename envelope, bytecode
  wrapper, selector byte, or FuzzedDataProvider layout.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.
