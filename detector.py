def detect_intrusion(packet):
    print(f"Checking packet: {packet}")  # Debug line
    suspicious_ports = [22, 3389]
    if packet['port'] in suspicious_ports or packet['payload_size'] > 1400:
        print("Intrusion Detected!")     # Debug line
        return True, "Suspicious port or payload size"
    return False, "Normal"

