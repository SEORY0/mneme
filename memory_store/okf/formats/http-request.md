---
type: format-family
title: http-request format
description: Structure and reachability facts for http-request inputs.
tags: [http-request]
okf_support: 0
---
# Http Request Format

## Round 10 Factual Contract

### Schema / Invariants
- The request parser accepts a normal method, path, version line followed by repeated header lines and a blank line terminator. Each parsed header contributes boundary metadata, so header count is the controlling structure rather than body content.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 17 Factual Contract

### Schema / Invariants
- The parser expects a method, path, version line, header lines, and a blank-line terminator.
- Header dispatch first groups by a short prefix and then applies per-header name and separator checks before storing header values.

### Harness Links
- [[afl-libfuzzer-raw-request-parser]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
