from Protocol import *


class Fluorescence(Protocol, object):
    def __init__(self, expTime, ledIndex, wavelength_led_1, wavelength_led_2,
                                    wavelength_led_3, label, plate, order):
        super(Fluorescence, self).__init__(label, plate, order)
        self.__expTime = expTime  # Integer
        # self.__lightInt = lightInt  # Integer
        self.__ledIndex = ledIndex  # String
        self.__wavelength = [wavelength_led_1, wavelength_led_2, wavelength_led_3] # List of Integers
        self.excel_length = 5

    def get_full_description(self):
        print "--- OVERALL DESCRIPTION ---"
        print "Label: " + self.label
        print "Plate #: " + str(self.plate)
        print "Order: " + str(self.order)
        print "- - - - - - - - - - - - - -"
        print "Exposure Time: " + str(self.__expTime) + " (ms)"
        # print "Light Intensity: " + str(self.__lightInt) + "%"
        print "LED: " + str(self.__ledIndex)
        print "Wavelength: " + str(self.__wavelength) + " nm"

    def get_exposure_time(self):
        return self.__expTime

    def get_led_index(self):
        return self.__ledIndex

    def get_wavelength(self):
        return self.__wavelength

    def set_exposure_time(self, time):
        self.__expTime = time

    def set_excitation_source(self, index, wavelength):
        self.__ledIndex = index
        self.__wavelength = wavelength

    def initialize_excel_section(self, worksheet, merge_format, header_format, current_row):
        worksheet.merge_range(current_row, 0, current_row, 4, '----------- FLUORESCENCE -----------', merge_format)
        worksheet.merge_range(current_row+ 1, 0, current_row + 1, 1, 'Exposure Time:', merge_format)
        worksheet.merge_range(current_row + 1, 2, current_row + 1, 3, str(self.__expTime), merge_format)
        worksheet.write(current_row + 1, 4, '(ms)')
        led_count = 2
        if self.__ledIndex[0] == '1':
            worksheet.merge_range(current_row + led_count, 0, current_row + led_count, 1, 'LED:', merge_format)
            worksheet.merge_range(current_row + led_count, 2, current_row + led_count, 3, str(self.__wavelength[0]), merge_format)
            worksheet.write(current_row + led_count, 4, 'nm')
            led_count += 1

        if self.__ledIndex[1] == '1':
            worksheet.merge_range(current_row + led_count, 0, current_row + led_count, 1, 'LED:', merge_format)
            worksheet.merge_range(current_row + led_count, 2, current_row + led_count, 3, str(self.__wavelength[1]), merge_format)
            worksheet.write(current_row + led_count, 4, 'nm')
            led_count += 1

        if self.__ledIndex[2] == '1':
            worksheet.merge_range(current_row + led_count, 0, current_row + led_count, 1, 'LED:', merge_format)
            worksheet.merge_range(current_row + led_count, 2, current_row + led_count, 3, str(self.__wavelength[2]), merge_format)
            worksheet.write(current_row + led_count, 4, 'nm')
            led_count += 1

        if self.__ledIndex[3] == '1':
            worksheet.merge_range(current_row + led_count, 0, current_row + led_count, 1, 'LED:', merge_format)
            worksheet.merge_range(current_row + led_count, 2, current_row + led_count, 3, 'FIBER', merge_format)
            led_count += 1
        worksheet.merge_range(current_row + led_count, 0, current_row + led_count, 4, '-----------------------------------------',
                              merge_format)
        self.excel_length = current_row + led_count + 1
        return self.excel_length

    def get_dark(self, machine):
        machine.set_exposure_time(self.__expTime)
        machine.spec.scans_to_average(machine.settings[3])
        wavelengths, intensities = machine.get_spectra()
        # wavelengths = range(1, 1025)
        # intensities = range(1500, 2524)
        return wavelengths, intensities

    def start(self, machine):
        machine.set_exposure_time(self.__expTime)
        machine.spec.scans_to_average(machine.settings[3])
        machine.turn_led_on(self.__ledIndex)
        wavelengths, intensities = machine.get_spectra()
        machine.turn_led_off(self.__ledIndex)
        # wavelengths = range(1, 1025)
        # intensities = range(1500, 2524)
        return wavelengths, intensities