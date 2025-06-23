import csv
import os
from plyer import notification
import smtplib
from email.message import EmailMessage

LOG_FILE = 'data/logs.csv'

def system_alert(title, message):
    notification.notify(title=title, message=message, timeout=5)

def send_email_alert(packet, reason):
    try:
        sender = "your_email@gmail.com"
        password = "your_app_password"
        receiver = "receiver_email@example.com"

        msg = EmailMessage()
        msg['Subject'] = '🚨 IDS ALERT: Intrusion Detected'
        msg['From'] = sender
        msg['To'] = receiver
        msg.set_content(f"""
        Alert Reason: {reason}
        Source IP: {packet['source_ip']}
        Destination IP: {packet['destination_ip']}
        Port: {packet['port']}
        Payload Size: {packet['payload_size']}
        Timestamp: {packet['timestamp']}
        """)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
    except Exception as e:
        print(f"Email failed: {e}")

def log_alert(packet, reason):
    os.makedirs('data', exist_ok=True)
    exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(['timestamp', 'source_ip', 'destination_ip', 'port', 'payload_size', 'reason'])
        writer.writerow([packet['timestamp'], packet['source_ip'], packet['destination_ip'],
                         packet['port'], packet['payload_size'], reason])
    system_alert("Intrusion Detected", f"{packet['source_ip']} → {packet['destination_ip']}: {reason}")
    send_email_alert(packet, reason)
