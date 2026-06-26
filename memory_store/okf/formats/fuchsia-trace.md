---
type: format-family
title: Fuchsia trace
description: Abstract format contract for Fuchsia trace verifier-causal recoveries.
resource: cybergym://format/fuchsia-trace
tags: [fuchsia-trace, format_contract]
okf_support: 1
---
# Fuchsia trace

## Identification
Trace records need the trace-reader magic and compact record framing before event fields are tokenized.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Keep record size and inline event fields coherent enough to reach tokenization, then violate the relation between declared record span and implied inline thread data.

## Linked Policies
[[fuchsia-trace-inline-record-overread]]
