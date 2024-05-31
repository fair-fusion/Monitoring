import os
import time
import Adafruit_DHT
import config #import from settings.json the configurations for the monitoring process

# Load settings from JSON file
settings = config.load_settings('settings.json')

# Extract settings values
data_base = config.get_setting(settings, 'data_base')
threshold_temp = config.get_setting(settings, 'threshold_temp')
batch_number = config.get_setting(settings, 'batch_number')
time_interval = config.get_setting(settings, 'time_interval')

#set the pin for the DHT22 sensor to read from 
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 7

#Open a txt file called "data_base.txt", if it's already in your folder, if not, create the file with the headers for all the sensor readings
#Define the headers of the data_base
data_base = "data_base.txt"
headers = ["date", "time", "temperature","humidity", "threshold_temp", "batch_number"]
#time interval = 2

# Check if the file exists
if not os.path.exists(data_base):
    print(f"File {data_base} already exists. Appending values to it.")
    # Create the file and write the headers
    with open(data_base, "w") as f:
        f.write(",".join(headers) + "\n")
        print(f"File {data_base} created and appending values to it.")
        #set the time interval for the sensor to read the temperature and humidity  
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        #register temperature, humidity, and the time (hour and minute)
        if humidity is not None and temperature is not None:
            f.write('{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n'.format(time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S'), temperature, humidity, threshold_temp, batch_number))
            print("{0},{1},{2:0.1f}*C,{3:0.1f}%\r\n".format(time.strftime('%m/%d/%y'), time.strftime('%H:%M:%S'), temperature, humidity, threshold_temp, batch_number))
        else:
            print("Failed to retrieve data from humidity sensor")
        #set time in seconds for every n number of seconds you want to register a temperature reading
        time.sleep(time_interval)