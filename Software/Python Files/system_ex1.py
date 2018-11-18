# OSP - System Control Example Script 01
# This script walks through the basics of controlling the OSP device via a manual Python script. 
# ---------------------------------
# Written by: Karol Szymula 
# Last Updated: Nov. 18, 2018
# ---------------------------------

# Import the OSP System class and all its functions
from System import *

# Create an instance of the OSP System object
system = System()

# Initialize the Machine class object to all for machine command execution
system.initialize_machine()
time.sleep(1)

# Add a plate configuration to the system and define the plate type (24 or 96)
system.set_plate_type(24) 
time.sleep(1)

# Now select the wells which you want to run protocols on
# To select ALL wells 
system.select_all_wells(0)
time.sleep(1)

# To clear ALL wells
system.clear_wells(0)
time.sleep(1)

# To select specific wells (A1-A6 in this case)
# func - system.select_wells (plate_index, well_list)
#       Paramaters
#           plate_index - index of the plate for which wells are being selected. Indexing begins at zero.
# 
#           well_list - list of well indices, where well A1 is indexed at 0 and indicies increase along the
#                       rows. For example, in a 24-well plate, the indicies of the first row wells A1-A6 = 0-5, 
#                       second row B1-B6 = 6-11, etc. 
system.select_wells(0, [0,1,2,3,4,5])
time.sleep(1)

# Add the following protocol sequence:
#   1. Shake
#       func - system.add_shake_protocol(label, plate_index, order)
#           Paramaters
#               label  - string label of the protocol, 'Shake' in this case.
#               
#               plate_index - index of the plate for which wells are being selected. Indexing begins at zero.
# 
#               order - index of the the protocol in the existing list of protocols for the plate configuration object.
#                      Indexing begins at 0. 
#  
#   2. Absorbance (Exposure Time: 100ms)
#       func - system.add_absorbance_protocol(exp_time, label, plate_index, order)
#           Paramaters
#               exp_time - exposure time to perform protocol under in milliseconds.
#
#               label  - string label of the protocol, 'Shake' in this case.
#               
#               plate_index - index of the plate for which wells are being selected. Indexing begins at zero.
# 
#               order - index of the the protocol in the existing list of protocols for the plate configuration object.
#                      Indexing begins at 0.
#   3. Shake
#   4. Fluorescence (Exposure Time: 100ms, LED 1)
#       func - system.add_fluorescence_protocol(exp_time, led_index, wavelength_led1, wavelength_led2, wavelength_led3, label, plate_index, order)
#           Paramaters
#               exp_time - exposure time to perform protocol under in milliseconds.
#
#               led_index - binary string consisting of 4 values, such as '1111'. The first three characters of the string represent the on/off
#                           status of the excitation soruces LED 1, LED 2, LED 3, respectively. The fourth characeter represents the on/off status 
#                           of the external source (for the bottom optical train). A "1" means that the fluorescent measurement will be taken with
#                           that specific source on, while a 0 means that light source will be off.
# 
#               wavelength_led# - gives the user the ability to define in the system the wavelength of the LED, which is then output to the excel 
#                                 sheet for reference. 
#
#               label  - string label of the protocol, 'Shake' in this case.
#               
#               plate_index - index of the plate for which wells are being selected. Indexing begins at zero.
# 
#               order - index of the the protocol in the existing list of protocols for the plate configuration object.
#                      Indexing begins at 0.

system.add_shake_protocol('Shake', 0, 0)
time.sleep(1)
system.add_absorbance_protocol(100, 'Absorbance', 0, 1)
time.sleep(1)
system.add_shake_protocol('Shake', 0, 2)
time.sleep(1)
system.add_fluorescence_protocol(100, '1000', 490, 530, 630, 'Fluorescence', 0, 3)
time.sleep(1)

# Run the protocol
#       func - system.start_program(system.plateList, filename)
#           Paramaters
#               system.plateList - object part of System object containing a list of plate configuration objects.
#
#               filename - [this input is optional] string which will be used as the name of the output data file.

system.start_program(system.plateList, 'system_ex1_output')
time.sleep(1)

