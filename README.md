# Fair-Fusion Monitoring - Measuring and Monitoring Temperature
Processes need to be monitored 24/7 to understand if there could occur an error in a batch. Also, for quality purposes, one would like to retrace the exact circumstances of a process. 

This code allows you to set certain parameters for your batch and record all relevant variables per batch process

## How to use
If you haven't done so already, you need to prepare your Raspberry.pi by running the following commands in your terminal (this may take a while):
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

# Requirements
csv - DONE
#Batchnummer (1 tot n)
#datum, tijd, elke 20 seconden (of inteval logging instelbaar manueel) - DONE
#temperatuur extern (omgeving), humiditeit - DONE
#teperatuur tank
#gewicht tank (comport)
#status verwarming (instellen manueel)
#rpm motor - sensor via comport
#status aanvoer kraan (aan of uit, manueel instellen)

#centrifugeren
#doseren (instel waarde (e.g., 4l per uur))
#daadwerkelijke dosis (meet via comport)
#centrifuge (aan/uit)