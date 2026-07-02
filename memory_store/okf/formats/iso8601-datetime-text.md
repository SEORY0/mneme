---
type: format-family
title: "Iso8601 Datetime Text format"
description: "Round 28 descriptive format facts for iso8601-datetime-text."
resource: cybergym://format/iso8601-datetime-text
tags: ["iso8601-datetime-text", "round-28"]
okf_support: 0
---
# Iso8601 Datetime Text Format

## Round 28 Factual Contract

### Schema / Invariants
- The accepted input is plain ISO-8601 date-time text: supported dates include calendar, ordinal, and week forms; the time component is hour/minute/seconds with optional fractional digits; a timezone suffix or default timezone is required. The seconds parser accepts only decimal digits with an optional decimal separator and fractional digit run, so literal NaN tokens are rejected before the constructor.

### Harness Links
- [[afl-libfuzzer-raw-file]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
