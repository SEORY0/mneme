---
type: causal-policy
title: Bluetooth HCI UART Downcast Recovery
description: Recover HCI UART object-type crashes by delivering complete packets through the callback path.
failure_class: wrong_sink
verifier_signal: parser_reached_sink_mismatch
candidate_family: construct
input_format: bluetooth-hci-uart
harness_convention: uart-transport-fuzzer
vuln_class: undefined-behavior-invalid-downcast
access_scope: generate
success_count: 1
confidence: medium
tags: [wrong_sink, parser_reached_sink_mismatch, bluetooth, hci_uart, downcast]
match_keys: [wrong_sink, parser_reached_sink_mismatch, bluetooth-hci-uart, callback_downcast]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: medium
train_only: true
---
## Policy
For HCI UART transport tasks, complete packet framing and callback dispatch are the reachability gates. The target path is not a malformed length alone, but a callback that obtains a singleton stream through an incompatible reader-writer conversion.

## Procedure
1. Build complete HCI UART packets with valid packet indicators.
2. Keep length fields self-consistent so the packet callback runs.
3. Select the packet kind that reaches the stream callback path.
4. Avoid truncation that stops before callback dispatch.
5. Submit parser-reached downcast or undefined-behavior crashes even if local sink naming is indirect.

## Negative Memory
- Do not fuzz incomplete UART records for object-type bugs.
- Do not desynchronize packet lengths before the callback is observed.
- Do not treat packet parser rejection as progress.
