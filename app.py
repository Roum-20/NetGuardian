import streamlit as st
import pandas as pd
import altair as alt
import threading
import time

from packet_sniffer import packet_stream
from detector import detect_intrusion
from logger import log_alert
from utils import load_logs

# Set page layout
st.set_page_config(page_title="NetGuardian", layout="wide")
st.sidebar.title("🔧 Controls")
st.title("🛡️Netguardian")

# Function to monitor live packets
def monitor():
    for packet in packet_stream():
        detected, reason = detect_intrusion(packet)
        if detected:
            log_alert(packet, reason)

# Start button
if 'started' not in st.session_state:
    st.session_state.started = False

if st.button("▶️ Start IDS") and not st.session_state.started:
    threading.Thread(target=monitor, daemon=True).start()
    st.session_state.started = True
    st.success("Started monitoring")

st.markdown("---")
st.subheader("🔍 Filter Intrusion Logs")

# Load logs
logs = load_logs()

# Filters
selected_port = st.selectbox("Filter by Port", ["All"] + sorted(logs['port'].dropna().astype(str).unique().tolist()))
selected_src_ip = st.selectbox("Filter by Source IP", ["All"] + sorted(logs['source_ip'].dropna().unique()))
selected_reason = st.selectbox("Filter by Reason", ["All"] + sorted(logs['reason'].dropna().unique()))

if selected_port != "All":
    logs = logs[logs['port'].astype(str) == selected_port]
if selected_src_ip != "All":
    logs = logs[logs['source_ip'] == selected_src_ip]
if selected_reason != "All":
    logs = logs[logs['reason'] == selected_reason]

# Display logs
st.dataframe(logs[::-1], use_container_width=True)

# Live chart of intrusions
st.subheader("📈 Intrusion Frequency Over Time")

def plot_intrusions(df):
    if df.empty:
        st.info("No intrusion data to plot.")
        return

    df['time'] = pd.to_datetime(df['timestamp'], unit='s')
    df['minute'] = df['time'].dt.floor('min')
    freq_df = df.groupby('minute').size().reset_index(name='count')

    chart = alt.Chart(freq_df).mark_line(point=True).encode(
        x=alt.X('minute:T', title='Time'),
        y=alt.Y('count:Q', title='Intrusions'),
        tooltip=['minute:T', 'count:Q']
    ).properties(width=800, height=400).interactive()

    st.altair_chart(chart, use_container_width=True)

plot_intrusions(logs)
