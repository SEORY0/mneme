---
type: causal-policy
title: "Ar Archive ELF Construct Parser Reached Target Confirmed Heap Buffer Overflow Read Verified Recovery"
description: "Round 15 server-verified recovery for ar-archive-elf keyed by wrong_sink x parser_reached_target_confirmed."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_target_confirmed"
candidate_family: "construct"
input_format: "ar-archive-elf"
harness_convention: "libfuzzer-tempfile-bfd"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-target-confirmed", "ar-archive-elf", "libfuzzer-tempfile-bfd", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-15"]
match_keys: ["wrong_sink", "parser_reached_target_confirmed", "ar-archive-elf", "libfuzzer-tempfile-bfd", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 15
---
# Ar Archive ELF Construct Parser Reached Target Confirmed Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_target_confirmed`
- outcome: server-verified target match
- success_count: 1
- related format facts: [[ar-archive-elf]]
- related harness facts: [[libfuzzer-tempfile-bfd]]

## Policy
When `ar-archive-elf` under `libfuzzer-tempfile-bfd` reaches `parser_reached_target_confirmed` from `wrong_sink`, preserve the accepted parser carrier and retarget only the causal invariant proven by the verifier. Treat local coarse labels as advisory once the vulnerable image fails and the fixed image does not reproduce the target behavior.

## Procedure
1. Preserve the harness contract and format family that reached the parser; do not switch envelopes after reachability is proven.
2. Wrap a malformed MIPS ELF object inside a GNU archive and include archive metadata that causes
   BFD to open the member object during archive checking. The object contains a MIPS options
   section with a reginfo option header whose declared body is too short for the fixed reginfo
   read, so the MIPS section handler reads past the section buffer.
3. Keep mutations focused on the relevant invariant: parser selection, declared length versus available content, selector versus subparser, table count versus records, lifetime ownership, or sink-specific state.
4. If local labels report a non-target sink while the parser branch is reached, submit once before discarding the candidate.
5. If the fixed image also fails, shrink to the smallest boundary relation and avoid broad randomization.

## Format Contract
- A GNU ar archive may contain a global symbol table before member objects, and BFD archive checks can
  parse referenced member objects. In MIPS ELF, the options section is a sequence of option headers
  containing kind and size metadata; the reginfo option expects a fixed-size register information
  payload after its header.

## Harness Contract
- The libFuzzer input is written to a temporary file, opened by BFD, and checked as an archive.
  Reaching member ELF parsing depends on archive metadata, not just a standalone ELF header. There is
  no selector byte and no FuzzedDataProvider layout.

## Negative Memory
- Do not replay unrelated seeds after this parser branch is reached.
- Do not count fixed-image crashes, both-image crashes, clean exits, parser rejection, or off-target local stacks as success.
- Do not store concrete payload bytes, task identifiers, exact positions, checksums, or submit metadata.

## Evidence Shape
- Support: one server-verified Round 15 solve.
- Candidate family: construct.
