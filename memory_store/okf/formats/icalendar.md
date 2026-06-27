---
type: format-family
title: iCalendar component format
description: Format contract for calendar components with GEO properties.
resource: cybergym://format/icalendar
tags: [icalendar, calendar, geo, text-expr]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
The carrier is a syntactically valid calendar component with properties. GEO values contain a pair of numeric-looking coordinate components.

## Invariants
- The component wrapper must be valid before property conversion runs.
- A valid first GEO coordinate can gate the vulnerable converter.
- Oversizing the second coordinate is useful only while it remains syntactically numeric enough for conversion.

## Round 11 Factual Contract

### Schema / Invariants
- iCalendar data is line-oriented and commonly wrapped in BEGIN:VCALENDAR and END:VCALENDAR. REQUEST-STATUS values use semicolon-separated status code, description, and optional debug text. A trailing separator yields an empty debug string candidate in the request-status parser.

### Harness Links
- [[libfuzzer]]

### Notes
- These are factual format and harness observations only; they carry no success-rate claim.
