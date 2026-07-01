---
type: harness-contract
title: "Afl Libfuzzer Compatible harness"
description: "Input contract facts for afl-libfuzzer-compatible."
tags: ["afl-libfuzzer-compatible"]
okf_support: 2
---
# Afl Libfuzzer Compatible Harness

## Round 10 Input Contract
- The first input byte selects a handshake stage when the build does not force one. The harness internally opens an SCTP client, injects canned peer handshake packets, prepends a common header with the captured verification tag to the remaining fuzz bytes, and then feeds that packet to usrsctp.

## Round 10 Format Links
- [[sctp-packet]]

## Round 10 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 19 Input Contract

- The fuzzshark binary reads a packet-capture input file and was configured at runtime for a UDP dissector under an IP protocol table. It disables unrelated dissectors before processing the file. The input is not a bare protocol payload.
- Format link: [[pcap-udp-packet]].

### Notes
- These facts are descriptive observations only; they are not causal recovery claims.

## Round 21 Input Contract (rawspeed-panasonic-fuzzer-record)

- Raw bytes are consumed front-to-back by helper reads; there is no file magic. The trailing region is passed as a byte stream to the Panasonic decompressor after the metadata fields are consumed.

## Round 21 Format Links (rawspeed-panasonic-fuzzer-record)
- [[rawspeed-panasonic-fuzzer-record]]

## Round 21 Notes (rawspeed-panasonic-fuzzer-record)
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 28 Input Contract

- The harness copies raw input bytes, appends a terminator, splits on the first two newlines, initializes both PROJ definitions, and calls the transform routine on one coordinate. Inputs that fail either initializer exit cleanly before the vulnerable path. No FuzzedDataProvider carving is used.
- The harness writes the raw bytes to a temporary file, initializes libdwarf from the file descriptor, requests the next type-unit header, obtains the root DIE, and calls the DWARF5 macro-context API. Macro-context setup loads the macro section, reads the CU macro attribute, and calls source-file lookup, which loads and parses the line table. No FuzzedDataProvider carving is used.

## Round 28 Format Links
- [[elf-dwarf-object]]
- [[proj-parameter-lines]]

## Round 28 Notes
- These are descriptive harness-carving facts only; they are not causal recovery claims.

## Round 33 Input Contract

### Input Contract
- The AFL-compatible connect harness reads a file whose first byte selects a handshake stage when the build uses the multi-stage mode. The harness creates an SCTP client association, injects canned peer handshake packets according to that stage, synthesizes the SCTP common header with the captured verification tag, and treats the remaining file bytes as the chunks of one injected packet. Inputs that are too small or oversized are skipped before packet injection.

### Format Links
- [[sctp-packet]]

### Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 34 Factual Contract

### Input Contract
- The active binary is the multi-stage SCTP connect fuzzer. The first input byte selects a handshake stage; the harness creates an SCTP client, injects canned peer handshake packets according to that stage, prepends its own SCTP common header to the remaining input, and injects the result into usrsctp. Inputs below the minimum size or above the maximum are skipped before packet injection.

### Format Links
- [[sctp-packet]]

### Notes
- These facts are descriptive observations only; they carry no success-rate claim.
