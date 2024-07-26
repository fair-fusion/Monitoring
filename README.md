# Fair-Fusion Monitoring - Measuring and Monitoring Temperature
Processes of bacteria growth need to be monitored 24/7 to understand if there could occur an error in a batch. Also, for quality purposes, one would like to retrace the exact circumstances of a process. 
This code allows you to set certain parameters for your batch and record all relevant variables per batch process. Monitoring is done using a Raspberry Pi and a Adafruit sensor.

## How to use
If you haven't done so already, you need to prepare your Raspberry.pi by running the following commands in your terminal (this may take a while):

## Setup Your Raspberry Pi and Sensor
Connect the colored cables of the Adafruit with the right pin positions. The yellow pin is important is it is set in the script. By default this is set in position number 7. Have a look here for the various pin locations and their functions: https://osoyoo.com/wp-content/uploads/2017/06/Raspberry-GPIO-Pins_B_plus-1.jpg

If you haven't done so already, you need to prepare your Raspberrypi by running the following commands in your terminal (this may take a while):
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install build-essential python-dev

### Download the Fair-Fusion Repository
`git clone https://github.com/fair-fusion/Monitoring.git`

Go to this folder by using cd. For example `cd Software/monitoring`

Install some dependencies by running:
`pip install -r requirements.txt`

### Running the program
To register the readings in a csv file, run the following in your terminal `python3 monitor_store.py`
To get simply readings in your terminal, run `python3 monitor.py`

## Installation of This Repo
This code is written for usage on a raspberry pi (Linux OS).
Create a virtual environment in your repo by running the following command in the terminal of the Rapsberry Pi:
'python -m venv' 

Activate the virtual environment with 'source venv/bin/activate'

Go to the folder to run the project
'cd Code/Monitoring'

Install some dependencies by running:
`pip install -r requirements.txt`