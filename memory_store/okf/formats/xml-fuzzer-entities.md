---
type: format-family
title: XML fuzzer entities
description: Abstract format contract for XML fuzzer entities verifier-causal recoveries.
resource: cybergym://format/xml-fuzzer-entities
tags: [xml-fuzzer-entities, format_contract]
okf_support: 1
---
# XML fuzzer entities

## Identification
The XML entity fuzzer uses an options/envelope layer before the document; XInclude and fallback processing only matter after that wrapper selects the right parser mode.

## Structure
Keep the earliest magic, wrapper, declared length, mode selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Keep the fuzzer envelope valid, enable the entity/XInclude mode needed by the target, then make fallback ownership visible during serialization.

## Linked Policies
round recovery policies
