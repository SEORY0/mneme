---
type: harness-contract
title: "Libprotobuf Mutator Nginx Http Request Fuzzer"
description: "Round 36 factual harness contract for libprotobuf-mutator-nginx-http-request-fuzzer."
tags: ["libprotobuf-mutator-nginx-http-request-fuzzer", "round-36", "harness-contract"]
okf_support: 1
train_only: true
---
# Libprotobuf Mutator Nginx Http Request Fuzzer

## Round 36 Input Contract
- The generated wrapper runs an nginx HTTP request fuzzer over one text-format protobuf input file. The fuzzer initializes nginx with a Unix listener and an HTTP/1.1 proxy-oriented configuration, then services request and reply data through custom recv handlers. It passes protobuf strings through C-string length handling rather than using protobuf byte lengths.

## Round 36 Format Links
- [[text-format-protobuf-http-request]]

## Round 36 Notes
- These are descriptive harness-carving facts from round 36; they are not causal recovery claims.
