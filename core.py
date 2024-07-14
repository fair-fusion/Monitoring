import time
import board
import adafruit_dht
import os
import csv
import smtplib  # for email notification (optional)
import json

class TemperatureMonitor:
    def __init__(self, pin, config_file="settings.json"):
        self.config = self.load_config(config_file)
        self.dhtDevice = adafruit_dht.DHT22(pin)
        self.time_interval = self.config["time_interval"]
        self.threshold_temperature = self.config["threshold_temperature"]
        self.batch_number = self.config["batch_number"]
        self.csv_file = "data.csv"

    def load_config(self, config_file):
        with open(config_file, "r") as f:
            return json.load(f)

    def register_temperature(self):
        try:
            temperature_c = self.dhtDevice.temperature
            humidity = self.dhtDevice.humidity
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"Temp: {temperature_c:.1f} C    Humidity: {humidity}%    Time: {current_time}")
            return temperature_c, humidity, current_time
        except RuntimeError as error:
            print(error.args[0])
            return None, None, None

    def log_data(self, temperature_c, humidity, current_time):
        with open(self.csv_file, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([current_time, temperature_c, humidity, self.batch_number])

    def send_notification(self, subject, message):
        # Replace with your email credentials and settings
        sender_email = "your_email@example.com"
        recipient_email = "recipient_email@example.com"
        password = "your_email_password"
        smtp_server = "smtp.example.com"
        smtp_port = 587

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, recipient_email, f"Subject: {subject}\n\n{message}")
            server.quit()
            print("Notification sent!")
        except Exception as e:
            print(f"Error sending notification: {e}")

    def check_threshold(self, temperature_c):
        if temperature_c > self.threshold_temperature:
            subject = "Temperature Alert!"
            message = f"Temperature is above the threshold ({self.threshold_temperature}°C): {temperature_c:.1f}°C"
            self.send_notification(subject, message)

    def run(self):
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["date_time", "Temperature (C)", "Humidity (%)", "Batch Number"])

        while True:
            temperature_c, humidity, current_time = self.register_temperature()
            if temperature_c is not None:
                self.log_data(temperature_c, humidity, current_time)
                self.check_threshold(temperature_c)

            time.sleep(self.time_interval)

if __name__ == "__main__":
    monitor = TemperatureMonitor(board.D5)
    monitor.run()