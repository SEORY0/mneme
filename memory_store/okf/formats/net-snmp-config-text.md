---
type: format-family
title: "net-snmp-config-text format"
description: "Structure and reachability facts for net-snmp-config-text."
resource: cybergym://format/net-snmp-config-text
tags: ["net-snmp-config-text"]
okf_support: 1
---
# Net Snmp Config Text Format

## Round 9 Factual Contract

### Schema / Invariants
- The accepted input is Net-SNMP configuration text: line-oriented tokens with whitespace-separated
  arguments.
- Packet envelopes such as AgentX or BER SNMP messages are treated as config tokens and do not reach
  packet parsers under this wrapper.

### Harness Links
- [[afl-file-fuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 22 Factual Contract

### Schema / Invariants
- Net-SNMP configuration input is plain text split into directive lines. Directive keywords select handlers and the rest of the line is parsed as arguments. File-reference directives route through path construction logic that combines configured directories with user-supplied path text.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
