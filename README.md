# NetworkLatencyTest
Simple Python script to monitor my Wi-Fi network latency

A small weekend project to explore observability and AI — starting with my home Wi-Fi.

This script logs latency and failures by pinging a set of public targets at regular intervals, then uses an LLM (like GPT) to analyze the results and surface meaningful insights:  
- When is the internet slow or unstable?  
- Are there patterns based on time of day?  
- When should I avoid video calls?

While simple, this experiment highlights a powerful concept:  
> **Observability isn't just for production systems — it's for decision-making anywhere.**

---

## 🚀 Features

- Pings websites like `google.com`, `openai.com`, and `cloudflare.com`
- Logs latency, success/failure, and timestamps to a CSV
- Visualize with Python and pandas
- Analyze with GPT to extract trends and get plain-language insights

---

## 📦 Requirements

- Python 3.7+
- Works on macOS, Linux, or WSL (uses `ping -c 1` command)

### Install packages (for visualization)

```bash
pip install pandas matplotlib
or
sudo apt install python3-pandas
