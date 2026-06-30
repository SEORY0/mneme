---
type: causal-policy
title: "UDP Sigcomp Construct Parser Reached Sink Mismatch Label But Stack Matches Sigcomp Operand Decoder Heap Buffer Overflow Read Verified Recovery"
description: "Round 27 verified recovery for wrong_sink with verifier signal parser_reached_sink_mismatch_label_but_stack_matches_sigcomp_operand_decoder."
failure_class: "wrong_sink"
verifier_signal: "parser_reached_sink_mismatch_label_but_stack_matches_sigcomp_operand_decoder"
candidate_family: "construct"
input_format: "udp-sigcomp"
harness_convention: "libfuzzer-fuzzshark-udp"
vuln_class: "heap-buffer-overflow-read"
access_scope: generate
success_count: 1
confidence: high
tags: ["wrong-sink", "parser-reached-sink-mismatch-label-but-stack-matches-sigcomp-operand-decoder", "udp-sigcomp", "libfuzzer-fuzzshark-udp", "construct", "heap-buffer-overflow-read", "verified-recovery", "round-27"]
match_keys: ["wrong_sink", "parser_reached_sink_mismatch_label_but_stack_matches_sigcomp_operand_decoder", "udp-sigcomp", "libfuzzer-fuzzshark-udp", "heap-buffer-overflow-read", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
round: 27
---
# UDP Sigcomp Construct Parser Reached Sink Mismatch Label But Stack Matches Sigcomp Operand Decoder Heap Buffer Overflow Read Verified Recovery

## Policy
For `wrong_sink x parser_reached_sink_mismatch_label_but_stack_matches_sigcomp_operand_decoder`, preserve the format and harness gates that reached the parser or sink, then apply the verified causal relation below. This is a positive recovery policy because the official vulnerable/fixed verifier recorded a target match.

## Procedure
1. Build a raw UDP datagram whose ports select the SigComp dissector, then use SigComp's uploaded-bytecode message form.
2. The uploaded UDVM program writes an operand-consuming instruction into the terminal UDVM memory cell and branches there with a position-independent address operand.
3. Execution then asks the reference-operand decoder to fetch the next operand beyond UDVM memory, producing a target-only heap read while keeping the packet and decompression path otherwise narrow.
4. Keep the carrier abstract: preserve the gate/invariant relation, not any task-local bytes or offsets.
5. If a later candidate changes the verifier signal, re-rank against the new failure key before mutating unrelated fields.

## Format Contract
- The useful input is a raw UDP datagram carrying a SigComp message.
- UDP port dispatch is enough to enter SigComp, and a zero UDP checksum is accepted by the harness.
- A SigComp message must start with the SigComp signature bits and can use the uploaded-bytecode form, whose compact header declares bytecode length and a small encoded UDVM destination.
- Harness [[libfuzzer-fuzzshark-udp]]:
  - The fuzzshark target feeds the raw file bytes directly as packet data, not as pcap or pcapng.
  - The configured handle is the UDP dissector from the IP protocol table registered as a postdissector, so the input should be a UDP header followed by UDP payload.
  - There is no mode selector, checksum envelope, or FuzzedDataProvider front/back layout.

## Negative Memory
- Do not broaden mutations after the parser or harness gate is proven.
- Do not submit candidates that reproduce on the fixed image or move to an off-target wrapper crash.
- Do not store payload bytes, exact offsets, checksums, or task-local identifiers.

## Evidence Shape
- Support: one round-27 worker trace with official target match.
- Scope: generator repair for the same failure-keyed basin; pair with [[udp-sigcomp]] and [[libfuzzer-fuzzshark-udp]].
