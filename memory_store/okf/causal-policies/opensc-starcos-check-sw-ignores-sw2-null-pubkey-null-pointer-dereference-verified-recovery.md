---
type: causal-policy
title: "OpenSC Starcos Check SW Ignores SW2 Null Pubkey Null Pointer Dereference Verified Recovery"
description: "Verified recovery for no_crash where starcos_check_sw accepts SW1==0x90 ignoring SW2, leaving a NULL public-key modulus that is later encoded."
failure_class: "no_crash"
verifier_signal: "reached_status_word_misaccept_null_value"
candidate_family: "construct"
input_format: "smartcard-apdu-trace"
harness_convention: "opensc-pkcs15init-fuzzer"
vuln_class: "null-pointer-dereference"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "construct", "smartcard-apdu-trace", "null-pointer-dereference", "status-word", "verified-recovery"]
match_keys: ["no_crash", "reached_status_word_misaccept_null_value", "smartcard-apdu-trace", "opensc-pkcs15init-fuzzer", "null-pointer-dereference", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# OpenSC Starcos Check SW Ignores SW2 Null Pubkey Null Pointer Dereference Verified Recovery

## Policy
For `no_crash` on the OpenSC `pkcs15init` fuzzer, the bug is in `starcos_check_sw`: it treats ANY SW1==0x90
as success regardless of SW2, so an operation whose status word is `0x90 0x01` is mis-accepted. The caller
then proceeds with an unpopulated value — here a generated RSA public key whose modulus is `data=NULL,
len=128` — and a later encode step (`sc_pkcs15_encode_pubkey_rsa` -> `BN_bin2bn`) reads through NULL. The fix
requires `sw1==0x90 && sw2==0x00`.

## Procedure
1. The harness replays a scripted **virtual-card APDU trace**. Provide a STARCOS generic ATR + a profile with
   ACL = NONE so key generation is permitted without auth.
2. Drive the flow to `do_generate_key` for an RSA-1024 key; script the GENERATE KEY APDU to return status
   word `0x90 0x01` (SW1=success, SW2 nonzero) so `starcos_check_sw` mis-accepts it and the public key is
   left with a NULL modulus buffer.
3. The subsequent public-key encode dereferences the NULL modulus -> SEGV NULL read in the crypto encode.
   Minimum-margin: a valid trace that only differs by the one mis-accepted SW2. Confirm fix exits 0
   (it rejects SW2!=0 and aborts cleanly).

## Format Contract
- See [[smartcard-apdu-trace]]. The fuzzer input is a sequence of card responses (ATR + per-APDU SW/data);
  reaching the bug needs a profile/ACL that allows key generation and an RSA-1024 generate path.

## Negative Memory
- Do not return a clean `0x90 0x00` (no mis-accept; stays no_crash) and do not return an error SW (aborts
  before the encode).
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).
