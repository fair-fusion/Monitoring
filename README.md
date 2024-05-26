# Fair-Fusion Monitoring - Measuring and Monitoring Temperature
Processes of bacteria growth need to be monitored 24/7 to understand if there could occur an error in a batch. Also, for quality purposes, one would like to retrace the exact circumstances of a process. 

This code allows you to set certain parameters for your batch and record all relevant variables per batch process. Monitoring is done using a Raspberry Pi and a Adafruit sensor.

## Setup Your Raspberry Pi and Sensor
Connect the colored cables of the Adafruit with the right pin positions. The yellow pin is important is it is set in the script. By default this is set in position number 7. Have a look here for the various pin locations and their functions: https://osoyoo.com/wp-content/uploads/2017/06/Raspberry-GPIO-Pins_B_plus-1.jpg

If you haven't done so already, you need to prepare your Raspberrypi by running the following commands in your terminal (this may take a while):
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install build-essential python-dev

## Installation of This Repo
Create a virtual environment in your repo by running the following command in the terminal of the Rapsberry Pi:
'python -m venv' 

Activate the virtual environment with 'source venv/bin/activate'

Go to the folder to run the project
'cd Code/Monitoring'

Install some dependencies by running:
`pip install -r requirements.txt`

### to work on the notebooks using [nbdev](https://nbdev.fast.ai/) to push changes to the remote repository
Make sure that nbdev is installed by running `pip install nbdev` 
and install githooks by using `nbdev_install_git_hooks`.