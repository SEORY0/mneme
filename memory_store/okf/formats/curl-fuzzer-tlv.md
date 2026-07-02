---
type: format-family
title: "Curl Fuzzer Tlv format"
description: "Round 8 descriptive format facts for curl-fuzzer-tlv."
resource: cybergym://format/curl-fuzzer-tlv
tags: ["curl-fuzzer-tlv", "round-8"]
okf_support: 2
---
# Curl Fuzzer Tlv Format

## Round 8 Factual Contract

### Schema / Invariants
- The curl fuzzer input is a sequence of big-endian TLVs. One TLV supplies the URL, response TLVs supply staged server replies, and optional TLVs supply credentials, headers, upload data, or protocol options. Ping-pong protocols consume response slots as simulated socket reads.

### Harness Links
- [[afl-file-wrapper]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 32 Factual Contract

### Schema / Invariants
- The curl fuzzer stream is a sequence of big-endian tag-length-value records. One record supplies the URL, ordered response records emulate server replies, an FTP secondary-socket response supplies passive data-channel bytes, and option records can toggle behaviors such as wildcard matching. FTP response slots are consumed by protocol phase, not merely by record order in the file.

### Harness Links
- [[libfuzzer]]

### Notes
- These facts are descriptive format observations only; they are not causal recovery claims.
