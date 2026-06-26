---
type: format-family
title: NDR CAB carrier
description: Abstract format contract for NDR CAB carrier verifier-causal recoveries.
resource: cybergym://format/ndr-cab
tags: [ndr-cab, format_contract]
okf_support: 1
---
# NDR CAB carrier

## Identification
The generic NDR fuzzer needs a public-structure selector before CAB compression state is initialized.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Select the CAB public-structure path and keep compressed-chunk shape valid enough for setup and teardown ownership to run.

## Linked Policies
[[ndr-cab-compression-state-uaf]]
