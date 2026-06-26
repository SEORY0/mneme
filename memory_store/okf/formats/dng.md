---
type: format-family
title: DNG/TIFF image
description: Abstract format contract for DNG/TIFF image verifier-causal recoveries.
resource: cybergym://format/dng
tags: [dng, format_contract]
okf_support: 1
---
# DNG/TIFF image

## Identification
DNG inherits TIFF byte order, IFD tags, strip metadata, and baseline image fields before raw decoder metadata is consumed.

## Structure
Keep the earliest magic, wrapper, declared length, selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Build a minimal valid TIFF/DNG carrier and move the failure into a metadata table size consumed after image decode setup.

## Linked Policies
[[dng-linearization-table-capacity]]
