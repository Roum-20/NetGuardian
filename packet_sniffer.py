from scapy.all import sniff, IP, TCP, UDP
import time
from collections import deque

def parse_packet(packet):
    if IP in packet:
        ip = packet[IP]
        transport = packet[TCP] if TCP in packet else packet[UDP] if UDP in packet else None
        return {
            "source_ip": ip.src,
            "destination_ip": ip.dst,
            "port": transport.dport if transport else 0,
            "payload_size": len(packet),
            "timestamp": time.time()
        }

def packet_stream():
    buffer = deque()

    def sniff_callback(pkt):
        parsed = parse_packet(pkt)
        if parsed:
            buffer.append(parsed)

    sniff(prn=sniff_callback, store=0, filter="ip", iface=None, timeout=0)

    while True:
        if buffer:
            yield buffer.popleft()
        else:
            time.sleep(0.1)
