from Arduino import *
import seabreeze.spectrometers as sb
import numpy as np
import pickle

class Machine(object):
    def __init__(self, saved_setting_list):
        self.plate_list = []
        self.settings = saved_setting_list
        self.initialize_arduino()
        self.initialize_spec()
        self.positions24well = []
        self.positions96well = []
        self.arduinocmd = ''
        self.run = 0

    def initialize_arduino(self):
        self.arduino = Arduino()
        print 'Initialized Arduino'

    def initialize_spec(self):
        self.spec = sb.Spectrometer.from_serial_number()
        self.spec.integration_time_micros(1000)
        self.spec.scans_to_average(self.settings[3])
        print 'Initialized Spec'

    def move_plate(self, position_string):
        self.arduinocmd = self.arduinocmd + 'M'
        self.arduinocmd = self.arduinocmd + position_string + ';'
        self.arduino.write(self.arduinocmd)
        self.run = 1
        while self.run == 1:
            signal = self.arduino.read()
            print str(signal)
            if str(signal) == 'done\r\n':
                self.run = 0
        self.arduinocmd = ''

    def turn_led_on(self, led_index):
        self.arduinocmd = ''
        self.arduinocmd = self.arduinocmd + 'L'
        self.arduinocmd = self.arduinocmd + str(led_index) + ';'
        self.arduino.write(self.arduinocmd)
        self.run = 1
        while self.run == 1:
            signal = self.arduino.read()
            print str(signal)

            if str(signal) == 'done\r\n':
                self.run = 0
        self.arduinocmd = ''

    def turn_led_off(self, led_index):
        self.arduinocmd = self.arduinocmd + 'L'
        self.arduinocmd = self.arduinocmd + str(led_index) + ';'
        self.arduino.write(self.arduinocmd)
        self.run = 1
        while self.run == 1:
            signal = self.arduino.read()
            print str(signal)

            if str(signal) == 'done\r\n':
                self.run = 0
        self.arduinocmd = ''

    def trigger_aux(self, aux_index, duration):
        self.arduinocmd = self.arduinocmd + 'A'
        self.arduinocmd = self.arduinocmd + str(aux_index) + str(duration) + ';'
        self.arduino.write(self.arduinocmd)
        self.run = 1
        while self.run == 1:
            signal = self.arduino.read()
            print str(signal)

            if str(signal) == 'done\r\n':
                self.run = 0
        self.arduinocmd = ''

    def set_exposure_time(self, exp_time):
        corrected_exp_time = exp_time*1000
        self.spec.integration_time_micros(corrected_exp_time)

    def set_scans_to_avg(self, scans_to_avg):
        self.spec.scans_to_average(scans_to_avg)

    def set_boxcar_width(self, width):
        self.spec.boxcar_width(width)

    def get_spectra(self):
        return self.spec.wavelengths(), self.spec.intensities()

    def calibrate(self, plate_type):
        #  Run calibration step to find plate boundaries
        protocol_running = 1
        self.arduino.write('CF'+str(plate_type)+';')
        time.sleep(10)
        while protocol_running == 1:
            signal = self.arduino.read()
            if len(str(signal).strip().split(';')) > 1:
                if str(signal).strip().split(';')[0].isdigit():
                    splitCorr = signal.strip().split(';')
                    if plate_type == 1:
                        dpx = round(int(splitCorr[0]), -1)
                        dpy = round(int(splitCorr[1]), -1)
                    elif plate_type == 2:
                        dpx = int(splitCorr[0])
                        dpy = int(splitCorr[1])
                    topPos = int(splitCorr[2])
                    bottomPos = int(splitCorr[3])
                    leftPos = int(splitCorr[4])
                    rightPos = int(splitCorr[5])
                    protocol_running = 0

        print 'TOP: ' + str(topPos)
        print 'BOTTOM: ' + str(bottomPos)
        print 'LEFT: ' + str(leftPos)
        print 'RIGHT: ' + str(rightPos)
        print 'DPX: ' + str(dpx)
        print 'DPY: ' + str(dpy)

        if plate_type == 1:
            raw_well_layout_x = np.zeros((4, 6))
            raw_well_layout_y = np.zeros((4, 6))
            raw_well_layout_x[3][0] = leftPos
            raw_well_layout_y[3][0] = bottomPos
            for row in range(3, -1, -1):
                for col in range(0, 6):
                    raw_well_layout_y[row][col] = raw_well_layout_y[3][0] + dpy*((row-3)*-1)
                    raw_well_layout_x[row][col] = raw_well_layout_x[3][0] + dpx*col

            well_layout_1_x = np.zeros((4, 6))
            well_layout_1_y = np.zeros((4, 6))
            well_layout_2_x = np.zeros((4, 6))
            well_layout_2_y = np.zeros((4, 6))
            well_layout_3_x = np.zeros((4, 6))
            well_layout_3_y = np.zeros((4, 6))
            well_layout_final_x = np.zeros((4, 6))
            well_layout_final_y = np.zeros((4, 6))

            #  Run calibration to tune LEFT, BOTTOM corner well
            protocol_running = 1
            # print 'CT'+str(int(raw_well_layout_x[3][0]))+str(int(raw_well_layout_y[3][0]))+';'
            self.arduino.write('CT'+str(int(raw_well_layout_x[3][0]))+str(int(raw_well_layout_y[3][0]))+';')
            time.sleep(10)
            while protocol_running == 1:
                signal = self.arduino.read()
                if len(str(signal).strip().split(';')) > 1:
                    if str(signal).strip().split(';')[0].isdigit():
                        splitCorr = str(signal).strip().split(';')
                        well_layout_1_x[3][0] = int(splitCorr[0])
                        well_layout_1_y[3][0] = int(splitCorr[1])
                        for row in range(3, -1, -1):
                            for col in range(0, 6):
                                well_layout_1_y[row][col] = well_layout_1_y[3][0] + dpy * ((row - 3) * -1)
                                well_layout_1_x[row][col] = well_layout_1_x[3][0] + dpx * col
                        protocol_running = 0
            time.sleep(3)
        #
        #     #  Run calibration to tune WELL #2
            protocol_running = 1
            self.arduino.write('CT'+str(int(raw_well_layout_x[2][4]))+str(int(raw_well_layout_y[2][4]))+';')
            time.sleep(10)
            while protocol_running == 1:
                signal = self.arduino.read()
                if len(str(signal).strip().split(';')) > 1:
                    if str(signal).strip().split(';')[0].isdigit():
                        splitCorr = str(signal).strip().split(';')
                        well_layout_2_x[2][4] = int(splitCorr[0])
                        well_layout_2_y[2][4] = int(splitCorr[1])
                        for row in range(2, -1, -1):
                            for col in range(4, 6):
                                well_layout_2_y[row][col] = well_layout_2_y[2][4] + dpy * ((row - 2) * -1)
                                well_layout_2_x[row][col] = well_layout_2_x[2][4] + dpx * (col - 4)
                            for col in range(0, 4):
                                well_layout_2_y[row][col] = well_layout_2_y[2][4] + dpy * ((row - 2) * -1)
                                well_layout_2_x[row][col] = well_layout_2_x[2][4] - dpx * ((col - 4) * -1)
                        for row in range(2, 4):
                            for col in range(4, 6):
                                well_layout_2_y[row][col] = well_layout_2_y[2][4] - dpy * (row - 2)
                                well_layout_2_x[row][col] = well_layout_2_x[2][4] + dpx * (col - 4)
                            for col in range(0, 4):
                                well_layout_2_y[row][col] = well_layout_2_y[2][4] - dpy * (row - 2)
                                well_layout_2_x[row][col] = well_layout_2_x[2][4] - dpx * ((col - 4) * -1)
                        protocol_running = 0
        #
        #     #  Run calibration to tune WELL #3
            protocol_running = 1
            self.arduino.write('CT'+str(int(raw_well_layout_x[1][1]))+str(int(raw_well_layout_y[1][1]))+';')
            time.sleep(10)
            while protocol_running == 1:
                signal = self.arduino.read()
                if len(str(signal).strip().split(';')) > 1:
                    if str(signal).strip().split(';')[0].isdigit():
                        splitCorr = str(signal).strip().split(';')
                        well_layout_3_x[1][1] = int(splitCorr[0])
                        well_layout_3_y[1][1] = int(splitCorr[1])
                        for row in range(1, -1, -1):
                            for col in range(1, 6):
                                well_layout_3_y[row][col] = well_layout_3_y[1][1] + dpy * ((row - 1) * -1)
                                well_layout_3_x[row][col] = well_layout_3_x[1][1] + dpx * (col - 1)
                                well_layout_3_y[row][col] = well_layout_3_y[1][1] + dpy * ((row - 1) * -1)
                                well_layout_3_x[row][col] = well_layout_3_x[1][1] - dpx * ((col - 1) * -1)
                        for row in range(1, 4):
                            for col in range(1, 6):
                                well_layout_3_y[row][col] = well_layout_3_y[1][1] - dpy * (row - 1)
                                well_layout_3_x[row][col] = well_layout_3_x[1][1] + dpx * (col - 1)
                            for col in range(0, 1):
                                well_layout_3_y[row][col] = well_layout_3_y[1][1] - dpy * (row - 1)
                                well_layout_3_x[row][col] = well_layout_3_x[1][1] - dpx * ((col - 1) * -1)
                        protocol_running = 0
        #
            well_layout_final_x = (well_layout_1_x + well_layout_2_x + well_layout_3_x)/3.0
            well_layout_final_y = (well_layout_1_y + well_layout_2_y + well_layout_3_y)/3.0
            position_format = np.zeros((24, 2))
            well_count = -1
            for row in range(0, 4):
                for col in range(0, 6):
                    well_count += 1
                    position_format[well_count][0] = well_layout_final_x[row][col]
                    position_format[well_count][1] = well_layout_final_y[row][col]
            with open('calibration24Wells', 'wb') as f:
                print position_format
                pickle.dump(position_format, f)

        elif plate_type == 2:
            raw_well_layout_x = np.zeros((8, 12))
            raw_well_layout_y = np.zeros((8, 12))
            raw_well_layout_x[7][0] = leftPos
            raw_well_layout_y[7][0] = bottomPos
            for row in range(7, -1, -1):
                for col in range(0, 12):
                    raw_well_layout_y[row][col] = raw_well_layout_y[7][0] + dpy*((row-7)*-1)
                    raw_well_layout_x[row][col] = raw_well_layout_x[7][0] + dpx*col

            well_layout_1_x = np.zeros((8, 12))
            well_layout_1_y = np.zeros((8, 12))
            well_layout_2_x = np.zeros((8, 12))
            well_layout_2_y = np.zeros((8, 12))
            well_layout_3_x = np.zeros((8, 12))
            well_layout_3_y = np.zeros((8, 12))
            well_layout_final_x = np.zeros((8, 12))
            well_layout_final_y = np.zeros((8, 12))

            #  Run calibration to tune LEFT, BOTTOM corner well
            protocol_running = 1
            self.arduino.write('CT'+str(int(raw_well_layout_x[7][0]))+str(int(raw_well_layout_y[7][0]))+';')
            time.sleep(10)
            while protocol_running == 1:
                signal = self.arduino.read()
                if len(str(signal).strip().split(';')) > 1:
                    if str(signal).strip().split(';')[0].isdigit():
                        splitCorr = str(signal).strip().split(';')
                        well_layout_1_x[7][0] = int(splitCorr[0])
                        well_layout_1_y[7][0] = int(splitCorr[1])
                        for row in range(7, -1, -1):
                            for col in range(0, 12):
                                well_layout_1_y[row][col] = well_layout_1_y[7][0] + dpy * ((row - 7) * -1)
                                well_layout_1_x[row][col] = well_layout_1_x[7][0] + dpx * col
                        protocol_running = 0

            #  Run calibration to tune WELL #2
            protocol_running = 1
            self.arduino.write('CT'+str(int(raw_well_layout_x[6][9]))+str(int(raw_well_layout_y[6][9]))+';')
            time.sleep(10)
            while protocol_running == 1:
                signal = self.arduino.read()
                if len(str(signal).strip().split(';')) > 1:
                    if str(signal).strip().split(';')[0].isdigit():
                        splitCorr = str(signal).strip().split(';')
                        well_layout_2_x[6][9] = int(splitCorr[0])
                        well_layout_2_y[6][9]  = int(splitCorr[1])
                        for row in range(6, -1, -1):
                            for col in range(9, 12):
                                well_layout_2_y[row][col] = well_layout_2_y[6][9]  + dpy * ((row - 6) * -1)
                                well_layout_2_x[row][col] = well_layout_2_x[6][9]  + dpx * (col - 9)
                            for col in range(0, 9):
                                well_layout_2_y[row][col] = well_layout_2_y[6][9]  + dpy * ((row - 6) * -1)
                                well_layout_2_x[row][col] = well_layout_2_x[6][9]  - dpx * ((col - 9) * -1)
                        for row in range(6, 8):
                            for col in range(9, 12):
                                well_layout_2_y[row][col] = well_layout_2_y[6][9]  - dpy * (row - 6)
                                well_layout_2_x[row][col] = well_layout_2_x[6][9]  + dpx * (col - 9)
                            for col in range(0, 12):
                                well_layout_2_y[row][col] = well_layout_2_y[6][9]  - dpy * (row - 6)
                                well_layout_2_x[row][col] = well_layout_2_x[6][9]  - dpx * ((col - 9) * -1)
                        protocol_running = 0

            #  Run calibration to tune WELL #3
            protocol_running = 1
            self.arduino.write('CT'+str(int(raw_well_layout_x[1][1]))+str(int(raw_well_layout_y[1][1]))+';')
            time.sleep(10)
            while protocol_running == 1:
                signal = self.arduino.read()
                if len(str(signal).strip().split(';')) > 1:
                    if str(signal).strip().split(';')[0].isdigit():
                        splitCorr = str(signal).strip().split(';')
                        well_layout_3_x[1][1] = int(splitCorr[0])
                        well_layout_3_y[1][1] = int(splitCorr[1])
                        for row in range(1, -1, -1):
                            for col in range(1, 12):
                                well_layout_3_y[row][col] = well_layout_3_y[1][1] + dpy * ((row - 1) * -1)
                                well_layout_3_x[row][col] = well_layout_3_x[1][1] + dpx * (col - 1)
                            for col in range(0, 1):
                                well_layout_3_y[row][col] = well_layout_3_y[1][1] + dpy * ((row - 1) * -1)
                                well_layout_3_x[row][col] = well_layout_3_x[1][1] - dpx * ((col - 1) * -1)
                        for row in range(1, 8):
                            for col in range(1, 12):
                                well_layout_3_y[row][col] = well_layout_3_y[1][1] - dpy * (row - 1)
                                well_layout_3_x[row][col] = well_layout_3_x[1][1] + dpx * (col - 1)
                            for col in range(0, 1):
                                well_layout_3_y[row][col] = well_layout_3_y[1][1] - dpy * (row - 1)
                                well_layout_3_x[row][col] = well_layout_3_x[1][1] - dpx * ((col - 1) * -1)
                        protocol_running = 0

            well_layout_final_x = (well_layout_1_x + well_layout_2_x + well_layout_3_x)/3.0
            well_layout_final_y = (well_layout_1_y + well_layout_2_y + well_layout_3_y)/3.0
            position_format = np.zeros((96, 2))
            well_count = -1
            for row in range(0, 8):
                for col in range(0, 12):
                    well_count += 1
                    position_format[well_count][0] = well_layout_final_x[row][col]
                    position_format[well_count][1] = well_layout_final_y[row][col]
            with open('System Settings/calibration96Wells', 'wb') as f:
                pickle.dump(position_format, f)


    def start_program(self, plate_list, worksheet, workbook, merge_format, header_format, positions24, positions96):
        print 'Machine start'
        current_row = 5  # 5 rows below initialization text
        plate_index = []
        for plate_numb in range(0, len(plate_list)):
            current_row += 2  # Every new plate configuration add 5 rows to the current row
            worksheet.merge_range(current_row, 0, current_row, 4, '-------------------- Plate Configuration #' +
                                  str(plate_numb+1) + ' --------------------', merge_format)
            plate = plate_list[plate_numb]
            numb_of_protocols = plate.get_protocol_count()
            selected_well_string, selected_well_labels, selected_well_index = plate.get_selected_wells()

            print 'Machine selected wells'
            if plate.well_numb == 24:
                motor_positions = positions24
                print motor_positions
            elif plate.well_numb == 96:
                motor_positions = positions96

            current_row += 1
            self.move_plate('1300.001300.00')
            for w in range(0, len(selected_well_index)):
                print 'Machine protocol prep'
                if plate.well_numb == 24:
                    position = str(motor_positions[selected_well_index[w]][0]) + '0' \
                               + str(motor_positions[selected_well_index[w]][1])+'0'
                elif plate.well_numb == 96:
                    position = str(format(motor_positions[selected_well_index[w]][0], '.2f')) + \
                               str(format(motor_positions[selected_well_index[w]][1], '.2f'))
                print 'M' + position + ';'
                self.move_plate(position)
                if w != 0:
                    current_row = plate_index[plate_numb]
                else:
                    current_row += 1
                for p in range(0, numb_of_protocols):
                    protocol = plate.get_protocol(p)
                    if protocol.label != 'Kinetic':
                        if w == 0:
                            if protocol.label != 'Auxiliary':
                                current_row = protocol.initialize_excel_section(worksheet, merge_format, header_format, current_row)
                                current_row += 1
                                print 'GETTING DARK'
                                wavelengths, intensities = protocol.get_dark(self)
                                worksheet.write(current_row, 0, 'Wavelengths', header_format)
                                for c in range(0, len(wavelengths)):
                                    worksheet.write(current_row, c + 1, wavelengths[c], header_format)
                                current_row += 1
                                worksheet.write(current_row, 0, 'Dark', header_format)
                                for i in range(0, len(intensities)):
                                    worksheet.write(current_row, i + 1, intensities[i])
                                current_row += 1
                            print 'PROTOCOL START'
                            if protocol.label == 'Auxiliary':
                                protocol.start(self, position)
                            else:
                                wavelengths, intensities = protocol.start(self)
                            print 'PROTOCOL DONE'
                            worksheet.write(current_row, 0, selected_well_labels[w], header_format)
                            if protocol.label != 'Auxiliary':
                                for i in range(0, len(intensities)):
                                    worksheet.write(current_row, i + 1, intensities[i])
                                if p == 0:
                                    plate_index.append(current_row)
                                current_row += len(selected_well_index) + 3
                        else:
                            if p != 0:
                                current_row += len(selected_well_index) + 3 + protocol.excel_length + 3
                            else:
                                current_row += w
                            print 'PROTOCOL START'
                            if protocol.label == 'Auxiliary':
                                protocol.start(self, position)
                                print 'PROTOCOL DONE'
                            else:
                                wavelengths, intensities = protocol.start(self)
                                print 'PROTOCOL DONE'
                                worksheet.write(current_row, 0, selected_well_labels[w], header_format)
                                for i in range(0, len(intensities)):
                                    worksheet.write(current_row, i + 1, intensities[i])
                    else:
                        if protocol.label != 'Auxiliary':
                            current_row = protocol.initialize_excel_section_start(worksheet, merge_format, header_format,
                                                                            current_row)
                            current_row += 1
                        numb_of_kinetic_protocols = protocol.get_protocol_count()
                        interval = (protocol.interval)/1000.0
                        duration = (protocol.duration)/1000.0
                        method = protocol.method
                        reps = protocol.reps

                        if method == 1:
                            start_time = time.time()
                            kinetic_on = 1
                            interval_on = 1
                            while kinetic_on == 1:
                                elapsed_time = time.time()-start_time
                                if elapsed_time < duration:
                                    interval_start = time.time()
                                    for kp in range(0, numb_of_kinetic_protocols):
                                        kinetic_protocol = protocol.get_protocol(kp)
                                        if w == 0:
                                            current_row = kinetic_protocol.initialize_excel_section(worksheet, merge_format,
                                                                                            header_format, current_row)
                                            current_row += 1
                                            print 'GETTING DARK'
                                            wavelengths, intensities = kinetic_protocol.get_dark(self)
                                            worksheet.write(current_row, 0, 'Wavelengths', header_format)
                                            for c in range(0, len(wavelengths)):
                                                worksheet.write(current_row, c + 1, wavelengths[c], header_format)
                                            current_row += 1
                                            worksheet.write(current_row, 0, 'Dark', header_format)
                                            for i in range(0, len(intensities)):
                                                worksheet.write(current_row, i + 1, intensities[i])
                                            current_row += 1
                                            print 'PROTOCOL START'
                                            if protocol.label == 'Auxiliary':
                                                wavelengths, intensities = kinetic_protocol.start(self, position)
                                            else:
                                                wavelengths, intensities = kinetic_protocol.start(self)
                                            print 'PROTOCOL DONE'
                                            worksheet.write(current_row, 0, selected_well_labels[w], header_format)
                                            for i in range(0, len(intensities)):
                                                worksheet.write(current_row, i + 1, intensities[i])
                                            if p == 0:
                                                plate_index.append(current_row)
                                            current_row += len(selected_well_index) + 3
                                        else:
                                            if p != 0:
                                                current_row += len(selected_well_index) + 3 + protocol.excel_length + 3
                                            else:
                                                current_row += w
                                            print 'PROTOCOL START'
                                            if protocol.label == 'Auxiliary':
                                                wavelengths, intensities = kinetic_protocol.start(self, position)
                                            else:
                                                wavelengths, intensities = kinetic_protocol.start(self)
                                            print 'PROTOCOL DONE'
                                            worksheet.write(current_row, 0, selected_well_labels[w], header_format)
                                            for i in range(0, len(intensities)):
                                                worksheet.write(current_row, i + 1, intensities[i])
                                        interval_on = 1
                                    while interval_on == 1:
                                        interval_elapsed_time = time.time()-interval_start
                                        if interval_elapsed_time >= interval:
                                            interval_on = 0
                                else:
                                    kinetic_on = 0
                            current_row = protocol.initialize_excel_section_stop(worksheet, merge_format, header_format,
                                                                                 current_row)
                            current_row += 1

                        elif method == 2:
                            for r in range(0, reps):
                                for kp in range(0, numb_of_kinetic_protocols):
                                    kinetic_protocol = protocol.get_protocol(kp)
                                    if w == 0:
                                        current_row = kinetic_protocol.initialize_excel_section(worksheet, merge_format,
                                                                                        header_format, current_row)
                                        current_row += 1
                                        print 'GETTING DARK'
                                        wavelengths, intensities = kinetic_protocol.get_dark(self)
                                        worksheet.write(current_row, 0, 'Wavelengths', header_format)
                                        for c in range(0, len(wavelengths)):
                                            worksheet.write(current_row, c + 1, wavelengths[c], header_format)
                                        current_row += 1
                                        worksheet.write(current_row, 0, 'Dark', header_format)
                                        for i in range(0, len(intensities)):
                                            worksheet.write(current_row, i + 1, intensities[i])
                                        current_row += 1
                                        print 'PROTOCOL START'
                                        if protocol.label == 'Auxiliary':
                                            wavelengths, intensities = kinetic_protocol.start(self, position)
                                        else:
                                            wavelengths, intensities = kinetic_protocol.start(self)
                                        print 'PROTOCOL DONE'
                                        worksheet.write(current_row, 0, selected_well_labels[w], header_format)
                                        for i in range(0, len(intensities)):
                                            worksheet.write(current_row, i + 1, intensities[i])
                                        if p == 0:
                                            plate_index.append(current_row)
                                        current_row += len(selected_well_index) + 3
                                    else:
                                        if p != 0:
                                            current_row += len(selected_well_index) + 3 + protocol.excel_length + 3
                                        else:
                                            current_row += w
                                        print 'PROTOCOL START'
                                        if protocol.label == 'Auxiliary':
                                            wavelengths, intensities = kinetic_protocol.start(self, position)
                                        else:
                                            wavelengths, intensities = kinetic_protocol.start(self)
                                        print 'PROTOCOL DONE'
                                        worksheet.write(current_row, 0, selected_well_labels[w], header_format)
                                        for i in range(0, len(intensities)):
                                            worksheet.write(current_row, i + 1, intensities[i])
                            current_row = protocol.initialize_excel_section_stop(worksheet, merge_format,
                                                                                  header_format,
                                                                                  current_row)
                            current_row += 1

        workbook.close()

    def close(self):
        self.spec.close()
        self.arduino.close()



