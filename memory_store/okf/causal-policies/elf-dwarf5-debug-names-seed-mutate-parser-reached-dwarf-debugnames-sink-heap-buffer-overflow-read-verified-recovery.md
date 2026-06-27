---
type: causal-policy
title: "ELF Dwarf5 Debug Names Seed Mutate Parser Reached DWARF Debugnames Sink Heap Buffer Overflow Read Verified Recovery"
description: "Server-verified recovery for elf-dwarf5-debug-names when wrong_sink pairs with parser_reached_dwarf_debugnames_sink."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_dwarf_debugnames_sink"
candidate_family: "seed_mutate"
input_format: "elf-dwarf5-debug-names"
harness_convention: "oss-fuzz-run_poc-libdwarf-fuzz_globals"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-dwarf-debugnames-sink", "elf-dwarf5-debug-names", "oss-fuzz-run-poc-libdwarf-fuzz-globals", "seed-mutate", "verified-recovery", "round-18"]
match_keys: ["wrong-sink", "parser-reached-dwarf-debugnames-sink", "elf-dwarf5-debug-names", "oss-fuzz-run-poc-libdwarf-fuzz-globals", "seed-mutate", "heap-buffer-overflow-read", "verified-recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 18
---
# ELF Dwarf5 Debug Names Seed Mutate Parser Reached DWARF Debugnames Sink Heap Buffer Overflow Read Verified Recovery

- key: `wrong_sink x parser_reached_dwarf_debugnames_sink`
- outcome: server-verified vulnerable/fixed split
- success_count: 1
- related format facts: [[elf-dwarf5-debug-names]]
- related harness facts: [[oss-fuzz-run-poc-libdwarf-fuzz-globals]]

## Policy
When `wrong_sink x parser_reached_dwarf_debugnames_sink` appears for `elf-dwarf5-debug-names`, preserve the parser or harness carrier already shown to reach the target branch. Retarget only the causal invariant named by the verifier signal and vulnerability class; do not broaden into unrelated container families after reachability is established.

## Procedure
1. Feed the libdwarf globals fuzzer an ELF/DWARF5 object with a malformed `.debug_names` accelerator table.
2. The table is accepted by dwarf_init and global lookup, but internal limit calculations for the debug-names header allow a read beyond the section buffer.

## Negative Memory
- Do not count local-only crashes, both-image crashes, coarse sink labels, or clean parser reachability as success for this key.
- Do not store raw payload bytes, exact positions, task identifiers, checksums, or submit metadata.

## Format Contract
Use [[elf-dwarf5-debug-names]]; the relevant gate is the accepted carrier plus the invariant described above, not a byte-specific recipe.

## Harness Contract
Use [[oss-fuzz-run-poc-libdwarf-fuzz-globals]]; preserve the observed input contract before mutating deeper fields.

## Evidence Shape
- Support: 1 server-verified round 18 solve.
- Candidate family: seed_mutate.

## Round 18 Verified Evidence
- Verifier key: `wrong_sink x parser_reached_dwarf_debugnames_sink`.
- Vulnerability class: `heap-buffer-overflow-read`.
- Recovery summary: Feed the libdwarf globals fuzzer an ELF/DWARF5 object with a malformed `.debug_names` accelerator table.
