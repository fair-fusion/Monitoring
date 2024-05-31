import pandas as pd
import os
import time
import Adafruit_DHT
from config import Config # import from settings.json the configurations for the monitoring process

def main():
    config = Config()

    threshold = config.threshold_temp
    email_settings = config.email_settings
    fixed_values = config.fixed_values
    batch_number = config.batch_number

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 7

#name and set the location of your csv file. The file name is monitoring.csv.
file_name = 'monitoring.csv'
try:
    #setting the file if it doesn't exist and write the headers
    f = open(file_name, 'a+')
    if os.stat(file_name).st_size == 0:
            f.write('Date, Time, Temperature, Humidity, batch_number, threshold, Water Supply Status\r\n')')
except:
    pass

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    #register temperature, humidity, and the time (hour and minute)
    if humidity is not None and temperature is not None:
        f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
        print("{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n".format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")
    #set time in seconds for every n number of seconds you want to register a temperature reading
    time.sleep(threshold)