import subprocess
import time
import csv
from datetime import datetime

# List of targets to ping
targets = ["google.com", "openai.com", "cloudflare.com"]

# Output CSV file
filename = "network_latency_log.csv"

# Write CSV header
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Target", "Latency_ms", "Status"])

# Ping every 60 seconds for 10 iterations (or run indefinitely with a while loop)
for i in range(60):
    for target in targets:
        timestamp = datetime.now().isoformat()
        try:
            # Ping the target (1 packet)
            result = subprocess.run(["ping", "-c", "1", target], capture_output=True, text=True)
            if result.returncode == 0:
                # Extract latency from output
                output = result.stdout
                latency_line = [line for line in output.split('\n') if "time=" in line]
                if latency_line:
                    latency = latency_line[0].split("time=")[1].split(" ")[0]
                else:
                    latency = "N/A"
                status = "Success"
            else:
                latency = "N/A"
                status = "Fail"
        except Exception as e:
            latency = "Error"
            status = str(e)

        # Save to CSV
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, target, latency, status])

    print(f"Logged data at {datetime.now().strftime('%H:%M:%S')}")
    time.sleep(10)
