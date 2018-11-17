from __future__ import division
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import pyqtSlot

import time
import numpy as np
import xlsxwriter

import platform
import os
import sys
import pickle
import seabreeze.spectrometers as sb
import matplotlib.pyplot as plt


from System import *
from Screens.mainScreen import *
from Screens.settingsScreen import *
from Screens.wellSelectScreen24 import *
from Screens.protocolSelectScreen_v2 import *
from Screens.absScreen import *
from Screens.flrScreen import *
from Screens.kineticScreen import *
from Screens.auxScreen import *
from Screens.reviewScreen import *
from Screens.plateOptionScreen import *
from Screens.wellSelectScreen96 import *


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class GUI(System, QtGui.QWidget):
    def __init__(self, argVal):
        super(GUI, self).__init__()
        if argVal == 0:
            self.initialize_machine()
        self.introwindow = mainScreen()
        self.introwindow.settings_button.clicked.connect(lambda: self.change_settings(0))
        self.introwindow.start_button.clicked.connect(lambda: self.start_plate_selection(0))
        self.introwindow.plateOut_button.clicked.connect(self.move_plate_out)
        self.introwindow.calibrate_button.clicked.connect(self.initialize_calibration)
        self.current_plate = -1
        self.kinetic_status = 0
        

    def move_plate_out(self):
        self.machine.move_plate('1700.001900.00')
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Insert Plate.")
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setWindowTitle(_translate("self", "OSP", None))
        msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
        reply = msgBox.exec_()
        self.machine.move_plate('1000.001000.00')
        msgBox = QtGui.QMessageBox()
        msgBox.setText("Plate ready.")
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.setIcon(QtGui.QMessageBox.Information)
        msgBox.setWindowTitle(_translate("self", "OSP", None))
        msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
        reply = msgBox.exec_()   

    def initialize_calibration(self):
        items = ("24 Well", "96 Well")
        item, ok = QtGui.QInputDialog.getItem(self, "Plate Selection", "Select plate type to calibrate", items,
                                              0, False)
        if ok and item:
            if item == "24 Well":
                self.machine.calibrate(1)
                self.load_calibration_data(24)
            elif item == "96 Well":
                self.machine.calibrate(2)
                self.load_calibration_data(96)

    def change_settings(self, argVal):
        if argVal == 0:
            self.introwindow.deleteLater()
        else:
            self.protocolselectionwindow.hide()
        self.settingswindow = settingsScreen()
        self.settingswindow.set_button.clicked.connect(lambda: self.update_settings(argVal))
        self.settingswindow.led1_spinBox.setValue(self.savedSettings[0])
        self.settingswindow.led2_spinBox.setValue(self.savedSettings[1])
        self.settingswindow.led3_spinBox.setValue(self.savedSettings[2])
        self.settingswindow.scanstoavg_spinbox.setValue(self.savedSettings[3])

    def update_settings(self, argVal):
        self.savedSettings[0] = self.settingswindow.led1_spinBox.value()
        self.savedSettings[1] = self.settingswindow.led2_spinBox.value()
        self.savedSettings[2] = self.settingswindow.led3_spinBox.value()
        self.savedSettings[3] = self.settingswindow.scanstoavg_spinbox.value()
        self.settingswindow.deleteLater()
        if argVal == 0:
            self.introwindow = mainScreen()
            self.introwindow.settings_button.clicked.connect(lambda: self.change_settings(0))
            self.introwindow.start_button.clicked.connect(lambda: self.start_plate_selection(0))
            self.introwindow.plateOut_button.clicked.connect(self.move_plate_out)
        else:
            self.protocolselectionwindow.show()
        self.save_settings()

    def start_plate_selection(self, argVal):
        if argVal == 0:
            self.introwindow.deleteLater()
        self.plateselectionwindow = plateOptionScreen()
        self.plateselectionwindow.back_button.clicked.connect(lambda: self.back_function(0, -1))
        self.plateselectionwindow.well24_button.clicked.connect(lambda: self.start_well_selection(0, 1))
        self.plateselectionwindow.well96_button.clicked.connect(lambda: self.start_well_selection(0, 2))

    def start_well_selection(self, argVal, argVal2):
        if argVal2 == 1:
            self.wellselectionwindow = wellSelectScreen24()
        elif argVal2 == 2:
            self.wellselectionwindow = wellSelectScreen96()

        if argVal == 0:
            self.plateselectionwindow.deleteLater()
            self.wellselectionwindow.back_button.clicked.connect(lambda: self.back_function(1, 0))
            argVal = 1
        elif argVal == 1:
            self.wellselectionwindow.back_button.clicked.connect(lambda: self.back_function(1, 2))
        self.wellselectionwindow.ready_button.clicked.connect(lambda: self.start_protocol_selection(argVal, argVal2))
        print "Total Plates: " + str(len(self.plateList))

    def start_protocol_selection(self, argVal, argVal2):
        self.wellselectionwindow.deleteLater()
        if argVal2 == 1:
            self.set_plate_type(24)
            self.current_plate = len(self.plateList)-1
        elif argVal2 == 2:
            self.set_plate_type(96)
            self.current_plate = len(self.plateList)-1

        welllist = []
        for w in range(0, len(self.wellselectionwindow.status)):
            if self.wellselectionwindow.status[w] == 'ON':
                welllist.append(w)

        self.select_wells(self.current_plate, welllist)
        self.protocolselectionwindow = protocolSelectScreen()
        self.protocolselectionwindow.abs_button.clicked.connect(lambda: self.open_protocol(1))
        self.protocolselectionwindow.flr_button.clicked.connect(lambda: self.open_protocol(2))
        self.protocolselectionwindow.aux_button.clicked.connect(lambda: self.open_protocol(3))
        self.protocolselectionwindow.kinetic_button.clicked.connect(lambda: self.open_protocol(4))
        self.protocolselectionwindow.shake_button.clicked.connect(lambda: self.open_protocol(5))
        self.protocolselectionwindow.new_plate_button.clicked.connect(lambda: self.add_new_plate_configuration(argVal2))
        self.protocolselectionwindow.load_button.clicked.connect(self.load_protocol_sequence)
        self.protocolselectionwindow.review_button.clicked.connect(self.review_protocols)
        self.protocolselectionwindow.settings_button.clicked.connect(lambda: self.change_settings(1))
        self.protocolselectionwindow.reset_button.clicked.connect(lambda: self.reset_system(2))

    def load_protocol_sequence(self):
        msgBox = QtGui.QMessageBox()
        msgBox.setText("If you continue with loading a protocol sequence "
                                           "from a file, then the current protocol "
                                           "sequence will be re-written.")
        msgBox.setInformativeText("Do you want to continue?")
        msgBox.setStandardButtons(QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        msgBox.setDefaultButton(QtGui.QMessageBox.Yes)
        msgBox.setIcon(QtGui.QMessageBox.Question)
        msgBox.setWindowTitle(_translate("self", "OSP", None))
        msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
        reply = msgBox.exec_()
        if reply == QtGui.QMessageBox.Yes:
            fileDir = QtGui.QFileDialog()
            fileDir.setDirectory('Protocols/')
            fileName = fileDir.getOpenFileName(self, 'OpenFile')
            with open(fileName, 'rb') as f:
                self.plateList = pickle.load(f)

            self.protocolselectionwindow.hide()
            self.reviewwindow = reviewScreen()
            self.reviewwindow.edit_button.clicked.connect(lambda: self.get_current_item(0))
            self.reviewwindow.remove_button.clicked.connect(lambda: self.get_current_item(1))
            self.reviewwindow.save_button.clicked.connect(self.save_protocol_sequence)
            self.reviewwindow.start_button.clicked.connect(self.start_program)
            self.reviewwindow.back_button.clicked.connect(lambda: self.back_function(7, 2))
            self.reviewwindow.reset_button.clicked.connect(lambda: self.reset_system(1))

            for p in range(0, len(self.plateList)):
                self.add_items(self.reviewwindow.protocol_tree.invisibleRootItem(), p)

    def save_protocol_sequence(self):
        fileDir = QtGui.QFileDialog()
        fileDir.setDirectory('Protocols/')
        fileName = fileDir.getSaveFileName(self, 'Save File')
        with open(fileName, 'wb') as f:
            pickle.dump(self.plateList, f)

    def add_new_plate_configuration(self, argVal):
        if self.kinetic_status == 0:
            self.protocolselectionwindow.hide()
            self.start_well_selection(1, argVal)

    def back_function(self, argVal, argVal2):
        if argVal == 0:  # If on plate selection
            self.plateselectionwindow.deleteLater()
        elif argVal == 1:  # If on well selection
            self.wellselectionwindow.deleteLater()
        elif argVal == 3:  # If on absorbance window
            self.absorbancewindow.deleteLater()
        elif argVal == 4:  # If on fluorescence window
            self.flrwindow.deleteLater()
        elif argVal == 5:  # If on auxiliary window
            self.auxwindow.deleteLater()
        elif argVal == 6:  # If on kinetic window
            self.kinwindow.deleteLater()
        elif argVal == 7:  # If on review window
            self.reviewwindow.deleteLater()

        if argVal2 == -1:  # If going to main screen
            self.introwindow = mainScreen()
            self.introwindow.settings_button.clicked.connect(lambda: self.change_settings(0))
            self.introwindow.start_button.clicked.connect(lambda: self.start_plate_selection(0))
            self.introwindow.plateOut_button.clicked.connect(self.move_plate_out)
        elif argVal2 == 0:  # If going to plate selections
            self.plateselectionwindow = plateOptionScreen()
            self.plateselectionwindow.well24_button.clicked.connect(lambda: self.start_well_selection(0, 1))
            self.plateselectionwindow.well96_button.clicked.connect(lambda: self.start_well_selection(0, 2))
            self.plateselectionwindow.back_button.clicked.connect(lambda: self.back_function(0, -1))

        elif argVal2 == 2:  # If going to protocol selection
            self.protocolselectionwindow.show()
        elif argVal2 == 7:  # If going to review screen
            self.reviewwindow.show()

    def open_protocol(self, argVal):
        self.protocolselectionwindow.hide()
        if argVal == 1:  # Absorbance window
            self.absorbancewindow = absScreen()
            self.absorbancewindow.back_button.clicked.connect(lambda: self.back_function(3, 2))
            self.absorbancewindow.set_button.clicked.connect(lambda: self.add_protocol(1))
        elif argVal == 2:  # Fluorescence window
            self.flrwindow = flrScreen()
            self.flrwindow.led1_checkBox.setText('LED 1 ('+str(self.savedSettings[0])+'nm)')
            self.flrwindow.led2_checkBox.setText('LED 2 (' + str(self.savedSettings[1]) + 'nm)')
            self.flrwindow.led3_checkBox.setText('LED 3 (' + str(self.savedSettings[2]) + 'nm)')
            self.flrwindow.back_button.clicked.connect(lambda: self.back_function(4, 2))
            self.flrwindow.set_button.clicked.connect(lambda: self.add_protocol(2))
        elif argVal == 3:  # Auxiliary window
            self.auxwindow = auxScreen()
            self.auxwindow.back_button.clicked.connect(lambda: self.back_function(5, 2))
            self.auxwindow.set_button.clicked.connect(lambda: self.add_protocol(3))
        elif argVal == 4:  # Kinetic window
            if self.kinetic_status == 0:
                self.kinwindow = kineticScreen()
                self.kinwindow.set_button.clicked.connect(lambda: self.add_protocol(4))
                self.kinwindow.back_button.clicked.connect(lambda: self.back_function(6, 2))
            elif self.kinetic_status == 1:
                self.add_protocol(4)
        elif argVal == 5: # Shaking 
            self.add_protocol(5)
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Shaking has been added.")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setIcon(QtGui.QMessageBox.Information)
            msgBox.setWindowTitle(_translate("self", "OSP", None))
            msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
            reply = msgBox.exec_()
            self.protocolselectionwindow.show()

    def add_protocol(self, argVal):
        if argVal == 1:  # Absorbance window
            exposure_time = self.absorbancewindow.expTime_singWave_spinBox.value()
            self.absorbancewindow.deleteLater()
            self.protocolselectionwindow.show()
            if self.kinetic_status == 0:
                order = self.plateList[self.current_plate].get_protocol_count()
                self.add_absorbance_protocol(exposure_time, 'Absorbance', self.current_plate, order)
            elif self.kinetic_status == 1:
                kinetic_index = self.plateList[self.current_plate].get_protocol_count()-1
                kinetic_protocol = self.plateList[self.current_plate].get_protocol(kinetic_index)
                order = kinetic_protocol.get_protocol_count()
                self.add_kinetic_absorbance_protocol(exposure_time, 'Absorbance', self.current_plate, kinetic_index, order)
        elif argVal == 2:  # Fluorescence window
            exposure_time = self.flrwindow.expTime_singWave_spinBox.value()
            led_index_total = ''
            wavelengths = [0, 0, 0, 0]
            if self.flrwindow.led1_checkBox.isChecked() == 1:
                led_index_total = led_index_total + '1'
                wavelengths[0] = self.savedSettings[0]
            else:
                led_index_total = led_index_total + '0'
                wavelengths[0] = self.savedSettings[0]

            if self.flrwindow.led2_checkBox.isChecked() == 1:
                led_index_total = led_index_total + '1'
                wavelengths[1] = self.savedSettings[1]
            else:
                led_index_total = led_index_total + '0'
                wavelengths[1] = self.savedSettings[1]

            if self.flrwindow.led3_checkBox.isChecked() == 1:
                led_index_total = led_index_total + '1'
                wavelengths[2] = self.savedSettings[2]
            else:
                led_index_total = led_index_total + '0'
                wavelengths[2] = self.savedSettings[2]

            if self.flrwindow.led4_checkBox.isChecked() == 1:
                led_index_total = led_index_total + '1'
                wavelengths[3] = 0
            else:
                led_index_total = led_index_total + '0'
                wavelengths[3] = 0

            if led_index_total != '0000':
                self.flrwindow.deleteLater()
                self.protocolselectionwindow.show()
                if self.kinetic_status == 0:
                    order = self.plateList[self.current_plate].get_protocol_count()
                    self.add_fluorescence_protocol(exposure_time, led_index_total, wavelengths[0], wavelengths[1],
                                                   wavelengths[2], 'Fluorescence', self.current_plate, order)
                elif self.kinetic_status == 1:
                    kinetic_index = self.plateList[self.current_plate].get_protocol_count() - 1
                    kinetic_protocol = self.plateList[self.current_plate].get_protocol(kinetic_index)
                    order = kinetic_protocol.get_protocol_count()
                    self.add_kinetic_fluorescence_protocol(exposure_time, led_index_total, wavelengths[0], wavelengths[1],
                                                   wavelengths[2], 'Fluorescence', self.current_plate, kinetic_index, order)
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText("You have not selected an excitation LED!")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle(_translate("self", "OSP", None))
                msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
                reply = msgBox.exec_()
        elif argVal == 3:  # Auxiliary window
            if self.auxwindow.ctrl1_checkBox.isChecked() == 1:
                aux_index = 1
                duration = self.auxwindow.duration_C1_spinBox.value()
            elif self.auxwindow.ctrl2_checkBox.isChecked() == 1:
                aux_index = 2
                duration = self.auxwindow.duration_C2_spinBox.value()
            elif self.auxwindow.ctrl3_checkBox.isChecked() == 1:
                aux_index = 3
                duration = self.auxwindow.duration_C3_spinBox.value()
            elif self.auxwindow.aux_led_checkBox.isChecked() == 1:
                aux_index = 4
                duration = self.auxwindow.duration_AL_spinBox.value()
            else:
                aux_index = 0

            if aux_index != 0:
                self.auxwindow.deleteLater()
                self.protocolselectionwindow.show()
                if self.kinetic_status == 0:
                    order = self.plateList[self.current_plate].get_protocol_count()
                    self.add_auxiliary_protocol(aux_index, duration, 'Auxiliary', self.current_plate, order)
                elif self.kinetic_status == 1:
                    kinetic_index = self.plateList[self.current_plate].get_protocol_count() - 1
                    kinetic_protocol = self.plateList[self.current_plate].get_protocol(kinetic_index)
                    order = kinetic_protocol.get_protocol_count()
                    self.add_kinetic_auxiliary_protocol(aux_index, duration, 'Auxiliary',
                                                           self.current_plate, kinetic_index, order)
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText("You have not selected an auxiliary port!")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle(_translate("self", "OSP", None))
                msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
                reply = msgBox.exec_()
        elif argVal == 4:  # Kinetic Toggle
            if self.kinetic_status == 0:  # If kinetics is being turned ON
                kin_method = 0  # Used to keep track of which method (interval or repeat) user has checked
                if self.kinwindow.interval_checkBox.isChecked() == 1:
                    kin_method = 1  # Interval method
                    order = self.plateList[self.current_plate].get_protocol_count()
                    self.turn_kinetic_tracking_on(kin_method, self.kinwindow.timeInterval_spinBox.value(),
                                                  self.kinwindow.duration_spinBox.value(),
                                                  self.kinwindow.numbRepeats_spinBox.value(), 'Kinetic',
                                                  self.current_plate, order)
                elif self.kinwindow.repeat_checkBox.isChecked() == 1:
                    kin_method = 2  # Repeat method
                    order = self.plateList[self.current_plate].get_protocol_count()
                    self.turn_kinetic_tracking_on(kin_method, self.kinwindow.timeInterval_spinBox.value(),
                                                  self.kinwindow.duration_spinBox.value(),
                                                  self.kinwindow.numbRepeats_spinBox.value(), 'Kinetic',
                                                  self.current_plate, order)
                if kin_method != 0:  # Used to check if user has checked one of the methods
                    self.protocolselectionwindow.setStyleSheet(
                        _fromUtf8("background-color: red;\n""font: 75 20pt \"Roboto\";"))
                    self.protocolselectionwindow.show()
                    self.kinwindow.deleteLater()
                    self.kinetic_status = 1
                else:
                    msgBox = QtGui.QMessageBox()
                    msgBox.setText("You have not checked a kinetic method!")
                    msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                    msgBox.setIcon(QtGui.QMessageBox.Warning)
                    msgBox.setWindowTitle(_translate("self", "OSP", None))
                    msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
                    reply = msgBox.exec_()

            elif self.kinetic_status == 1:  # If kinetics is being turned OFF
                self.protocolselectionwindow.setStyleSheet(_fromUtf8("background-color: rgb(0, 122, 179);"
                                                                     "\n""font: 75 20pt \"Roboto\";"))
                self.protocolselectionwindow.show()
                kinetic_index = self.plateList[self.current_plate].get_protocol_count()-1
                kinetic_protocol = self.plateList[self.current_plate].get_protocol(kinetic_index)
                for p in range(0, kinetic_protocol.get_protocol_count()):
                    kinetic_protocol.get_protocol_brief_description(p)

                self.kinetic_status = 0
        elif argVal == 5: # Shake
            if self.kinetic_status == 0:
                order = self.plateList[self.current_plate].get_protocol_count()
                self.add_shake_protocol('Shake', self.current_plate, order)
            elif self.kinetic_status == 1:
                kinetic_index = self.plateList[self.current_plate].get_protocol_count()-1
                kinetic_protocol = self.plateList[self.current_plate].get_protocol(kinetic_index)
                order = kinetic_protocol.get_protocol_count()
                self.add_kinetic_shake_protocol(self.current_plate, kinetic_index, order)

    def review_protocols(self):
        if self.kinetic_status == 0:
            self.protocolselectionwindow.hide()
            self.reviewwindow = reviewScreen()
            self.reviewwindow.edit_button.clicked.connect(lambda: self.get_current_item(0))
            self.reviewwindow.remove_button.clicked.connect(lambda: self.get_current_item(1))
            self.reviewwindow.save_button.clicked.connect(self.save_protocol_sequence)
            self.reviewwindow.start_button.clicked.connect(self.initialize_program)
            self.reviewwindow.back_button.clicked.connect(lambda: self.back_function(7, 2))
            self.reviewwindow.reset_button.clicked.connect(lambda: self.reset_system(1))

            for p in range(0, len(self.plateList)):
                self.add_items(self.reviewwindow.protocol_tree.invisibleRootItem(), p)

        elif self.kinetic_status == 1:
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Kinetic tracking is still on. Turn off before continuing.")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle(_translate("self", "OSP", None))
            msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
            reply = msgBox.exec_()
    def initialize_program(self):
        text, ok = QtGui.QInputDialog.getText(self, 'Text Input Dialog', 'Enter filename:')
        if ok:
            self.start_program(self.plateList, str(text))
            self.reset_system(0)

    def reset_system(self, argVal):
        if argVal == 0:
            self.reviewwindow.deleteLater()
            self.__init__(1)
            self.load_calibration_data(24)
            msgBox = QtGui.QMessageBox()
            msgBox.setText("Protocol finished. System Reset!")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setIcon(QtGui.QMessageBox.Information)
            msgBox.setWindowTitle(_translate("self", "OSP", None))
            msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
            reply = msgBox.exec_()
        elif argVal == 1:
            self.reviewwindow.deleteLater()
            self.__init__(1)
            msgBox = QtGui.QMessageBox()
            msgBox.setText("System Reset!")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setIcon(QtGui.QMessageBox.Information)
            msgBox.setWindowTitle(_translate("self", "OSP", None))
            msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
            reply = msgBox.exec_()
        elif argVal == 2:
            self.protocolselectionwindow.deleteLater()
            self.__init__(1)
            msgBox = QtGui.QMessageBox()
            msgBox.setText("System Reset!")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.setIcon(QtGui.QMessageBox.Information)
            msgBox.setWindowTitle(_translate("self", "OSP", None))
            msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
            reply = msgBox.exec_()    

    def add_items(self, parent, item_numb):
        column = 0
        # Adding Plate # Item to top of tree
        plate_name = 'Plate ' + str(item_numb+1)
        plate_item = self.add_parent(parent, column, plate_name, '')

        # Adding Selected Wells item below specific Plate #
        well_item = self.add_child(plate_item, column, 'Selected Wells', '')

        # Adding string of selected wells under the Selected Wells Item
        [selected_well_string, selected_well_labels, selected_well_index] = self.plateList[item_numb].get_selected_wells()

        if selected_well_string == '':
            selected_well_string = 'NONE'

        self.add_subchild(well_item, column, selected_well_string, '')

        # Adding protocol items, based on the order of selection in protocolList
        protocol_item = self.add_child(plate_item, column, 'Protocols', '')
        for p in range(0, self.plateList[item_numb].get_protocol_count()):
            protocol_object = self.plateList[item_numb].get_protocol(p)
            protocol_name = protocol_object.label
            if protocol_name == 'Absorbance':
                protocol = self.add_child(protocol_item, column, protocol_name, '')
                self.add_subchild(protocol, column, 'Exposure Time: ' + str(protocol_object.get_exposure_time()) + ' ms'
                                  , '')
            elif protocol_name == 'Fluorescence':
                protocol = self.add_child(protocol_item, column, protocol_name, '')
                self.add_subchild(protocol, column, 'Exposure Time: ' + str(protocol_object.get_exposure_time()) + ' ms'
                                  , '')
                self.add_subchild(protocol, column, 'LED #: ' + str(protocol_object.get_led_index())
                                 + ' (' + str(protocol_object.get_wavelength()) + ' nm)', '')
            elif protocol_name == 'Auxiliary':
                protocol = self.add_child(protocol_item, column, protocol_name, '')
                self.add_subchild(protocol, column, 'Duration: ' + str(protocol_object.get_duration()) + ' ms', '')
                self.add_subchild(protocol, column, 'Port #: ' + str(protocol_object.get_aux_index()), '')
            elif protocol_name == 'Shake':
                protocol = self.add_child(protocol_item, column, protocol_name, '')
            elif protocol_name == 'Kinetic':
                protocol = self.add_child(protocol_item, column, protocol_name, '')
                protocol_settings = self.add_child(protocol, column, 'Settings', '')
                if protocol_object.method == 1:
                    self.add_subchild(protocol_settings, column, 'Interval: ' + str(protocol_object.interval) + ' ms',
                                      '')
                    self.add_subchild(protocol_settings, column, 'Duration: ' + str(protocol_object.duration) + ' ms',
                                      '')
                elif protocol_object.method == 2:
                    self.add_subchild(protocol_settings, column, 'Number of Repeats: ' + str(protocol_object.reps), '')

                protocol_program = self.add_child(protocol, column, 'Program', '')
                for kp in range(0, protocol_object.get_protocol_count()):
                    kinetic_protocol = protocol_object.get_protocol(kp)
                    kinetic_protocol_name = kinetic_protocol.label
                    if kinetic_protocol_name == 'Absorbance':
                        protocol = self.add_child(protocol_program, column, kinetic_protocol_name, '')
                        self.add_subchild(protocol, column, 'Exposure Time: ' +
                                          str(kinetic_protocol.get_exposure_time()) + ' ms', '')
                    elif kinetic_protocol_name == 'Fluorescence':
                        protocol = self.add_child(protocol_program, column, kinetic_protocol_name, '')
                        self.add_subchild(protocol, column,'Exposure Time: ' + str(kinetic_protocol.get_exposure_time())
                                          + ' ms', '')
                        self.add_subchild(protocol, column, 'LED #: ' + str(kinetic_protocol.get_led_index()) +
                                          ' (' + str(kinetic_protocol.get_wavelength()) + ' nm)', '')
                    elif kinetic_protocol_name == 'Auxiliary':
                        protocol = self.add_child(protocol_item, column, kinetic_protocol_name, '')
                        self.add_subchild(protocol, column, 'Duration: ' + str(kinetic_protocol.get_duration()) + ' ms',
                                          '')
                        self.add_subchild(protocol, column, 'Port #: ' + str(kinetic_protocol.get_aux_index()), '')
                    elif kinetic_protocol_name == 'Shake':
                        protocol = self.add_child(protcol_item, column, kinetic_protocol_name, '')


    def get_current_item(self, argVal):
        current_item = self.reviewwindow.protocol_tree.currentItem()
        if str(current_item.text(0)).split(' ')[0] == 'Plate' and argVal == 1:
            item_plate = str(current_item.text(0)).split(' ')[1]
            self.remove_plate(item_plate)
        else:
            current_item_parent = current_item.parent()
            current_item_parent_label = str(current_item_parent.text(0))

            if current_item_parent_label.split(' ')[0] == 'Plate':
                item_plate = current_item_parent_label.split(' ')[1]
                item_index = current_item_parent.indexOfChild(current_item)
                if item_index == 0:  # Well configuration edit selected
                    self.edit_protocol_selection(1, int(item_plate), -1)
                elif item_index == 1:  # Plate Protocol header item selected
                    msgBox = QtGui.QMessageBox()
                    msgBox.setText("You cannot do that. Please select a specific protocol "
                                                               "or plate configutation to edit.")
                    msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                    msgBox.setIcon(QtGui.QMessageBox.Warning)
                    msgBox.setWindowTitle(_translate("self", "OSP", None))
                    msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
                    reply = msgBox.exec_()
            elif current_item_parent_label.split(' ')[0] == 'Kinetic':
                current_item_grandparent = current_item_parent.parent()
                current_item_grand_grandparent = current_item_grandparent.parent()
                item_plate = current_item_grand_grandparent.text(0).split(' ')[1]
                item_index = current_item_parent.indexOfChild(current_item)
                parent_index = current_item_grandparent.indexOfChild(current_item_parent)
                if item_index == 0:  # Kinetic Settings selected
                    if argVal == 0:
                        self.edit_protocol_selection(6, int(item_plate), int(parent_index))
                    elif argVal == 1:
                        self.remove_protocol_selection(6, int(item_plate), int(parent_index))

            elif current_item_parent_label.split(' ')[0] == 'Program':
                current_item_grandparent = current_item_parent.parent()
                current_item_grand_grandparent = current_item_grandparent.parent()
                current_item_grand_grand_grandparent = current_item_grand_grandparent.parent()
                item_plate = current_item_grand_grand_grandparent.text(0).split(' ')[1]
                item_index = current_item_parent.indexOfChild(current_item)
                grandparent_index = current_item_grand_grandparent.indexOfChild(current_item_grandparent)
                item_kinetic_obj = self.plateList[int(item_plate) - 1].get_protocol(grandparent_index)
                item_kinetic_protocol = item_kinetic_obj.get_protocol(item_index)
                item_label = item_kinetic_protocol.label
                if item_label == 'Absorbance':
                    item_type = 2
                elif item_label == 'Fluorescence':
                    item_type = 3
                elif item_label == 'Auxiliary':
                    item_type = 4
                if argVal == 0:
                    self.edit_kinetic_protocol_selection(item_type, int(item_plate), item_kinetic_obj, item_kinetic_protocol,  item_index)
                elif argVal == 1:
                    self.remove_kinetic_protocol_selection(item_type, int(item_plate), item_kinetic_obj,
                                                         item_kinetic_protocol, item_index)
            else:
                current_item_grandparent = current_item_parent.parent()
                item_plate = current_item_grandparent.text(0).split(' ')[1]
                item_index = current_item_parent.indexOfChild(current_item)
                item_protocol = self.plateList[int(item_plate) - 1].get_protocol(item_index)
                item_label = item_protocol.label
                if item_label == 'Absorbance':
                    item_type = 2
                elif item_label == 'Fluorescence':
                    item_type = 3
                elif item_label == 'Auxiliary':
                    item_type = 4
                elif item_label == 'Kinetic':
                    item_type = 5
                if argVal == 0:
                    self.edit_protocol_selection(item_type, int(item_plate), item_index)
                elif argVal == 1:
                    self.remove_protocol_selection(item_type, int(item_plate), item_index)

    def remove_plate(self, plate_numb):
        self.reviewwindow.deleteLater()
        self.remove_plate_object(plate_numb)
        self.current_plate = len(self.plateList)-1
        self.reviewwindow = reviewScreen()
        self.reviewwindow.edit_button.clicked.connect(lambda: self.get_current_item(0))
        self.reviewwindow.remove_button.clicked.connect(lambda: self.get_current_item(1))
        self.reviewwindow.save_button.clicked.connect(self.save_protocol_sequence)
        self.reviewwindow.start_button.clicked.connect(self.start_program)
        self.reviewwindow.back_button.clicked.connect(lambda: self.back_function(7, 2))
        self.reviewwindow.reset_button.clicked.connect(lambda: self.reset_system(1))

        for p in range(0, len(self.plateList)):
            self.add_items(self.reviewwindow.protocol_tree.invisibleRootItem(), p)

    def remove_protocol_selection(self, protocol_type, plate_numb, protocol_index):
        plate_numb = plate_numb - 1
        self.reviewwindow.deleteLater()
        plate_obj = self.plateList[plate_numb]
        plate_obj.remove_protocol(protocol_index)

        self.reviewwindow = reviewScreen()
        self.reviewwindow.edit_button.clicked.connect(lambda: self.get_current_item(0))
        self.reviewwindow.remove_button.clicked.connect(lambda: self.get_current_item(1))

        self.reviewwindow.save_button.clicked.connect(self.save_protocol_sequence)
        self.reviewwindow.start_button.clicked.connect(self.start_program)
        self.reviewwindow.back_button.clicked.connect(lambda: self.back_function(7, 2))
        self.reviewwindow.reset_button.clicked.connect(lambda: self.reset_system(1))

        for p in range(0, len(self.plateList)):
            self.add_items(self.reviewwindow.protocol_tree.invisibleRootItem(), p)

    def edit_protocol_selection(self, protocol_type, plate_numb, protocol_index):
        # Protocol Type Key: 1 - Well configuration
        #                    2 - Absorbance
        #                    3 = Fluorescence
        #                    4 - Auxiliary
        #                    6 - Kinetic Settings
        plate_numb = plate_numb - 1
        if protocol_type == 1:
            self.reviewwindow.hide()
            plate_obj = self.plateList[plate_numb]
            plate_well_status = plate_obj.get_well_status()
            plate_type = plate_obj.well_numb
            if plate_type == 24:
                self.wellselectionwindow = wellSelectScreen24()
                self.wellselectionwindow.ready_button.clicked.connect(lambda: self.update_protocol( protocol_type,
                                                                                                    plate_numb,
                                                                                                    protocol_index))
                self.wellselectionwindow.back_button.clicked.connect(lambda: self.back_function(1, 7))
            for child in self.wellselectionwindow.findChildren(QtGui.QLabel):
                if str(child.objectName()) in self.wellselectionwindow.wellNames:
                    name = str(child.objectName())
                    label = name[5:len(name)]
                    row = name[5]
                    column = int(name[6:len(name)])
                    if plate_well_status[self.wellselectionwindow.names.index(label)] == 'OFF':
                        child.setPixmap(QtGui.QPixmap(_fromUtf8("Images/emptyWell_Icon.svg")))
                        self.wellselectionwindow.status[self.wellselectionwindow.names.index(label)] = 'OFF'
                    elif plate_well_status[self.wellselectionwindow.names.index(label)] == 'ON':
                        child.setPixmap(QtGui.QPixmap(_fromUtf8("Images/selectedWell_Icon.png")))
                        self.wellselectionwindow.status[self.wellselectionwindow.names.index(label)] = 'ON'
        elif protocol_type == 2:
            self.reviewwindow.hide()
            self.absorbancewindow = absScreen()
            self.absorbancewindow.set_button.clicked.connect(lambda: self.update_protocol(protocol_type, plate_numb, protocol_index))
            self.absorbancewindow.back_button.clicked.connect(lambda: self.back_function(3, 7))
            plate_obj = self.plateList[plate_numb]
            protocol_obj = plate_obj.get_protocol(protocol_index)

            self.absorbancewindow.expTime_singWave_spinBox.setValue(protocol_obj.get_exposure_time())
        elif protocol_type == 3:
            self.reviewwindow.hide()
            self.flrwindow = flrScreen()
            self.flrwindow.set_button.clicked.connect(lambda: self.update_protocol(protocol_type, plate_numb, protocol_index))
            self.flrwindow.back_button.clicked.connect(lambda: self.back_function(4, 7))
            plate_obj = self.plateList[plate_numb]
            protocol_obj = plate_obj.get_protocol(protocol_index)
            protocol_led = protocol_obj.get_led_index()

            self.flrwindow.expTime_singWave_spinBox.setValue(protocol_obj.get_exposure_time())
            if protocol_led[0] == '1': 
                self.flrwindow.led1_checkBox.setChecked(True)
                self.flrwindow.led1_checkBox.setEnabled(True)
                # self.flrwindow.led2_checkBox.setEnabled(False)
                # self.flrwindow.led3_checkBox.setEnabled(False)
                # self.flrwindow.led4_checkBox.setEnabled(False)
                self.flrwindow.ledOn = protocol_led
            elif protocol_led[1] == '1': 
                # self.flrwindow.led1_checkBox.setEnabled(False)
                self.flrwindow.led2_checkBox.setEnabled(True)
                self.flrwindow.led2_checkBox.setChecked(True)
                # self.flrwindow.led3_checkBox.setEnabled(False)
                # self.flrwindow.led4_checkBox.setEnabled(False)
                self.flrwindow.ledOn = protocol_led
            elif protocol_led[2] == '1': 
                # self.flrwindow.led1_checkBox.setEnabled(False)
                # self.flrwindow.led2_checkBox.setEnabled(False)
                self.flrwindow.led3_checkBox.setEnabled(True)
                self.flrwindow.led3_checkBox.setChecked(True)
                # self.flrwindow.led4_checkBox.setEnabled(False)
                self.flrwindow.ledOn = protocol_led
            elif protocol_led[3] == '1':
                # self.flrwindow.led1_checkBox.setEnabled(False)
                # self.flrwindow.led2_checkBox.setEnabled(False)
                # self.flrwindow.led3_checkBox.setEnabled(False)
                self.flrwindow.led4_checkBox.setEnabled(True)
                self.flrwindow.led4_checkBox.setChecked(True)
                self.flrwindow.ledOn = protocol_led
        elif protocol_type == 4:
            self.reviewwindow.hide()
            self.auxwindow = auxScreen()
            self.auxwindow.set_button.clicked.connect(
                lambda: self.update_protocol(protocol_type, plate_numb, protocol_index))
            self.auxwindow.back_button.clicked.connect(lambda: self.back_function(5, 7))
            plate_obj = self.plateList[plate_numb]
            protocol_obj = plate_obj.get_protocol(protocol_index)
            protocol_port = protocol_obj.get_aux_index()
            protocol_duration = protocol_obj.get_duration()

            if protocol_port == 1:
                self.auxwindow.ctrl1_checkBox.setChecked(True)
                self.auxwindow.duration_C1_label.setEnabled(True)
                self.auxwindow.duration_C1_spinBox.setEnabled(True)
                self.auxwindow.duration_C2_label.setEnabled(False)
                self.auxwindow.duration_C2_spinBox.setEnabled(False)
                self.auxwindow.duration_C3_label.setEnabled(False)
                self.auxwindow.duration_C3_spinBox.setEnabled(False)
                self.auxwindow.ctrl1_checkBox.setEnabled(True)
                self.auxwindow.ctrl2_checkBox.setEnabled(False)
                self.auxwindow.ctrl3_checkBox.setEnabled(False)
            elif protocol_port == 2:
                self.auxwindow.duration_C1_label.setEnabled(False)
                self.auxwindow.duration_C1_spinBox.setEnabled(False)
                self.auxwindow.ctrl2_checkBox.setChecked(True)
                self.auxwindow.duration_C2_label.setEnabled(True)
                self.auxwindow.duration_C2_spinBox.setEnabled(True)
                self.auxwindow.duration_C3_label.setEnabled(False)
                self.auxwindow.duration_C3_spinBox.setEnabled(False)
                self.auxwindow.ctrl1_checkBox.setEnabled(False)
                self.auxwindow.ctrl2_checkBox.setEnabled(True)
                self.auxwindow.ctrl3_checkBox.setEnabled(False)
            elif protocol_port == 3:
                self.auxwindow.duration_C1_label.setEnabled(False)
                self.auxwindow.duration_C1_spinBox.setEnabled(False)
                self.auxwindow.duration_C2_label.setEnabled(False)
                self.auxwindow.duration_C2_spinBox.setEnabled(False)
                self.auxwindow.ctrl3_checkBox.setChecked(True)
                self.auxwindow.duration_C3_label.setEnabled(True)
                self.auxwindow.duration_C3_spinBox.setEnabled(True)
                self.auxwindow.ctrl1_checkBox.setEnabled(False)
                self.auxwindow.ctrl2_checkBox.setEnabled(False)
                self.auxwindow.ctrl3_checkBox.setEnabled(True)
        elif protocol_type == 6:
            self.reviewwindow.hide()
            self.kinwindow = kineticScreen()
            self.kinwindow.set_button.clicked.connect(
                lambda: self.update_protocol(protocol_type, plate_numb, protocol_index))
            self.kinwindow.back_button.clicked.connect(lambda: self.back_function(6, 7))
            plate_obj = self.plateList[plate_numb]
            protocol_obj = plate_obj.get_protocol(protocol_index)
            protocol_mode = protocol_obj.method
            if protocol_mode == 1:
                self.kinwindow.interval_checkBox.setChecked(True)
                self.kinwindow.interval_checkBox.setEnabled(True)
                self.kinwindow.timeInterval_spinBox.setEnabled(True)
                self.kinwindow.timeInterval_label.setEnabled(True)
                self.kinwindow.duration_spinBox.setEnabled(True)
                self.kinwindow.duration_label.setEnabled(True)
                self.kinwindow.repeat_checkBox.setEnabled(False)
                self.kinwindow.numbRepeats_spinBox.setEnabled(False)
                self.kinwindow.numbRepeats_label.setEnabled(False)
            elif protocol_mode == 2:
                self.kinwindow.repeat_checkBox.setChecked(True)
                self.kinwindow.repeat_checkBox.setEnabled(True)
                self.kinwindow.numbRepeats_spinBox.setEnabled(True)
                self.kinwindow.numbRepeats_label.setEnabled(True)
                self.kinwindow.interval_checkBox.setEnabled(False)
                self.kinwindow.timeInterval_spinBox.setEnabled(False)
                self.kinwindow.timeInterval_label.setEnabled(False)
                self.kinwindow.duration_spinBox.setEnabled(False)
                self.kinwindow.duration_label.setEnabled(False)

    def update_protocol(self, protocol_type, plate_numb, protocol_index):
        protocol_check = 0
        if protocol_type == 1:
            welllist = []
            for w in range(0, len(self.wellselectionwindow.status)):
                if self.wellselectionwindow.status[w] == 'ON':
                    welllist.append(w)
            self.clear_wells(plate_numb)
            self.select_wells(plate_numb, welllist)
            self.wellselectionwindow.deleteLater()
            protocol_check = 1
        elif protocol_type == 2:
            plate_obj = self.plateList[plate_numb]
            protocol_obj = plate_obj.get_protocol(protocol_index)
            protocol_obj.set_exposure_time(self.absorbancewindow.expTime_singWave_spinBox.value())
            self.absorbancewindow.deleteLater()
            protocol_check = 1
        elif protocol_type == 3:
            plate_obj = self.plateList[plate_numb]
            protocol_obj = plate_obj.get_protocol(protocol_index)
            protocol_obj.set_exposure_time(self.flrwindow.expTime_singWave_spinBox.value())
            led_check = 0
            if self.flrwindow.led1_checkBox.isChecked() == 1:
                protocol_obj.set_excitation_source(1, self.savedSettings[0])
                led_check = 1
            elif self.flrwindow.led2_checkBox.isChecked() == 1:
                protocol_obj.set_excitation_source(2, self.savedSettings[1])
                led_check = 1
            elif self.flrwindow.led3_checkBox.isChecked() == 1:
                protocol_obj.set_excitation_source(3, self.savedSettings[2])
                led_check = 1
            elif self.flrwindow.led4_checkBox.isChecked() == 1:
                protocol_obj.set_excitation_source(4, self.savedSettings[3])
                led_check = 1
            else:
                led_check = 0

            if led_check != 0:
                self.flrwindow.deleteLater()
                protocol_check = 1
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText("You have not selected an excitation LED!")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle(_translate("self", "OSP", None))
                msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
                reply = msgBox.exec_()
        elif protocol_type == 4:
            plate_obj = self.plateList[plate_numb]
            protocol_obj = plate_obj.get_protocol(protocol_index)
            port_check = 0
            if self.auxwindow.ctrl1_checkBox.isChecked() == 1:
                protocol_obj.set_aux_index(1)
                protocol_obj.set_duration(self.auxwindow.duration_C1_spinBox.value())
                port_check = 1
            elif self.auxwindow.ctrl2_checkBox.isChecked() == 1:
                protocol_obj.set_aux_index(2)
                protocol_obj.set_duration(self.auxwindow.duration_C2_spinBox.value())
                port_check = 1
            elif self.auxwindow.ctrl3_checkBox.isChecked() == 1:
                protocol_obj.set_aux_index(3)
                protocol_obj.set_duration(self.auxwindow.duration_C3_spinBox.value())
                port_check = 1

            if port_check != 0:
                self.auxwindow.deleteLater()
                protocol_check = 1
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText("You have not selected an auxiliary port!")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle(_translate("self", "OSP", None))
                msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
                reply = msgBox.exec_()
        elif protocol_type == 6:
            plate_obj = self.plateList[plate_numb]
            protocol_obj = plate_obj.get_protocol(protocol_index)
            method_check = 0
            if self.kinwindow.interval_checkBox.isChecked() == 1:
                protocol_obj.method = 1
                protocol_obj.interval = self.kinwindow.timeInterval_spinBox.value()
                protocol_obj.duration = self.kinwindow.duration_spinBox.value()
                method_check = 1
            elif self.kinwindow.repeat_checkBox.isChecked() == 1:
                protocol_obj.method = 2
                protocol_obj.reps = self.kinwindow.numbRepeats_spinBox.value()
                method_check = 1

            if method_check != 0:
                self.kinwindow.deleteLater()
                protocol_check = 1
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText("You have not selected kinetic method!")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle(_translate("self", "OSP", None))
                msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
                reply = msgBox.exec_()

        if protocol_check != 0:
            self.reviewwindow = reviewScreen()
            self.reviewwindow.edit_button.clicked.connect(self.get_current_item)
            self.reviewwindow.save_button.clicked.connect(self.save_protocol_sequence)
            self.reviewwindow.start_button.clicked.connect(self.start_program)
            self.reviewwindow.back_button.clicked.connect(lambda: self.back_function(7, 2))
            self.reviewwindow.reset_button.clicked.connect(lambda: self.reset_system(1))

            for p in range(0, len(self.plateList)):
                self.add_items(self.reviewwindow.protocol_tree.invisibleRootItem(), p)

    def edit_kinetic_protocol_selection(self, protocol_type, plate_numb, item_kinetic_obj, item_kinetic_protocol, protocol_index):
        # Protocol Type Key: 1 - ---
        #                    2 - Absorbance
        #                    3 - Fluorescence
        #                    4 - Auxiliary
        #                    5 - ---
        plate_numb = plate_numb - 1
        if protocol_type == 2:
            self.reviewwindow.hide()
            self.absorbancewindow = absScreen()
            self.absorbancewindow.set_button.clicked.connect(lambda: self.update_kinetic_protocol(protocol_type,
                                                                                                  plate_numb,
                                                                                                  item_kinetic_obj,
                                                                                                  item_kinetic_protocol,
                                                                                                  protocol_index))
            self.absorbancewindow.back_button.clicked.connect(lambda: self.back_function(3, 7))
            plate_obj = self.plateList[plate_numb]
            kinetic_obj = item_kinetic_obj
            protocol_obj = item_kinetic_protocol

            self.absorbancewindow.expTime_singWave_spinBox.setValue(protocol_obj.get_exposure_time())
        elif protocol_type == 3:
            self.reviewwindow.hide()
            self.flrwindow = flrScreen()
            self.flrwindow.set_button.clicked.connect(lambda: self.update_kinetic_protocol(protocol_type, plate_numb,
                                                                                           item_kinetic_obj,
                                                                                           item_kinetic_protocol,
                                                                                           protocol_index))
            self.flrwindow.back_button.clicked.connect(lambda: self.back_function(4, 7))
            plate_obj = self.plateList[plate_numb]
            plate_obj = self.plateList[plate_numb]
            kinetic_obj = item_kinetic_obj
            protocol_obj = item_kinetic_protocol
            protocol_led = protocol_obj.get_led_index()

            self.flrwindow.expTime_singWave_spinBox.setValue(protocol_obj.get_exposure_time())

            if protocol_led == 1:
                self.flrwindow.led1_checkBox.setChecked(True)
                self.flrwindow.led1_checkBox.setEnabled(True)
                self.flrwindow.led2_checkBox.setEnabled(False)
                self.flrwindow.led3_checkBox.setEnabled(False)
                self.flrwindow.led4_checkBox.setEnabled(False)
                self.flrwindow.ledOn = 1
            elif protocol_led == 2:
                self.flrwindow.led1_checkBox.setEnabled(False)
                self.flrwindow.led2_checkBox.setEnabled(True)
                self.flrwindow.led2_checkBox.setChecked(True)
                self.flrwindow.led3_checkBox.setEnabled(False)
                self.flrwindow.led4_checkBox.setEnabled(False)
                self.flrwindow.ledOn = 2
            elif protocol_led == 3:
                self.flrwindow.led1_checkBox.setEnabled(False)
                self.flrwindow.led2_checkBox.setEnabled(False)
                self.flrwindow.led3_checkBox.setEnabled(True)
                self.flrwindow.led3_checkBox.setChecked(True)
                self.flrwindow.led4_checkBox.setEnabled(False)
                self.flrwindow.ledOn = 3
            elif protocol_led == 4:
                self.flrwindow.led1_checkBox.setEnabled(False)
                self.flrwindow.led2_checkBox.setEnabled(False)
                self.flrwindow.led3_checkBox.setEnabled(False)
                self.flrwindow.led4_checkBox.setEnabled(True)
                self.flrwindow.led4_checkBox.setChecked(True)
                self.flrwindow.ledOn = 4
        elif protocol_type == 4:
            self.reviewwindow.hide()
            self.auxwindow = auxScreen()
            self.auxwindow.set_button.clicked.connect(
                lambda: self.update_kinetic_protocol(protocol_type, plate_numb, item_kinetic_obj, item_kinetic_protocol,
                                                     protocol_index))
            self.auxwindow.back_button.clicked.connect(lambda: self.back_function(5, 7))
            plate_obj = self.plateList[plate_numb]
            kinetic_obj = item_kinetic_obj
            protocol_obj = item_kinetic_protocol
            protocol_port = protocol_obj.get_aux_index()
            protocol_duration = protocol_obj.get_duration()

            if protocol_port == 1:
                self.auxwindow.ctrl1_checkBox.setChecked(True)
                self.auxwindow.duration_C1_label.setEnabled(True)
                self.auxwindow.duration_C1_spinBox.setEnabled(True)
                self.auxwindow.duration_C2_label.setEnabled(False)
                self.auxwindow.duration_C2_spinBox.setEnabled(False)
                self.auxwindow.duration_C3_label.setEnabled(False)
                self.auxwindow.duration_C3_spinBox.setEnabled(False)
                self.auxwindow.ctrl1_checkBox.setEnabled(True)
                self.auxwindow.ctrl2_checkBox.setEnabled(False)
                self.auxwindow.ctrl3_checkBox.setEnabled(False)
            elif protocol_port == 2:
                self.auxwindow.duration_C1_label.setEnabled(False)
                self.auxwindow.duration_C1_spinBox.setEnabled(False)
                self.auxwindow.ctrl2_checkBox.setChecked(True)
                self.auxwindow.duration_C2_label.setEnabled(True)
                self.auxwindow.duration_C2_spinBox.setEnabled(True)
                self.auxwindow.duration_C3_label.setEnabled(False)
                self.auxwindow.duration_C3_spinBox.setEnabled(False)
                self.auxwindow.ctrl1_checkBox.setEnabled(False)
                self.auxwindow.ctrl2_checkBox.setEnabled(True)
                self.auxwindow.ctrl3_checkBox.setEnabled(False)
            elif protocol_port == 3:
                self.auxwindow.duration_C1_label.setEnabled(False)
                self.auxwindow.duration_C1_spinBox.setEnabled(False)
                self.auxwindow.duration_C2_label.setEnabled(False)
                self.auxwindow.duration_C2_spinBox.setEnabled(False)
                self.auxwindow.ctrl3_checkBox.setChecked(True)
                self.auxwindow.duration_C3_label.setEnabled(True)
                self.auxwindow.duration_C3_spinBox.setEnabled(True)
                self.auxwindow.ctrl1_checkBox.setEnabled(False)
                self.auxwindow.ctrl2_checkBox.setEnabled(False)
                self.auxwindow.ctrl3_checkBox.setEnabled(True)

    def update_kinetic_protocol(self, protocol_type, plate_numb, item_kinetic_obj, item_kinetic_protocol, protocol_index):
        protocol_check = 0
        if protocol_type == 2:
            plate_obj = self.plateList[plate_numb]
            kinetic_obj = item_kinetic_obj
            protocol_obj = item_kinetic_protocol
            protocol_obj.set_exposure_time(self.absorbancewindow.expTime_singWave_spinBox.value())
            self.abswindow.deleteLater()
            protocol_check = 1
        elif protocol_type == 3:
            plate_obj = self.plateList[plate_numb]
            kinetic_obj = item_kinetic_obj
            protocol_obj = item_kinetic_protocol
            protocol_obj.set_exposure_time(self.flrwindow.expTime_singWave_spinBox.value())
            led_check = 0
            if self.flrwindow.led1_checkBox.isChecked() == 1:
                protocol_obj.set_excitation_source(1, self.savedSettings[0])
                led_check = 1
            elif self.flrwindow.led2_checkBox.isChecked() == 1:
                protocol_obj.set_excitation_source(2, self.savedSettings[1])
                led_check = 1
            elif self.flrwindow.led3_checkBox.isChecked() == 1:
                protocol_obj.set_excitation_source(3, self.savedSettings[2])
                led_check = 1
            elif self.flrwindow.led4_checkBox.isChecked() == 1:
                protocol_obj.set_excitation_source(4, self.savedSettings[3])
                led_check = 1
            else:
                led_check = 0

            if led_check != 0:
                self.flrwindow.deleteLater()
                protocol_check = 1
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText("You have not selected an excitation LED!")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle(_translate("self", "OSP", None))
                msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
                reply = msgBox.exec_()
        elif protocol_type == 4:
            plate_obj = self.plateList[plate_numb]
            kinetic_obj = item_kinetic_obj
            protocol_obj = item_kinetic_protocol
            port_check = 0
            if self.auxwindow.ctrl1_checkBox.isChecked() == 1:
                protocol_obj.set_aux_index(1)
                protocol_obj.set_duration(self.auxwindow.duration_C1_spinBox.value())
                port_check = 1
            elif self.auxwindow.ctrl2_checkBox.isChecked() == 1:
                protocol_obj.set_aux_index(2)
                protocol_obj.set_duration(self.auxwindow.duration_C2_spinBox.value())
                port_check = 1
            elif self.auxwindow.ctrl3_checkBox.isChecked() == 1:
                protocol_obj.set_aux_index(3)
                protocol_obj.set_duration(self.auxwindow.duration_C3_spinBox.value())
                port_check = 1

            if port_check != 0:
                self.auxwindow.deleteLater()
                protocol_check = 1
            else:
                msgBox = QtGui.QMessageBox()
                msgBox.setText("You have not selected an auxiliary port!")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle(_translate("self", "OSP", None))
                msgBox.setWindowIcon(QtGui.QIcon("Images/logo_icon.png"))
                reply = msgBox.exec_()

        if protocol_check != 0:
            self.reviewwindow = reviewScreen()
            self.reviewwindow.edit_button.clicked.connect(self.get_current_item)
            self.reviewwindow.save_button.clicked.connect(self.save_protocol_sequence)
            self.reviewwindow.start_button.clicked.connect(self.start_program)
            self.reviewwindow.back_button.clicked.connect(lambda: self.back_function(7, 2))
            self.reviewwindow.reset_button.clicked.connect(lambda: self.reset_system(1))

            for p in range(0, len(self.plateList)):
                self.add_items(self.reviewwindow.protocol_tree.invisibleRootItem(), p)

    # Function to add a parent item (QtGui.QTreeWidgetItem) to the primary tree widget
    @staticmethod
    def add_parent(parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
        item.setExpanded(True)
        return item

    # Function to add a child item (QtGui.QTreeWidgetItem) to the primary tree widget
    @staticmethod
    def add_child( parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setChildIndicatorPolicy(QtGui.QTreeWidgetItem.ShowIndicator)
        item.setExpanded(False)
        return item

    # Function to add a sub-child item (QtGui.QTreeWidgetItem) to the primary tree widget
    @staticmethod
    def add_subchild(parent, column, title, data):
        item = QtGui.QTreeWidgetItem(parent, [title])
        item.setData(column, QtCore.Qt.UserRole, data)
        item.setDisabled(True)
        return item


def main():
    import sys
    app = QtGui.QApplication(sys.argv)
    ex = GUI(0)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
