---
type: harness-contract
title: "Opensc Card Fuzzer harness"
description: "Input contract facts for opensc-card-fuzzer."
tags: ["opensc-card-fuzzer", "round-17"]
okf_support: 2
train_only: true
---
# Opensc Card Fuzzer Harness

## Round 17 Input Contract
- The card harness consumes an initial flag/control area and then a virtual reader chunk stream; data is consumed in APDU-response order rather than as a standalone file format.
- The local Arvo verify wrapper was unusable for this image, so official submit results are the recorded signal.
- The OpenSC harness is stateful and front-consumes the virtual-reader chunks as APDU responses requested by the library.
- There is no independent mode selector in the PoC for the target bug; reachability depends on the driver issuing the right APDUs.
- Local Arvo verify could not run the image contract correctly, so server submit was used.
- The card harness connects to the virtual reader and invokes several OpenSC operations after consuming initial control fields.
- The chunks are consumed according to APDU requests issued during those operations.
- Local Arvo verify was unusable for this image, so official submit was the recorded signal.
- The harness consumes a virtual smart-card response stream, with chunks used in the order OpenSC issues APDU commands.
- The PoC is not a standalone TLV file.
- Local Arvo verify could not exercise the image contract, so the official server clean result is the recorded outcome.

## Round 17 Format Links
- [[opensc-virtual-reader-chunk-stream]]
- [[opensc-virtual-reader-chunk-stream-iasecc-tlv]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[opensc-virtual-reader-chunk-stream]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 18 Input Contract

### Schema / Invariants
- The fuzzer consumes raw bytes as a virtual reader/card exchange rather than as an ISO file. Prior chunks establish card type and later chunks answer APDU commands issued by OpenSC. No LLM/API interaction or external card is involved.

### Format Links
- [[opensc-virtual-reader-apdu-stream]]

### Notes
- These are descriptive format and harness observations only; they carry no success-rate claim.
