import pandas as pd
import matplotlib.pyplot as plt

# Load the logged CSV file
df = pd.read_csv("5g_log.csv")

# Convert timestamp if available
if "Timestamp" in df.columns:
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Plot RSRP, RSRQ, SINR
plt.figure(figsize=(12, 6))

plt.plot(df["Timestamp"], df["RSRP"], label="RSRP (dBm)", marker="o")
plt.plot(df["Timestamp"], df["RSRQ"], label="RSRQ (dB)", marker="s")
plt.plot(df["Timestamp"], df["SINR"], label="SINR (dB)", marker="^")

plt.xlabel("Time")
plt.ylabel("Signal Metrics")
plt.title("5G Network KPIs Over Time")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
