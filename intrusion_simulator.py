from scapy.all import IP, TCP, send
import time

def simulate_intrusion(dst_ip="127.0.0.1", port=22, size=1600, count=5):
    print(f"[+] Sending {count} fake intrusion packets to {dst_ip}:{port}")

    for i in range(count):
        pkt = IP(dst=dst_ip)/TCP(dport=port)/("X"*size)
        send(pkt, verbose=False)
        print(f"  > Packet {i+1} sent (port={port}, size={size})")
        time.sleep(1)

if __name__ == "__main__":
    simulate_intrusion()
