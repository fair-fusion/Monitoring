import time
import board
import adafruit_dht
import os
import csv
import smtplib  # for email notification (optional)

class TemperatureMonitor:
    def __init__(self, pin, time_interval=30.0, threshold_temperature=25.0):
        self.dhtDevice = adafruit_dht.DHT22(pin)
        self.time_interval = time_interval
        self.threshold_temperature = threshold_temperature
        self.csv_file = "data.csv"

    def register_temperature(self):
        try:
            temperature_c = self.dhtDevice.temperature
            humidity = self.dhtDevice.humidity
            current_time = time.strftime("%H:%M:%S")
            print(f"Temp: {temperature_c:.1f} C    Humidity: {humidity}%    Time: {current_time}")
            return temperature_c, humidity, current_time
        except RuntimeError as error:
            print(error.args[0])
            return None, None, None

    def log_data(self, temperature_c, humidity, current_time):
        with open(self.csv_file, "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([current_time, temperature_c, humidity])

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
                writer.writerow(["Time", "Temperature (C)", "Humidity (%)"])

        while True:
            temperature_c, humidity, current_time = self.register_temperature()
            if temperature_c is not None:
                self.log_data(temperature_c, humidity, current_time)
                self.check_threshold(temperature_c)

            time.sleep(self.time_interval)

            # Allow user to adjust the threshold temperature
            user_input = input("Enter a new threshold temperature (or press Enter to keep current): ")
            if user_input:
                try:
                    self.threshold_temperature = float(user_input)
                    print(f"Threshold temperature set to {self.threshold_temperature}°C")
                except ValueError:
                    print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    monitor = TemperatureMonitor(board.D5)
    monitor.run()