---
type: harness-contract
title: "Libfuzzer Fuzzshark harness"
description: "Input contract facts for libfuzzer-fuzzshark."
tags: ["libfuzzer-fuzzshark", "round-17"]
okf_support: 1
train_only: true
---
# Libfuzzer Fuzzshark Harness

## Round 17 Input Contract
- The fuzzshark harness gives libFuzzer bytes to Wireshark packet/dissector machinery as raw input for the configured target; it is not a FuzzedDataProvider stream.
- The local Arvo verify wrapper could not exercise these images because the image expected a PoC directory where the wrapper mounted a file, so official submit was used for outcome measurement.
- The harness routes libFuzzer bytes directly into Wireshark packet dissection for the selected dissector.
- It is not a FuzzedDataProvider contract and did not require a pcap wrapper for the solving candidate.
- Local Arvo verify was unavailable because of the PoC mount contract, so official submit provided the success signal.

## Round 17 Format Links
- [[asn1-ber-like-dissector-payload]]
- [[raw-ipv4-tcp]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.

## Round 17 Format Links
- [[asn1-ber-like-dissector-payload]]

## Round 17 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
