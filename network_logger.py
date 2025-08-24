import serial
import time
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

# Configure your serial port here
SERIAL_PORT = "COM12"   # Change to /dev/ttyUSBx on Linux
BAUDRATE = 115200

def parse_qeng(line):
    """
    Parse AT+QENG="servingcell" response.
    Example: +QENG: "servingcell","NOCONN","LTE","FDD",404,70,901DC1F,103,515,1,4,4,31F,-85,-10,-55,14,0,-,38
    """
    try:
        parts = line.split(",")
        rsrp = int(parts[-6])   # -85
        rsrq = int(parts[-5])   # -10
        rssi = int(parts[-4])   # -55
        sinr = int(parts[-3])   # 14
        cell_id = parts[6]      # 901DC1F
        return rsrp, rsrq, rssi, sinr, cell_id
    except:
        return None, None, None, None, None

def main():
    ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=1)

    with open("5g_log.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Time", "RSRP", "RSRQ", "RSSI", "SINR", "Cell_ID"])

        print("Logging started... Press Ctrl+C to stop.")

        try:
            while True:
                ser.write(b'AT+QENG="servingcell"\r')
                time.sleep(0.5)

                response = ser.readlines()
                for line in response:
                    line = line.decode(errors="ignore").strip()
                    if line.startswith("+QENG:"):
                        rsrp, rsrq, rssi, sinr, cell_id = parse_qeng(line)
                        if rsrp is not None:
                            ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            writer.writerow([ts, rsrp, rsrq, rssi, sinr, cell_id])
                            f.flush()
                            print(ts, rsrp, rsrq, rssi, sinr, cell_id)

                time.sleep(2)

        except KeyboardInterrupt:
            print("\nLogging stopped.")

    ser.close()

def plot_data():
    df = pd.read_csv("5g_log.csv")
    plt.figure(figsize=(10,6))
    plt.plot(df["Time"], df["RSRP"], label="RSRP (dBm)")
    plt.plot(df["Time"], df["RSRQ"], label="RSRQ (dB)")
    plt.plot(df["Time"], df["SINR"], label="SINR (dB)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.title("5G/LTE Signal KPIs over Time")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
    # After logging, run plot_data() separately
