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
        print 'Hello'

    def load_calibration_data(self, platetype, filename=''):
        if not filename:
            if platform.system() == 'Windows':
                if platetype == 24:
                    with open('System Settings/calibration24Wells', 'r') as f:
                        self.positions24well = pickle.load(f)
                        self.positions24well[0][0] = 1048
                        self.positions24well[0][1] = 1513
                elif platetype == 96:
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
        else:
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
        with open('System Settings/savedSettings', 'rb') as f:
            self.savedSettings = pickle.load(f)

    def save_settings(self):
        with open('System Settings/savedSettings', 'wb') as f:
            pickle.dump(self.savedSettings, f)

    def load_well_labels(self):
        for row in self.rows:
                for column in self.cols:
                    self.wellNames96.append('well_' + row + str(column))
                    self.wellDict96.append('OFF')
        for row in self.rows[1:5]:
            for column in self.cols[1:7]:
                self.wellNames24.append('well_' + row + str(column))
                self.wellDict24.append('OFF')

    def set_plate_type(self, platetype):
        self.__platetype = platetype
        self.__platecount += 1
        if platetype == 24:
            self.selectionDict[self.__platecount] = self.wellDict24
        elif platetype == 96:
            self.selectionDict[self.__platecount] = self.wellDict96
        plate = PlateConfiguration(platetype, self.__platecount)
        self.plateList.append(plate)

    def set_current_plate(self, index):
        self.__current_plate_index = index

    def get_current_plate_type(self):
        plate_type = self.plateList[len(self.plateList)-1].well_numb
        return plate_type

    def get_plate_count(self):
        plate_numb = self.plateList[-1].order
        return plate_numb

    def remove_plate_object(self, plate_numb):
        del self.plateList[int(plate_numb)-1]
        for p in range(0, len(self.plateList)):
            self.plateList[p].order = p+1

    def get_selected_wells(self, plate_index):
        selected_wells = self.plateList[plate_index].get_selected_wells()
        return selected_wells

    def get_settings(self):
        return self.savedSettings

    def select_wells(self, plate_index, well_list):
        print self.plateList
        print plate_index
        for i in well_list:
            self.plateList[plate_index].select_wells(well_list)

    def clear_wells(self, plate_index):
        self.plateList[plate_index].clear_wells()

    def select_all_wells(self, plate_index):
        self.plateList[plate_index].select_all_wells()

    def add_absorbance_protocol(self, exp_time, label, plate_index, order):
        new_protocol = Absorbance(exp_time, label, plate_index, order)
        self.plateList[plate_index].add_protocol(new_protocol)

    def add_fluorescence_protocol(self, exp_time, led_index, wavelength_led_1, wavelength_led_2, wavelength_led_3,
                                  label, plate_index, order):
        new_protocol = Fluorescence(exp_time, led_index,  wavelength_led_1, wavelength_led_2,
                                    wavelength_led_3, label, plate_index, order)
        self.plateList[plate_index].add_protocol(new_protocol)

    def add_auxiliary_protocol(self, aux_index, duration, label, plate_index, order):
        new_protocol = Auxiliary(aux_index, duration, label, plate_index, order)
        self.plateList[plate_index].add_protocol(new_protocol)

    def turn_kinetic_tracking_on(self, method, interval, duration, reps, label, plate_index, order):
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
