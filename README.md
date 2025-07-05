# 🛡️ NetGuardian: Real-Time Intrusion Detection Dashboard

NetGuardian is a real-time network intrusion detection system (IDS) with a live interactive dashboard. It monitors incoming network packets, detects suspicious activity like port scans and large payloads, and displays live alerts using Streamlit.

## 🚀 Features
- Real-time packet sniffing using Scapy
- Detection of port scans, suspicious ports, and large payloads
- Desktop notifications on intrusion
- Streamlit dashboard with live logs and charts
- Intrusion simulator for testing
## 💻 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Set your network interface
In `packet_sniffer.py`, update:
```python
interface_to_use = "Wi-Fi"  # or "eth0", "wlan0", etc.
```

### 3. Start the IDS
```bash
streamlit run app.py
```
This launches the dashboard at `http://localhost:8501` and starts capturing packets.

### 4. Optional: Simulate an attack
```bash
python intrusion_simulator.py
```
### 5. detct the attack
```bash
python detector.py
```
## 📊 Dashboard
- Click **Start IDS** to begin monitoring
- View alerts in a live table and chart
- Filter by intrusion reason

## 🧠 Detection Rules
- **Suspicious ports**: e.g., 22, 23, 3306, 445, etc.
- **Large payloads**: >1400 bytes
- **Port scans**: rapid access to multiple ports

## 🔔 Alerts
- Desktop pop-ups via Plyer
- Logged to `data/logs.csv`
- Shown in the Streamlit dashboard

## 📌 Notes
- Run as Administrator/root to sniff packets
- Works on local and Wi-Fi networks

## ⚠️ Legal Notice
This tool is intended only for authorized testing and educational purposes.
