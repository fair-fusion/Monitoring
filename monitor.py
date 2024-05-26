import pandas as pd
import os
import time
import Adafruit_DHT
# from config import Config #to import the settings file

#import a settings file that contains values for the time interval of the data logging, the heating status, water supply status, batch number, temperature threshold, and an email adress using config.py that imports a json file
# config = Config()
# time_interval = Config.time_interval
# heating_status = Config.heating_status
# water_supply_status = Config.water_supply_status
# threshold = config.threshold
# email_settings = config.email_settings
# fixed_values = config.fixed_values
# batch_number = config.batch_number

#set the file name of the csv where the data will be logged. If the file does not exist yet, create a file called 'monitoring.csv'.
#If the file already exists, the data will be appended to the file.
#the file contains columns for the date, time, temperature, humidity, heating status, and water supply status.
#write the sensor values to the csv file
#set sensor name (DHT22) and pin number.
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 7
#name and set the location of your csv file. The file name is humiditytest.csv.
file_name = 'monitoring.csv'
try:
    f = open(file_name, 'a+')
    if os.stat(file_name).st_size == 0:
            f.write('Date,Time,Temperature,Humidity, Heating Status, Water Supply Status\r\n')
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
    time.sleep(time_interval)