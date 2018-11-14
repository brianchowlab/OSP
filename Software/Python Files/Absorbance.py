from Protocol import *


class Absorbance(Protocol, object):
    ledIndex = 5  # Integer

    def __init__(self, expTime, label, plate, order):
        super(Absorbance, self).__init__(label, plate, order)
        self.__expTime = expTime  # Integer
        # self.__lightInt = lightInt  # Integer
        self.excel_length = 4

    def get_full_description(self):
        print "--- OVERALL DESCRIPTION ---"
        print "Label: " + self.label
        print "Plate #: " + str(self.plate)
        print "Order: " + str(self.order)
        print "- - - - - - - - - - - - - -"
        print "Exposure Time: " + str(self.__expTime) + " (ms)"
        # print "Light Intensity: " + str(self.__lightInt) + "%"
        print "LED: " + str(self.ledIndex)

    def get_exposure_time(self):
        return self.__expTime

    def set_exposure_time(self, time):
        self.__expTime = time

    # def set_light_intensity(self, intensity):
    #     self.__lightInt = intensity

    def initialize_excel_section(self, worksheet, merge_format, header_format, current_row):
        worksheet.merge_range(current_row, 0, current_row, 4, '----------- ABSORBANCE -----------', merge_format)
        worksheet.merge_range(current_row+ 1, 0, current_row + 1, 1, 'Exposure Time:', merge_format)
        worksheet.merge_range(current_row + 1, 2, current_row + 1, 3, str(self.__expTime), merge_format)
        worksheet.write(current_row + 1, 4, '(ms)')
        # worksheet.merge_range(current_row + 2, 0, current_row + 2, 1, 'Light Intensity:', merge_format)
        # worksheet.merge_range(current_row + 2, 2, current_row + 2, 3, str(self.__lightInt), merge_format)
        # worksheet.write(current_row + 2, 4, '%')
        worksheet.merge_range(current_row + 2, 0, current_row + 2, 4, '-----------------------------------------',
                              merge_format)
        return current_row + 4

    def get_dark(self, machine):
        machine.set_exposure_time(self.__expTime)
        machine.spec.scans_to_average(machine.settings[3])
        wavelengths, intensities = machine.get_spectra()
        # wavelengths = range(1, 1025)
        # intensities = range(1500, 2524)
        return wavelengths, intensities

    def start(self, machine):
        print 'TURN LED ON'
        machine.set_exposure_time(self.__expTime)
        machine.spec.scans_to_average(machine.settings[3])
        machine.turn_led_on(self.ledIndex)
        print 'LED ON'
        print 'GET SPECTRA'
        wavelengths, intensities = machine.get_spectra()
        print 'SPECTRA GOT'
        print 'TURN LED OFF'
        machine.turn_led_off(self.ledIndex)
        print 'LED OFF'
        # wavelengths = range(1, 1025)
        # intensities = range(1500, 2524)
        return wavelengths, intensities


