---
type: format-family
title: WebVTT
description: Abstract format contract for WebVTT verifier-causal recoveries.
resource: cybergym://format/webvtt
tags: [webvtt, format_contract]
okf_support: 1
---
# WebVTT

## Identification
A WebVTT input needs the signature and cue/header line grammar before subtitle comment or cue text buffers are populated.

## Structure
Keep the earliest magic, wrapper, declared length, mode selector, and terminator fields coherent enough to reach the target parser. Avoid whole-file corruption until parser reachability is proven.

## Build Contract
Use a valid signature and ordinary cue structure; make the long line semantic live before the cue parser copies it.

## Linked Policies
[[webvtt-overlong-comment-line]]
