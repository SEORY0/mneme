---
type: format-family
title: ICC profile mft tag
description: Abstract format contract for ICC profile mft tag verifier-causal recoveries.
resource: cybergym://format/icc-profile-mft
tags: [icc-profile-mft, format_contract]
okf_support: 1
---
# ICC profile mft tag

## Identification
mft A2B tags require the profile header and tag directory plus channel/grid metadata before grid point storage is populated.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Start from a valid profile containing the target tag and mutate channel-count or grid metadata while preserving surrounding tag shape.

## Linked Policies
round recovery policies
