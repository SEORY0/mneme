---
type: format-family
title: http-request format
description: Structure and reachability facts for http-request inputs.
tags: [http-request]
okf_support: 3
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

## Round 33 Factual Contract

### Schema / Invariants
- The input is an HTTP request: method, path, version, header lines, and a blank-line terminator. Known request headers are parsed by matching a short case-insensitive prefix first, then advancing over the expected full header name and checking for a name/value separator. Header discovery records line starts and ends in a fixed-size helper table before recognized headers are interpreted.
- The input is a raw HTTP request: a request line with method, path, and HTTP version, followed by CRLF-delimited headers and a blank-line terminator. Header values are parsed by matching known header names and splitting at the line terminator. If-Modified-Since is expected to contain an RFC-style date string with fixed weekday, day, month, year, time, and GMT fields; malformed or short values can be recorded as a header value before the date parser rejects them.
- The Lwan request parser expects a method, path, HTTP version, header lines, and a blank-line terminator. Its fuzz finalizer treats the terminator as evidence of a complete request unless the terminator is at the initial buffer position, while the later parser first ignores leading HTTP whitespace before method identification.

### Harness Links
- [[afl-libfuzzer-raw-request-parser]]
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
