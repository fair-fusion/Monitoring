import os
import time
import Adafruit_DHT
from config import Config #import from settings.json the configurations for the monitoring process

#import and set the values from settings.json
threshold_temp = Config.threshold_temp
batch_number = Config.batch_number
time_interval = Config.time_interval
data_base = Config.data_base

#set the pin for the DHT22 sensor to read from 
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 7

#Open a txt file called "data_base.txt", if it's already in your folder, if not, create the file with the headers for all the sensor readings
#Define the headers of the data_base
data_base = "data_base.txt"
headers = ["date", "time", "temperature"]

# Check if the file exists
if not os.path.exists(data_base):
    print(f"File {data_base} already exists. Appending values to it.")
    # Create the file and write the headers
    with open(data_base, "w") as f:
        f.write(",".join(headers) + "\n")
        print(f"File {data_base} created and appending values to it.")

#add the readings of the sensor to the database
f = open(data_base, 'a')

#set the time interval for the sensor to read the temperature and humidity  
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    #register temperature, humidity, and the time (hour and minute)
    if humidity is not None and temperature is not None:
        f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity, threshold_temp))
        print("{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n".format(time.strftime('%m/%d/%y'), time.strftime('%H:%M'), temperature, humidity, threshold_temp ))
    else:
        print("Failed to retrieve data from humidity sensor")
    #set time in seconds for every n number of seconds you want to register a temperature reading
    time.sleep(time_interval)