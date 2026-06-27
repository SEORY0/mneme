---
type: format-family
title: SIP message
description: Abstract format contract for SIP message verifier-causal recoveries.
resource: cybergym://format/sip
tags: [sip, format_contract]
okf_support: 2
---
# SIP message

## Identification
SIP parsers first gate on raw message size and request/status line shape, then walk headers and folded whitespace.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Use a plausible start line or intentional leading whitespace basin according to the target; keep malformed endings narrow enough not to crash both builds.

## Linked Policies
[[sip-leading-linebreak-overread]]; [[sip-content-length-folded-boundary]]

## Round 7 Factual Contract

### Schema / Invariants
- The SIP parser accepts a request line followed by colon-delimited headers. Well-known From/To
headers are parsed eagerly; To parameters begin after a semicolon and support quoted parameter
values with backslash escapes. A complete message body is not required for the To parser to run.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 15 Factual Contract

### Schema / Invariants
- A SIP request needs a request line, headers, CRLF line endings, and an empty line terminator. The To
  header accepts address parameters after semicolons; parameter names and values are separated by an
  equals sign, and quoted parameter values use backslash escapes.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
