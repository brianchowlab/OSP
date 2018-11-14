from Protocol import *


class Kinetic(Protocol, object):
    def __init__(self, method, interval, duration, reps, label, plate, order):
        super(Kinetic, self).__init__(label, plate, order)
        self.order = order
        self.method = method
        self.interval = interval
        self.duration = duration
        self.reps = reps
        self.plate = plate
        self.label = label
        self.__protocols = []
        self.excel_length = 4

    def get_full_description(self):
        print "--- OVERALL DESCRIPTION ---"
        print "Label: " + self.label
        print "Plate #: " + str(self.plate)
        print "Order: " + str(self.order)
        print "- - - - - - - - - - - - - -"
        if self.method == 1:
            print "Method Type: " + 'Interval'
            print "Duration: " + str(self.duration) + " ms"
            print "Interval: " + str(self.interval) + " ms"
        elif self.method == 2:
            print "Method Type: " + 'Repeat'
            print 'Number of Repeats: ' + str(self.reps)

    def add_protocol(self, protocol):
        self.__protocols.append(protocol)

    def remove_protocol(self, protocol_index):
        self.__protocols.pop(protocol_index)

    def get_protocol_count(self):
        return len(self.__protocols)

    def get_protocol_brief_description(self, protocol_index):
        self.__protocols[protocol_index].get_brief_description()

    def get_protocol_full_description(self, protocol_index):
        self.__protocols[protocol_index].get_full_description()

    def get_protocol(self, protocol_index):
        return self.__protocols[protocol_index]

    def initialize_excel_section_start(self, worksheet, merge_format, header_format, current_row):
        worksheet.merge_range(current_row, 0, current_row, 4, '----------- Kinetic Start -----------', merge_format)
        if self.method == 1:
            worksheet.merge_range(current_row+ 1, 0, current_row + 1, 1, 'Duration', merge_format)
            worksheet.merge_range(current_row + 1, 2, current_row + 1, 3, self.duration, merge_format)
            worksheet.write(current_row + 1, 4, '(ms)')
            worksheet.merge_range(current_row+ 2, 0, current_row + 2, 1, 'Interval', merge_format)
            worksheet.merge_range(current_row + 2, 2, current_row + 2, 3, self.interval, merge_format)
            worksheet.write(current_row + 2, 4, '(ms)')
            worksheet.merge_range(current_row + 3, 0, current_row + 3, 4, '-----------------------------------------',
                              merge_format)
            return current_row + 5
        elif self.method == 2:
            worksheet.merge_range(current_row + 1, 0, current_row + 1, 1, 'Number of Repeats', merge_format)
            worksheet.merge_range(current_row + 1, 2, current_row + 1, 3, self.reps, merge_format)
            worksheet.merge_range(current_row + 2, 0, current_row + 2, 4, '-----------------------------------------',
                              merge_format)
            return current_row + 4

    @staticmethod
    def initialize_excel_section_stop(worksheet, merge_format, header_format, current_row):
        worksheet.merge_range(current_row, 0, current_row, 4, '----------- Kinetic Stop -----------', merge_format)
        worksheet.merge_range(current_row + 1, 0, current_row + 1, 4, '-----------------------------------------',
                              merge_format)
        return current_row + 3
