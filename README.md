# 5G Network Analyzer

## 📌 Project Overview
The 5G Network Performance Analyzer is a Python-based tool to monitor, log, and visualize 5G network Key Performance Indicators (KPIs) in real-time.
It connects to a Quectel 5G modem (or similar) using AT commands over a serial interface. This tool helps in field testing, coverage analysis, and quality mapping of 5G networks.

---

## 📌 Features
- Send AT commands directly to the modem.
- Fetch and display network registration status.
- Check signal quality and operator details.
- Automate modem testing via Python scripts.
- Extendable for custom 5G modem use cases.

---

## ⚙️ Requirements
- Python 3.x
- `pyserial` library

Install dependencies:
```bash
pip install pyserial
```

---

## 🚀 Usage

### 1. Clone the Repository
```bash
git clone https://github.com/anshig135/5G-Network-Performance-Analyzer.git
cd 5G-Network-Performance-Analyzer
```

### 2. Run the Script
```bash
python network_logger.py
```

---

## 📖 Example AT Commands

Here are some useful AT commands you can try:

```bash
AT          # Check modem response
AT+CSQ      # Get signal quality
AT+CREG?    # Check network registration
AT+COPS?    # Get current operator
AT+CGATT?   # Check packet domain attach status
```

---

## 📊 Output Example

When you run the script, you may see output like this:

```text
Sending command: AT+CSQ
Response: +CSQ: 20,99

Sending command: AT+CREG?
Response: +CREG: 0,1
```

- `+CSQ: 20,99` → Signal strength (20 = good, range 0–31).  
- `+CREG: 0,1` → Registered to home network.  

---

## 🔍 Working Principle of a 5G Modem

A **5G modem** works as the interface between user equipment (laptops, IoT devices, routers) and the 5G cellular network.  

1. **Signal Processing** → Modulates/demodulates signals between digital (device) and RF (antenna).  
2. **AT Command Interface** → Allows configuration, monitoring, and control through serial communication.  
3. **Network Registration** → Connects to the nearest base station, authenticates SIM, and registers to the 5G core network.  
4. **Data Transmission** → Provides high-speed internet via packet-switched communication.  
5. **Monitoring** → Parameters like RSSI, SINR, RSRP, and RSRQ can be checked for performance tuning.  

---

## 🛠️ Future Improvements
- GUI dashboard for live modem stats.  
- Logging & graphing of network quality.  
- Integration with cloud for remote modem monitoring.  

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 👤 Author
**Anshika Gupta**  
B.Tech ECE | Banasthali Vidyapith  
