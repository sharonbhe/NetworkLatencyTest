import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("network_latency_log.csv")
df = df[df['Latency_ms'] != 'N/A']
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df['Latency_ms'] = df['Latency_ms'].astype(float)

for target in df['Target'].unique():
    subset = df[df['Target'] == target]
    plt.plot(subset['Timestamp'], subset['Latency_ms'], label=target)

plt.title("Network Latency Over Time")
plt.xlabel("Time")
plt.ylabel("Latency (ms)")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
