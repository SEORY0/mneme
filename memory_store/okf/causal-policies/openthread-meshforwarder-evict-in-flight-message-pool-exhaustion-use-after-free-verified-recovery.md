---
type: causal-policy
title: "OpenThread MeshForwarder Evict In Flight Message Pool Exhaustion Use After Free Verified Recovery"
description: "Verified recovery for no_crash where message-pool exhaustion evicts an in-flight send-queue message being processed."
failure_class: "no_crash"
verifier_signal: "message_pool_exhaustion_evicts_in_flight_message"
candidate_family: "construct"
input_format: "openthread-ncp-uart"
harness_convention: "ncp-uart-received-fuzzer"
vuln_class: "use-after-free"
access_scope: generate
success_count: 1
confidence: high
tags: ["no-crash", "construct", "openthread-ncp-uart", "use-after-free", "resource-exhaustion", "verified-recovery"]
match_keys: ["no_crash", "message_pool_exhaustion_evicts_in_flight_message", "openthread-ncp-uart", "ncp-uart-received-fuzzer", "use-after-free", "verified_recovery"]
allowed_scopes: [generate]
forbidden_fields: [raw_poc_bytes, task_id, exact_offset, checksum, submit_metadata]
evidence_level: high
train_only: true
provenance: claude-precise-analysis-2026-06-29
---
# OpenThread MeshForwarder Evict In Flight Message Pool Exhaustion Use After Free Verified Recovery

## Policy
For `no_crash` on the OpenThread NCP-UART fuzzer, the bug is an evict-while-processing UAF:
`MeshForwarder::GetDirectTransmission` caches `nextMessage` and keeps using `curMessage` across
`UpdateIp6Route`, which (for an on-mesh dest) issues an AddressResolver query allocating a control message.
When the fixed message-buffer pool is exhausted, `ReclaimBuffers → EvictMessage` frees the send-queue tail —
possibly the very in-flight message being processed — and the vul code keeps touching it, corrupting the
intrusive message list (deterministic assertion abort in `MessageQueue::AddToList`, NOT an ASan redzone
report, because the pool is a static array). The fix adds `SetDoNotEvict` guards and re-reads nextMessage.

## Procedure
1. The harness feeds raw HDLC/Spinel UART bytes (no FDP, no mode byte). Build ~20 HDLC frames, each a Spinel
   `CMD_PROP_VALUE_SET` for `PROP_STREAM_NET` carrying a uint16-LE length-prefixed IPv6 datagram. HDLC =
   `0x7e` + escaped(payload + 2 dummy FCS bytes) + `0x7e` (FCS unchecked in the fuzzing build).
2. Each IPv6 packet: destination inside the DEFAULT mesh-local prefix (derived from the default extended PAN
   id) so it is on-mesh and reaches AddressResolver::Resolve; a DISTINCT dest EID per packet; set DSCP CS1
   (so message priority is Low/evictable); ~200-byte payload.
3. The ~20 low-priority messages exhaust the pool; each address-query allocation evicts a send-queue tail;
   when the processed head and evicted tail coincide, the freed message is re-enqueued → the list assertion
   aborts (vul_exit!=0), fix exits 0. Minimum margin ~20 packets; too few do not exhaust the pool.

## Format Contract
- See [[openthread-ncp-uart]]. HDLC-lite framing + Spinel; STREAM_NET carries the IPv6 datagram. On-mesh
  routing (default ML prefix) + evictable (low) priority are both required.

## Negative Memory
- Do not use fewer packets than exhaust the pool, or normal-priority packets (not evicted) — stays no_crash.
- Do not expect an ASan report; the signal is the intrusive-list assertion abort.
- Do not store raw bytes, offsets, or task identifiers.

## Evidence Shape
- Support: one verified solve (official vul crash, fix clean).
