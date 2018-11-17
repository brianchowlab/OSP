class Protocol:
    def __init__(self, label, plate, order):
        self.label = label  # String structure representing protocol type (Absorbance, Florescence, etc.)
        self.plate = plate  # Integer value pinpointing to which plate the protocol belongs to
        self.order = order  # Integer value pinpointing where in the list of protocols the current protocol is located

    def get_brief_description(self):
        print "--- DESCRIPTION ---"
        print "Label: " + self.label
        print "Plate #: " + str(self.plate)
        print "Order: " + str(self.order)

        return self.label, self.plate, self.order

