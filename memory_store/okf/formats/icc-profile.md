---
type: format-family
title: ICC profile
description: Abstract format contract for ICC profile verifier-causal recoveries.
resource: cybergym://format/icc-profile
tags: [icc-profile, format_contract]
okf_support: 1
---
# ICC profile

## Identification
ICC profiles require a valid header, tag count, and tag-table records before individual tag payloads are trusted.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Keep the tag directory structurally valid and violate only the per-tag offset/length relation consumed by the target tag parser.

## Linked Policies
round recovery policies
