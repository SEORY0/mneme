---
type: format-family
title: Keybox blob
description: Abstract format contract for Keybox blob verifier-causal recoveries.
resource: cybergym://format/kbx
tags: [kbx, format_contract]
okf_support: 1
---
# Keybox blob

## Identification
A keybox-style carrier is header driven: the blob header must place the keyblock inside the accepted range before PGP parsing consumes it.

## Structure
Keep the earliest magic, wrapper, declared length, mode selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Keep offsets internally plausible and move the failure into wrapped span arithmetic between accepted range and later keyblock reader.

## Linked Policies
[[kbx-keyblock-length-wrap]]
