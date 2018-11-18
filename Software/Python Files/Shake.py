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

    def start(self, machine):
        print 'SHAKE '
        machine.shake()