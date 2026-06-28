---
type: format-family
title: "AAC USAC format"
description: "Round 8 descriptive format facts for aac-usac."
resource: cybergym://format/aac-usac
tags: ["aac-usac", "round-8"]
okf_support: 2
---
# AAC USAC Format

## Round 8 Factual Contract

### Schema / Invariants
- The accepted input is a raw AAC/USAC decoder stream, not an outer length-prefixed harness format. The XAAC decoder fuzzer decides ADTS mode from the first bytes, initializes the decoder, configures it with the same input buffer, then repeatedly decodes frames. Reaching this bug requires a USAC configuration with SBR ratio enabled and a parsed channel count that reaches decoder-create and SBR initialization.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 15 Factual Contract

### Schema / Invariants
- The decoder accepts raw AAC/USAC streams, including streams with MPEG surround configuration. MPS
  configuration carries normal and residual sampling-frequency index state, and corpus samples with
  MPS payloads reach the residual processing code more reliably than hand-built byte envelopes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
