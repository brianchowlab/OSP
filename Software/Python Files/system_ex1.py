# Import the OSP System class and all its functions
from .PythonFiles import System


# Create an instance of the OSP System object
system = System()

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
system.select_wells(0, [1,2,3,4,5,6])
time.sleep(1)

# Add the following protocol sequence:
#   1. Shake
#   2. Absorbance (Exposure Time: 100ms)
#   3. Shake
#   4. Fluorescence (Exposure Time: 100ms, LED 1)
system.add_shake_protocol('Shake', 0, 0)
time.sleep(1)
system.add_absorbance_protocol(100, 'Absorbance', 0, 1)
time.sleep(1)
system.add_shake_protocol('Shake', 0, 2)
time.sleep(1)
system.add_fluorescence_protocol(100, '1000', 490, 530, 630, 'Fluorescence', 0, 3)
time.sleep(1)

# Run the protocol
system.start_program(system.plateList, 'system_ex1_output')
time.sleep(1)

