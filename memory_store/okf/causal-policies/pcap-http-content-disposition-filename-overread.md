---
type: causal-policy
title: PCAP HTTP Content-Disposition Filename Overread Recovery
description: Verified recovery for wrong_sink with sanitizer_crash on pcap-http inputs.
failure_class: wrong_sink
verifier_signal: sanitizer_crash
candidate_family: construct
input_format: pcap-http
harness_convention: libfuzzer
vuln_class: heap-buffer-overflow-read
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong-sink, sanitizer-crash, construct, pcap-http, heap-buffer-overflow-read, verified-recovery]
match_keys: [wrong-sink, sanitizer-crash, pcap-http, heap-buffer-overflow-read]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
---
# PCAP HTTP Content-Disposition Filename Overread Recovery

- key: `wrong_sink x sanitizer_crash`
- outcome: verified recovery
- success_count: 1
- failure_count: 0
- formats: [[pcap-http]]

## Failure Shape
Use a valid packet-capture envelope carrying Ethernet, IPv4, TCP, and an HTTP response. The
response selects the HTTP content-inspection branch and uses malformed Content-Disposition
filename quoting so filename length arithmetic overreads during content classification.

## Policy
For `wrong_sink x sanitizer_crash` on `pcap-http`, preserve the parser and harness gate first, then mutate
only the causal invariant described by the verified trace. Prefer the candidate family `construct`
when the carrier is available because this shape was server-confirmed against vulnerable and fixed
builds.

## Procedure
1. Preserve the packet-capture header and a coherent Ethernet, IPv4, and TCP response flow.
2. Use an HTTP response that enters content-inspection, not just generic TCP decoding.
3. Malformed Content-Disposition filename quoting should violate filename length arithmetic
during classification.
4. When local verify reports a sanitizer wrong sink, submit if the response clearly reaches the
content classifier.

## Verifier Contract
The local signal may remain coarse. Keep candidates that reach the named parser or sink and
use the official vulnerable-versus-fixed comparison as the target-match gate.

## Negative Memory
- Do not mutate packet headers after HTTP classification is reached.
- Do not rely on unrelated HTTP headers; the overread is tied to filename quoting and length
arithmetic.
- Never store raw payload bytes, exact offsets, checksums, or task-local identifiers in memory.

## Evidence Shape
- Support: 1 server-verified solve.
- Scope: generator repair only.
