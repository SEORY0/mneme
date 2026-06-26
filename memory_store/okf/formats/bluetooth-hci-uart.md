---
type: format-family
title: Bluetooth HCI UART packet stream
description: Format contract for UART packet streams that dispatch through HCI callbacks.
resource: cybergym://format/bluetooth-hci-uart
tags: [bluetooth, hci, uart, packet]
timestamp: 2026-06-26T00:00:00Z
okf_support: 1
train_only: true
---
# Schema
## Structure
The input is a sequence of HCI UART packets with packet indicators and self-consistent lengths. Packet callbacks run only after the transport parser accepts a complete packet.

## Invariants
- Complete packet framing is required before stream object bugs are reachable.
- Length desynchronization too early prevents callback dispatch.
- Packet kind selection controls which callback path runs.
