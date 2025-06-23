import pandas as pd
import os

LOG_FILE = 'data/logs.csv'

def load_logs():
    """Loads the log file if it exists, otherwise returns an empty DataFrame."""
    if os.path.exists(LOG_FILE):
        try:
            return pd.read_csv(LOG_FILE)
        except Exception as e:
            print(f"Failed to read log file: {e}")
    return pd.DataFrame(columns=['timestamp', 'source_ip', 'destination_ip', 'port', 'payload_size', 'reason'])
