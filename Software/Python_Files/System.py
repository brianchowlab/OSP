"""
System.py
====================================
The core module of my example project
"""

from __future__ import division
from Machine import *
from PlateConfiguration import *
from Absorbance import *
from Fluorescence import *
from Kinetic import *
from Auxiliary import *
import xlsxwriter
import pickle
import platform

class System(object):
    """An example docstring for a class definition."""

    def __init__(self):
        super(System, self).__init__()
        self.positions24well = []  # Array to store motor positions of wells for 24 well plate
        self.positions96well = []  # Array to store motor positions of wells for 96 well plate
        self.rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # List of all possible row labels for 24 & 96 well plates
        self.cols = range(1, 13)  # List of all possible column labels for 24 & 96 well plates
        self.wellDict24 = []  # List to store selection status of all wells in 24 well plate
        self.wellDict96 = []  # List to store selection status of all wells in 96 well plate
        self.wellNames24 = []  # List to store the full label of all wells in 24 well plate
        self.wellNames96 = []  # List to store the full label of all wells in 96 well plate
        self.savedSettings = []  # List to store LED Wavelength properties and system measurement settings
        self.selectionDict = {1: {}}
        self.plateList = []
        self.__current_plate_index = 0
        self.__platetype = 0
        self.__platecount = 0
        self.load_calibration_data(24)
        self.load_calibration_data(96)
        self.load_settings()
        self.load_well_labels()


    def load_calibration_data(self, platetype, filename =''):
        """
        Return the most important thing about a person.

        Parameters
        ----------
        platetype
            A string indicating the name of the person.
        
        filename
            A filename of the calibration data 


        """

        if not filename: # If no filename was entered into function
            # Checks OS of system 
            if platform.system() == 'Windows':
                if platetype == 24: # Loads calibration data for 24-well plate
                    with open('System Settings/calibration24Wells', 'r') as f:
                        self.positions24well = pickle.load(f)
                        self.positions24well[0][0] = 1048
                        self.positions24well[0][1] = 1513
                elif platetype == 96: # Loads calibration data for 96-well plate
                    with open('System Settings/calibration96Wells', 'r') as f:
                        self.positions96well = pickle.load(f)
                        print self.positions96well
            elif platform.system() == 'Darwin':
                if platetype == 24:
                    with open('System Settings/calibration24Wells', 'r') as f:
                        self.positions24well = pickle.load(f)
                        self.positions24well[0][0] = 1048
                        self.positions24well[0][1] = 1513
                elif platetype == 96:
                    with open('System Settings/calibration96Wells', 'r') as f:
                        self.positions96well = pickle.load(f)
                        print self.positions96well
            elif platform.system() == 'Linux':
                if platetype == 24:
                    with open('System Settings/calibration24Wells', 'rb') as f:
                        self.positions24well = pickle.load(f)
                        self.positions24well[0][0] = 1048
                        self.positions24well[0][1] = 1513
                elif platetype == 96:
                    with open('System Settings/calibration96Wells', 'rb') as f:
                        self.positions96well = pickle.load(f)
                        print self.positions96well    
        else: # If filename was provided as an input
            if platform.system() == 'Windows':
                if platetype == 24:
                    with open('System Settings/' + filename, 'r') as f:
                        self.positions24well = pickle.load(f)
                elif platetype == 96:
                    with open('System Settings/' + filename, 'r') as f:
                        self.positions96well = pickle.load(f)
            elif platform.system() == 'Darwin':
                if platetype == 24:
                    with open('System Settings/' + filename, 'r') as f:
                        self.positions24well = pickle.load(f)
                elif platetype == 96:
                    with open('System Settings/' + filename, 'r') as f:
                        self.positions96well = pickle.load(f)
            elif platform.system() == 'Linux':
                if platetype == 24:
                    with open('System Settings/' + filename, 'rb') as f:
                        self.positions24well = pickle.load(f)
                elif platetype == 96:
                    with open('System Settings/' + filename, 'rb') as f:
                        self.positions96well = pickle.load(f)
                        
    def load_settings(self):
        """Used to automatically load the saved settings for the OSP software. Settings include
        the light source wavelengths and the number of scans to average. The settings are stored
        as a pickle file in System Settings directory. 
        """

        with open('System Settings/savedSettings', 'rb') as f:
            self.savedSettings = pickle.load(f)

    def save_settings(self):
        """
        Used to automatically save the system settings for the OSP software. Settings include
        the light source wavelengths and the number of scans to average. The settings are stored
        as a pickle file in System Settings directory. 
    

        """

        with open('System Settings/savedSettings', 'wb') as f:
            pickle.dump(self.savedSettings, f)

    def load_well_labels(self):
        """
        Creates the necessary list to store the well labels in form of 'well_rowcolumn'. For example
        the entry in the list for A2 would be 'well_A2'. Also creates a list to store the selection status
        of a particular well as either 'OFF' (not selected) or 'ON' (selected).
        
        
        """

        for row in self.rows:
                for column in self.cols:
                    self.wellNames96.append('well_' + row + str(column))
                    self.wellDict96.append('OFF')
        for row in self.rows[1:5]:
            for column in self.cols[1:7]:
                self.wellNames24.append('well_' + row + str(column))
                self.wellDict24.append('OFF')

    def set_plate_type(self, platetype):
        """
        This function initializes a new PlateConfiguration object which will be used to keep track
        of which wells are selected and which protocols to execute for the selected wells. The newly created
        PlateConfiguration object is added to a list allowing it be accessed later on. This function is executed
        every time a new set of protocols is desired to be run on a different group of wells (a new PlateConfiguration needed).


        Parameters
        ----------

        platetype
            possible value of 24 (for 24-well plate) or 96 (for 96-well plate).


        """

        self.__platetype = platetype
        self.__platecount += 1
        if platetype == 24:
            self.selectionDict[self.__platecount] = self.wellDict24
        elif platetype == 96:
            self.selectionDict[self.__platecount] = self.wellDict96
        plate = PlateConfiguration(platetype, self.__platecount)
        self.plateList.append(plate)

    def set_current_plate(self, index):
        """Function to keep track of the index of the PlateConfiguration which is being edited.
        
        Arguments:
            index {integer} -- index of the PlateConfiguration object in the self.plateList list
        """

        self.__current_plate_index = index

    def get_current_plate_type(self):
        """Function to attain the type of plate (24 or 96 well) of the current PlateConfiguration object
        
        Returns:
            integer -- plate type of current PlateConfiguration object being edited. Returns 24 (for 24-well plate)
            or 96 (for 96-well plate).
        """

        plate_type = self.plateList[len(self.plateList)-1].well_numb
        return plate_type

    def get_plate_count(self):
        """Used to attain the number of PlateConfiguration objects added to the system.
        
        Returns:
            integer -- number of PlateConfiguration objects in self.plateList.
        """

        plate_numb = self.plateList[-1].order
        return plate_numb

    def remove_plate_object(self, plate_numb):
        """Function to remove a PlateConfiguration object from self.plateList. If object is removed
        the indices of all other plates are fixed to account for the removal. 
        
        Arguments:
            plate_numb {integer} -- integer representing the index of the PlateConfiguration object in 
            self.plateList. For this variable, an input of 1 would represent the first entry in self.plateList.
        """

        del self.plateList[int(plate_numb)-1]
        for p in range(0, len(self.plateList)):
            self.plateList[p].order = p+1

    def get_selected_wells(self, plate_index):
        """Returns a list of all the wells which were selected for protocol execution. 
        
        Arguments:
            plate_index {integer} -- index of the PlateConfiguration object in self.plateList from which the selected wells
            are to be extracted from. 
        
        Returns:
            [list] -- Each element in list is the label (as a string) of a well which was selected. If well A1 was selected, 
            then the list would contain the element 'A1'.  
        """

        selected_wells = self.plateList[plate_index].get_selected_wells()
        return selected_wells

    def get_settings(self):
        """Returns the current settings of the system. 
        
        Returns:
            [list] -- The list is made up of four elements. The first 3 elements represent the wavelengths of LEDs 1, 2, and 3 respectively. 
            The fourth element of the list represents the number of scans to average. 
        """

        return self.savedSettings

    def select_wells(self, plate_index, well_list):
        """Function used to select the wells for protocol execution in a specific PlateConfiguration
        
        Arguments:
            plate_index {integer} -- index of the PlateConfiguration object in self.plateList in which to select wells
            well_list {list} -- a list of the well indices, where well A1 is indexed at 0 and indices increase along the rows.  
            For example, in a 24-well plate, the indices of the first row wells A1-A6 = 0-5,  second row B1-B6 = 6-11, etc
        """

        print self.plateList
        print plate_index
        for i in well_list:
            self.plateList[plate_index].select_wells(well_list)

    def clear_wells(self, plate_index):
        """Function used to unselect (clear) all the wells from the PlateConfiguration object
        
        Arguments:
            plate_index {integer} -- index of the PlateConfiguration object in self.plateList in which to unselect wells
        """

        self.plateList[plate_index].clear_wells()

    def select_all_wells(self, plate_index):
        """Function used to select all the wells in the PlateConfiguration object
        
        Arguments:
            plate_index {integer} -- index of the PlateConfiguration object in self.plateList in which to select wells
        """

        self.plateList[plate_index].select_all_wells()

    def add_absorbance_protocol(self, exp_time, label, plate_index, order):
        """Function to add an Absorbance protocol to the list of protocols to execute for a particular PlateConfiguration
        
        Arguments:
            exp_time {integer} -- exposure time with which to collect absorbance spectrum in milliseconds
            label {string} -- protocol label, should be set to 'Absorbance' 
            plate_index {integer} -- index of the PlateConfiguration object in self.plateList in which to select wells
            order {integer} -- the index of the protocol in the existing list of protocols of the plate configuration object. 
            If this is the first protocol that is being added to the PlateConfiguration object then the order is equal to zero. If it is the second, then the order is equal to 1 and so on.
        """

        new_protocol = Absorbance(exp_time, label, plate_index, order)
        self.plateList[plate_index].add_protocol(new_protocol)

    def add_fluorescence_protocol(self, exp_time, led_index, wavelength_led_1, wavelength_led_2, wavelength_led_3,
                                  label, plate_index, order):
        """Function to add an Fluorescence protocol to the list of protocols to execute for a particular PlateConfiguration
        
        Arguments:
            exp_time {integer} -- exposure time with which to collect absorbance spectrum in milliseconds
            led_index {integer} -- possible values 1,2 or 3 representing which LED to use for protocol. Only 1 LED per protocol.
            wavelength_led_1 {integer} -- wavelength of LED 1
            wavelength_led_2 {integer} -- wavelength of LED 2
            wavelength_led_3 {integer} -- wavelength of LED 3
            label {string} -- protocol label, should be set to 'Fluorescence' 
            plate_index {integer} -- index of the PlateConfiguration object in self.plateList in which to select wells
            order {integer} -- the index of the protocol in the existing list of protocols of the plate configuration object. 
            If this is the first protocol that is being added to the PlateConfiguration object then the order is equal to zero. If it is the second, then the order is equal to 1 and so on.
        """

        new_protocol = Fluorescence(exp_time, led_index,  wavelength_led_1, wavelength_led_2,
                                    wavelength_led_3, label, plate_index, order)
        self.plateList[plate_index].add_protocol(new_protocol)

    def add_auxiliary_protocol(self, aux_index, duration, label, plate_index, order):
        """Function to add an Auxiliary protocol to the list of protocols to execute for a particular PlateConfiguration.
        The auxiliary protocol type is defined by the aux_index input. 
        
        Arguments:
            aux_index {integer} -- possible values 1, 2, 3 or 4 representing which auxiliary port will be triggerd on.
            duration {integer} -- duration for how long to trigger the selected auxiliary port for.
            label {string} -- protocol label, should be set to 'Auxiliary' 
            plate_index {integer} -- index of the PlateConfiguration object in self.plateList in which to select wells
            order {integer} -- the index of the protocol in the existing list of protocols of the plate configuration object. 
            If this is the first protocol that is being added to the PlateConfiguration object then the order is equal to zero. If it is the second, then the order is equal to 1 and so on.
        """

        new_protocol = Auxiliary(aux_index, duration, label, plate_index, order)
        self.plateList[plate_index].add_protocol(new_protocol)

    def turn_kinetic_tracking_on(self, method, interval, duration, reps, label, plate_index, order):
        """Function to turn on the system kinetic mode. This enables the user to input protocols into a kinetic sequence
        which can be looped for a desired time period or repeated a specific number of times. 
        
        The interval method allows the user to perform a series of protocols in intervals for a specified duration of time. 
        For example, executing an Absorbance protocol very 30 seconds for 20 minutes.  

        The repetiion method allows the user to repeatedly perform a series of protocols. For example, executing an Absorbance
        protocol 10 times in a row. 
        
        Arguments:
            method {integer} -- possible value 1 (for Interval method) or 2 (for Repeat method)
            interval {integer} --  interval time for a kinetic protocol (milliseconds)
            duration {integer} -- the duration to perform the kinetic protocol sequence (milliseconds)
            reps {integer} -- number of times to repeat the kinetic protocol sequence
            label {string} -- protocol label, should be set to 'Kinetic' 
            plate_index {integer} -- index of the PlateConfiguration object in self.plateList in which to select wells
            order {integer} -- the index of the protocol in the existing list of protocols of the plate configuration object. 
            If this is the first protocol that is being added to the PlateConfiguration object then the order is equal to zero. If it is the second, then the order is equal to 1 and so on.
        """

        new_protocol = Kinetic(method, interval, duration, reps, label, plate_index, order)
        self.plateList[plate_index].add_protocol(new_protocol)

    def add_kinetic_absorbance_protocol(self, exp_time, label, plate_index, protocol_index, order):
        new_protocol = Absorbance(exp_time, label, plate_index, order)
        kinetic_protocol = self.plateList[plate_index].get_protocol(protocol_index)
        kinetic_protocol.add_protocol(new_protocol)

    def add_kinetic_fluorescence_protocol(self, exp_time, led_index, wavelength_led_1, wavelength_led_2,
                                          wavelength_led_3, label, plate_index, protocol_index, order):
        new_protocol = Fluorescence(exp_time, led_index,  wavelength_led_1, wavelength_led_2,
                                    wavelength_led_3, label, plate_index, order)
        kinetic_protocol = self.plateList[plate_index].get_protocol(protocol_index)
        kinetic_protocol.add_protocol(new_protocol)

    def add_kinetic_auxiliary_protocol(self, aux_index, duration, label, plate_index, protocol_index, order):
        new_protocol = Auxiliary(aux_index, duration, label, plate_index, order)
        kinetic_protocol = self.plateList[plate_index].get_protocol(protocol_index)
        kinetic_protocol.add_protocol(new_protocol)

    def get_all_protocol_brief_descriptions(self, plate_index):
        for p in range(0, self.plateList[plate_index].get_protocol_count()):
            protocol = self.plateList[plate_index].get_protocol(p)
            protocol.get_brief_description()

    def get_all_protocol_full_descriptions(self, plate_index):
        for p in range(0, self.plateList[plate_index].get_protocol_count()):
            protocol = self.plateList[plate_index].get_protocol(p)
            protocol.get_full_description()

    def initialize_machine(self):
        print 'Machine Initialized'
        self.machine = Machine(self.savedSettings)

    def close_machine(self):
        self.machine.arduino.close()
        self.machine.spec.close()

    def start_program(self, plate_list, filename=''):
        print 'Initialize Excel sheet'
        self.initialize_datasheet(filename)
        print 'System prompt machine to start'
        self.machine.start_program(plate_list, self.worksheet, self.workbook, self.merge_format, self.header_format,
                                   self.positions24well, self.positions96well)

    def initialize_datasheet(self, user_name):
        if not user_name:
            filename = 'Data/'+'data'+time.strftime("%Y_%m_%d_%H_%M")+'.xlsx'
        else:
            filename = 'Data/'+user_name+'.xlsx'
        self.workbook = xlsxwriter.Workbook(filename)
        self.worksheet = self.workbook.add_worksheet()
        self.merge_format = self.workbook.add_format({'align': 'center'})
        self.header_format = self.workbook.add_format()
        self.header_format.set_bold(True)
        self.header_format.set_bg_color('gray')
        self.worksheet.merge_range('A1:E1', '-------------------- PBPR --------------------', self.merge_format)
        self.worksheet.merge_range('A2:E2', str(time.ctime()), self.merge_format)
        self.worksheet.merge_range('A3:E3', '------------------------------------------------------------', self.merge_format)
        return filename
