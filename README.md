# Fair-Fusion Monitoring - Measuring and Monitoring Temperature
Processes of bacteria growth need to be monitored 24/7 to understand if there could occur an error in a batch. Also, for quality purposes, one would like to retrace the exact circumstances of a process. 

This code allows you to:
- Monitor the temperature continuously
- Save the measurements with a timestamp in a csv file
- Set and record parameters for your batch
- Send an email notification if a the temperature exceeds a threshold of your choice 

Monitoring is done using a Raspberry Pi and a Adafruit sensor.

## Setup Your Raspberry Pi and Sensor
Connect the colored cables of the Adafruit with the right pin positions. The yellow pin is important is it is set in the script. By default this is set in position number 7. Have a look here for the various pin locations and their functions: https://osoyoo.com/wp-content/uploads/2017/06/Raspberry-GPIO-Pins_B_plus-1.jpg

If you haven't done so already, you need to prepare your Raspberrypi by running the following commands in your terminal (this may take a while):
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install build-essential python-dev

## Installation
create a venvironment in your repo by running the following command in the terminal of the Rapsberry Pi:
`python -m venv`
`source venv/bin/activate`
### Download the Fair-Fusion Repository
`git clone https://github.com/fair-fusion/Monitoring.git`

Go to the relevant folder by using cd: `cd Monitoring`

Install some dependencies by running:
`pip install -r requirements.txt`

### Running the program
To register the readings in a csv file, run the following in your terminal `python3 monitor_store.py`
To get simply readings in your terminal, run `python3 monitor.py`