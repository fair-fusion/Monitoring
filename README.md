# Fair-Fusion Monitoring - Measuring and Monitoring Temperature

## Install

DOES NOT WORK YET
This is not yet a package so you only need to install the requirerments as specified in requirements.txt

`pip install monitoring`

## How to use
If you haven't done so already, you need to prepare your Raspberry.pi by running the following commands in your terminal (this may take a while):
- sudo apt-get update
- sudo apt-get upgrade
- sudo apt-get install build-essential python-dev

### Download the Fair-Fusion Repository
`git clone https://github.com/fair-fusion/monitoring.git`

Go to this folder by using cd. For example `cd Documents/software/monitoring`

Install some dependencies by running:
`pip install requirements.txt`

### Running the program
In your terminal, run `python3 temp_reg_p.py`

### to work on the notebooks using [nbdev](https://nbdev.fast.ai/) to push changes to the remote repository
Make sure that nbdev is installed by running `pip install nbdev` 
and install githooks by using `nbdev_install_git_hooks`.
