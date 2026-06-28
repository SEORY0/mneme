---
type: harness-contract
title: "Afl Style Fuzzshark Ip harness"
description: "Round 23 input contract facts for afl-style-fuzzshark-ip."
tags: ["afl-style-fuzzshark-ip", "round-23"]
okf_support: 1
train_only: true
---
# Afl Style Fuzzshark Ip Harness

## Round 23 Input Contract
- The active binary is configured for the IP dissector and disables several protocols including UDP. TCP payload dispatch by port can still reach SNMP from the IP harness; bare BER and UDP-carried SNMP do not reach the target path here.

## Round 23 Format Links
- [[wireshark-fuzzshark-ip-snmp]]

## Round 23 Notes
- These are descriptive harness-carving facts only; they carry no success-rate claim.
