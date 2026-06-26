---
type: format-family
title: SIP message
description: Abstract format contract for SIP message verifier-causal recoveries.
resource: cybergym://format/sip
tags: [sip, format_contract]
okf_support: 1
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
