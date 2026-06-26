---
type: format-family
title: PCAP HTTP format
description: Structure and bug-prone gates for PCAP HTTP flow inputs.
resource: cybergym://format/pcap-http
tags: [pcap-http, construct, heap-buffer-overflow-read]
okf_support: 1
---
# Schema
## Structure
HTTP content-inspection bugs through packet capture need a valid capture envelope,
Ethernet/IP/TCP framing, and an HTTP response that selects the content classifier. The
trigger is malformed filename quoting in Content-Disposition metadata.

## Round 5 Verified Contracts
- [[pcap-http-content-disposition-filename-overread]]: Use a valid packet-capture envelope carrying Ethernet, IPv4, TCP, and an HTTP response. The
response selects the HTTP content-inspection branch and uses malformed Content-Disposition
filename quoting so filename length arithmetic overreads during content classification.

# Examples
- Support: 1 server-verified solve.
- Winning strategies observed: construct.
- Abstract sink shape observed: heap-buffer-overflow-read.

# Citations
- Distilled from server-verified training outcomes with this format family.
