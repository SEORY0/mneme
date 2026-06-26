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
