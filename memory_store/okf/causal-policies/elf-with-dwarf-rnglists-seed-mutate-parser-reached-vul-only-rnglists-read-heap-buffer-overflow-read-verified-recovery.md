---
type: causal-policy
title: "Elf With Dwarf Rnglists Seed Mutate Parser Reached Vul Only Rnglists Read Heap Buffer Overflow Read Verified Recovery"
description: "Round 25 verified recovery for wrong_sink with verifier signal parser_reached_vul_only_rnglists_read."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_vul_only_rnglists_read"
candidate_family: "seed_mutate"
input_format: "elf-with-dwarf-rnglists"
harness_convention: "libfuzzer"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: medium
tags: ["wrong-sink", "parser-reached-vul-only-rnglists-read", "elf-with-dwarf-rnglists", "libfuzzer", "seed-mutate", "verified-recovery", "round-25"]
match_keys: ["wrong_sink", "parser_reached_vul_only_rnglists_read", "elf-with-dwarf-rnglists", "libfuzzer", "heap-buffer-overflow-read"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 25
---
# Elf With Dwarf Rnglists Seed Mutate Parser Reached Vul Only Rnglists Read Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_vul_only_rnglists_read`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[elf-with-dwarf-rnglists]]
- harnesses: [[libfuzzer]]

## Failure Shape
Use a valid ELF/DWARF carrier and add a `.debug_rnglists` section with more than one rnglists context. Make the later context declare a length that is not larger than the whole section but is larger than the bytes remaining from that context's start. The vulnerable loader accepts the header and records an end offset past the actual section; later range-entry iteration reads beyond the loaded section. The fixed build validates the context against the remaining section window.

## Policy
For `wrong_sink x parser_reached_vul_only_rnglists_read` on `elf-with-dwarf-rnglists`, preserve the format recognition and harness contract before varying the vulnerable invariant. Prefer `seed-mutate` only while that carrier and harness contract remain stable.

## Procedure
1. Preserve the `elf-with-dwarf-rnglists` carrier and `libfuzzer` harness contract until parser reachability is stable.
2. Apply the causal invariant in the failure shape before broad mutation or seed sweeping.
3. Treat local crash class as supporting signal only; keep the candidate only when vulnerable and fixed images diverge on the official target relation.

## Verifier Contract
The official vulnerable-versus-fixed target match is the confirmation gate for this recovery policy; local crash class is supporting evidence only.

## Negative Memory
- Do not corrupt the outer `elf-with-dwarf-rnglists` recognition gate while retargeting this signal.
- Do not treat off-target crashes, clean parser exits, fixed-build crashes, or both-image crashes as success for this policy.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Format Contract
DWARF v5 rnglists sections contain one or more tables. Each table begins with an area length, version, address size, segment selector size, and offset-entry count, followed by an offset table and range-list entries. The section must be embedded in a valid object file for libdwarf initialization.

## Harness Contract
The harness writes the raw input to a temporary file, initializes libdwarf from that file, loads rnglists contexts, then iterates offset entries and range-list entries. Bare rnglists bytes are not sufficient; a valid ELF/DWARF carrier reaches the target parser.

## Evidence Shape
- Support: 1 server-verified round 25 solve after 1 attempt.
- Scope: generator repair and retargeting only.
