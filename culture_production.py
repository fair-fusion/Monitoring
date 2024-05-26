#sproeidroger

# Requirements
csv
#Batchnummer (1 tot n)
#datum, tijd, elke 20 seconden (of inteval logging instelbaar manueel)
#temperatuur extern (omgeving), humiditeit
#teperatuur tank
#gewicht tank (comport)
#status verwarming (instellen manueel)
#rpm motor - sensor via comport
#status aanvoer kraan (aan of uit, manueel instellen)

#centrifugeren
#doseren (instel waarde (e.g., 4l per uur))
#daadwerkelijke dosis (meet via comport)
#centrifuge (aan/uit)

# Chapter 1: Equipment check
# Chapter 2: Data logging
# Chapter 3: Messaging via e-mail and sms
# Chapter 4: Temperature control of fermenation tank
# Chapter 5: Fermentation prepararion
# Chapter 6: Fermentation processing
# Chapter 7: Fermentation tank cleaning process
# Chapter 8: Centrifuge cleaning process

#To do
# - create pause function
# - data logger
# -  

#sotware start up
import time
import os
import serial
import datetime

# Chapter 1: equipment check
# 1: Check for error message from load cells
# 2: Check environment humidity and temperature
# 3: Fermentation tank temperatures
# 4: Dosing equipment error messages
# 5: reply from Centrifuge
# 6: reply from engine (optional)
# 7: Reply from Spray-dryer
# 8: error message from spectrophotometer
# 9: reply from smtp server
# 10: reply from DAV server
# 11: Fermentation tank temperatures
# 12: dashboard for monitoring


# Chapter 1: data logging: Luca?

# 1: ensure that every batch has its own batch-log file a.k.a. batch number
# 2: ensure that every file is logged is organised per year
# 3: ensure that when there is power failure the log file can be again to store data and to read the last status
# 4


# Chapter 2: messagging via e-mail and sms: Luca?

# 1: ensure that greenhost is used as smtp server
# 2: messages are copied to appropriet 'warning folder'
# 2: make e-mail alias fermentor@polybiotic-soltuions.nl



# Chapter 3: temperature control of fermenation tank

# Read current temperature of the fermentation tank and turn of or on the ketel


# Chapter 4: Fermentation prepararion

#Standard production settings
v = 1.0 #software version
T_tank = 32 #temperature of liquid tank
T_water = 34 #temperature of water added
time = 48 #fermentation duration in hours
StirA = 300 #rotation speed fo preperating fermentation in rpm
StirB = 275 #ration speed for fermentation in rpm
RateC = 4.2 #feed rate to the centrifuge in L/h
RateC_em = 0.1 #(errror margin)margin of error to the feed to the centrifuge in L/h
v_culture = 2 #mass of cutlure


#Start set-up
print("welcome to PolyBiotic production software V " v)

print("How much volume per cycle would you like to produce?")
user_input_production_Cycle_Volume = input(
            """How much volume per cycle would you like to produce?
            (answer \'exit\' or \'e\' if you want to stop):
            >>""")
        if "open" in user_input_beam_opening.lower() or user_input_beam_opening.lower() == "o":
            com_ser('?S')
            shutter_status = int(setting)
            shutter_status_fault_number = fault_number
            if shutter_status_fault_number != 0:
                print("error " + str(shutter_status_fault_number))
                print('look up the error code in the user-manual and fix it')
            if shutter_status == 0:
                com_ser('S=1')
                print("Beam-shutter is open now")
            if shutter_status == 1:

user_input_production_cycles = input(
            """How many cycles do you wish to run?
            (answer \'exit\' or \'e\' if you want to stop):
            >>""")
        if "open" in user_input_beam_opening.lower() or user_input_beam_opening.lower() == "o":
            com_ser('?S')
            shutter_status = int(setting)
            shutter_status_fault_number = fault_number
            if shutter_status_fault_number != 0:
                print("error " + str(shutter_status_fault_number))
                print('look up the error code in the user-manual and fix it')
            if shutter_status == 0:
                com_ser('S=1')
                print("Beam-shutter is open now")
            if shutter_status == 1:

user_input_production_type = input(
            """Would you like an energy optimized or speed optimised production?
            Answer s(speed) or e(energy)
            (answer \'exit\' or \'e\' if don't want change the beam shutter status):
            >>""")
        if "open" in user_input_beam_opening.lower() or user_input_beam_opening.lower() == "o":
            com_ser('?S')
            shutter_status = int(setting)
            shutter_status_fault_number = fault_number
            if shutter_status_fault_number != 0:
                print("error " + str(shutter_status_fault_number))
                print('look up the error code in the user-manual and fix it')
            if shutter_status == 0:
                com_ser('S=1')
                print("Beam-shutter is open now")
            if shutter_status == 1:

user_input_production_Last_check = input(
            """Do you want the following statement:
               "-" volume "Litres per cycle"
               "-" cycle "cycle(s)"
               "-" prod "optimized production")
            Answer Y(yes) or N(no)
            (answer \'exit\' or \'e\' if you want to stop):
            >>""")
        if "open" in user_input_beam_opening.lower() or user_input_beam_opening.lower() == "o":
            com_ser('?S')
            shutter_status = int(setting)
            shutter_status_fault_number = fault_number
            if shutter_status_fault_number != 0:
                print("error " + str(shutter_status_fault_number))
                print('look up the error code in the user-manual and fix it')

print("All set! x cycle()s) of production start now)

#Preparing fermentation

print("Add kg of Spirulina")


print("Add 2 litres of culture")

print("Preparing for fermentation. % complete")

#fermenting

print("Fermentation in progress. Temperature is and time remaining: ")

#centrifugation

print("Centrifugation in progress. Time remaining: ")

#spray-drying

#Final
print("The production of" c "cycles of " v "litres is completed")
print("The logg files are safed under: " loggs)






# configure the serial connections with settings from manual 9600 8N1
ser = serial.Serial(
    port='/dev/ttyS0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
ser.close()
ser.open()
ser.isOpen()

print('Enter your commands below. Insert "exit" to leave the application.')

input1 = 1
while 1:
    # get keyboard input
    input1 = input(">> ")
    if input1 == 'exit':
        ser.close()
        exit()
    else:
        # send the character to the device, with a semicolon at the end
        # It is also encode to bytes
        ser.write(str.encode(input1+";"))
        out = ""
        # let's wait one second before reading output (let's give device time to answer)
        time.sleep(0.6)
        while ser.inWaiting() > 0:
            out += ser.read(1).decode()  # decoding the bytes to a string

        if out != '':
            print(out)

loggs =  #folder where log files are stored