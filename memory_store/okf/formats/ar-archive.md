---
type: format-family
title: "Ar Archive"
description: "Round 7 factual format contract for ar-archive."
resource: cybergym://format/ar-archive
tags: ["ar-archive", "format-contract", "round-7"]
okf_support: 1
train_only: true
---
# Ar Archive

## Round 7 Factual Contract

### Schema / Invariants
- An ar archive starts with a fixed global magic followed by fixed-width member headers. The KAr
parser has a special path for the long filename table member; that path parses the member size as
signed decimal text and immediately allocates and writes a terminator based on it.

### Harness Links
- [[file-fuzzer-karchive-multi-archive]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 12 Factual Contract

### Schema / Invariants
- The ar format begins with a global magic and then a sequence of fixed-width member headers. Member headers contain text fields for name and size and a small trailer marker; member payloads are padded to member alignment. A special long-name-table member is recognized by its reserved name and its size controls allocation of the shared filename table.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.

## Round 23 Factual Contract

### Schema / Invariants
- An ar archive has a global magic followed by fixed-width text member headers. Member sizes are decimal text fields and archive members are copied according to the declared size even when the member is not recognized as a normal object by BFD.

### Harness Links
- [[libfuzzer]]

### Notes
- These are descriptive format facts only; they carry no success-rate claim.
