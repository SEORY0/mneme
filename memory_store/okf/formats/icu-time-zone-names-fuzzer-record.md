---
type: format-family
title: "ICU Time Zone Names Fuzzer Record Format"
description: "Round 27 descriptive format facts for icu-time-zone-names-fuzzer-record."
resource: cybergym://format/icu-time-zone-names-fuzzer-record
tags: ["icu-time-zone-names-fuzzer-record", "round-27"]
okf_support: 1
---
# ICU Time Zone Names Fuzzer Record Format

## Round 27 Factual Contract

- The time-zone-names input starts with a locale selector, then a UDate value, then a UTimeZoneNameType value, followed by the remaining bytes interpreted as UTF-16 text.
- The text is reused as both time-zone ID and metazone/display-name input across TimeZoneNames and TZDBTimeZoneNames methods.
- Valid enum masks select long, short, standard, daylight, generic, or exemplar-name lookup paths.

### Harness Links
- [[libfuzzer-icu-time-zone-names]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
