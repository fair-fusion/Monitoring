import time
import board
import adafruit_dht
import os
import csv

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D5)
time_interval = 30.0

# Check if the file exists, create it if it doesn't
if not os.path.exists("data.csv"):
    with open("data.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Time", "Temperature (C)", "Humidity (%)"])

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        current_time = time.strftime("%H:%M:%S")
        # Print the values to the serial port
        print(f"Temp: {temperature_c:.1f} C    Humidity: {humidity}%    Time: {current_time}")
        # Write to CSV file
        with open("data.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([current_time, temperature_c, humidity])
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(time_interval)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(time_interval)