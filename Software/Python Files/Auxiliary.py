from Protocol import *


class Auxiliary(Protocol, object):
    def __init__(self, aux_index, duration, label, plate, order):
        super(Auxiliary, self).__init__(label, plate, order)
        self.__duration = duration  # Integer
        self.__aux_index = aux_index
        self.excel_length = 3

    def get_full_description(self):
        print "--- OVERALL DESCRIPTION ---"
        print "Label: " + self.label
        print "Plate #: " + str(self.plate)
        print "Order: " + str(self.order)
        print "- - - - - - - - - - - - - -"
        print "Port #: " + str(self.__aux_index)
        print "Duration: " + str(self.__duration) + " (ms)"

    def get_aux_index(self):
        return self.__aux_index

    def get_duration(self):
        return self.__duration

    def set_duration(self, time):
        self.__duration = time

    def set_aux_index(self, index):
        self.__aux_index = index

    def start(self, machine, current_position):
        print self.__aux_index
        currentX = current_position[0:7]
        currentY = int(float(current_position[7:len(current_position)]))
        auxY = str(format(currentY + 316, '.2f'))
        aux_position = currentX + auxY
        print current_position
        print aux_position
        if self.__aux_index == 1:
            machine.move_plate(aux_position)
            machine.trigger_aux(self.__aux_index, self.__duration)
            machine.move_plate(current_position)
        elif self.__aux_index == 2:
            # machine.move_plate(aux_position)
            machine.trigger_aux(self.__aux_index, self.__duration)
            # machine.move_plate(current_position)
        elif self.__aux_index == 3:
            machine.move_plate(aux_position)
            machine.trigger_aux(self.__aux_index, self.__duration)
            machine.move_plate(current_position)
        elif self.__aux_index == 4:
            machine.move_plate(aux_position)
            machine.trigger_aux(self.__aux_index, self.__duration)
            machine.move_plate(current_position)