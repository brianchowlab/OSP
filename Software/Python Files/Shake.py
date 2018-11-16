from Protocol import *

class Shake(Protocol, object):
    def __init__(self, label, plate, order):
        super(Shake, self).__init__(label, plate, order)
        self.excel_length = 4
    
    def get_full_description(self):
        print "--- OVERALL DESCRIPTION ---"
        print "Label: " + self.label
        print "Plate #: " + str(self.plate)
        print "Order: " + str(self.order)
        print "- - - - - - - - - - - - - -"

    def initialize_excel_section(self, worksheet, merge_format, header_format, current_row):
        worksheet.merge_range(current_row, 0, current_row, 4, '-----------------------------------------', merge_format)
        worksheet.merge_range(current_row + 1, 0, current_row + 1, 4, '---------------   SHAKE  ------------', merge_format)
        worksheet.merge_range(current_row + 2, 0, current_row + 2, 4, '-----------------------------------------',
                              merge_format)
        return current_row + 4

    def start(self, machine):
        print 'SHAKE '
        machine.shake()