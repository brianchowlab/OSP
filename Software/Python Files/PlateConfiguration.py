class PlateConfiguration(object):
    def __init__(self, well_numb, order):
        self.well_numb = well_numb
        self.order = order
        self.__protocols = []
        self.__well_status = []
        self.__well_names = []
        self.initialize_wells()

    def add_protocol(self, protocol):
        self.__protocols.append(protocol)

    def get_protocol_count(self):
        return len(self.__protocols)

    def initialize_wells(self):
        rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        if self.well_numb == 24:
            for row in rows[0:4]:
                for column in range(0, 6):
                    self.__well_names.append(row + str(column+1))
                    self.__well_status.append('OFF')
        elif self.well_numb == 96:
            for row in rows[0:8]:
                for column in range(0, 12):
                    self.__well_names.append(row + str(column+1))
                    self.__well_status.append('OFF')

    def get_protocol_brief_description(self, protocol_index):
        self.__protocols[protocol_index].get_brief_description()

    def get_protocol_full_description(self, protocol_index):
        self.__protocols[protocol_index].get_full_description()

    def get_protocol(self, protocol_index):
        return self.__protocols[protocol_index]

    def remove_protocol(self, protocol_index):
        del self.__protocols[protocol_index]

    def get_selected_wells(self):
        if not self.__well_status:
            well_string = 'NONE'
            well_label = []
            well_index = []
        else:
            well_string = ''
            well_index = []
            well_label = []
            for well in range(0, len(self.__well_status)):
                if self.__well_status[well] == 'ON':
                    well_string = well_string + self.__well_names[well] + ', '
                    well_label.append(self.__well_names[well])
                    well_index.append(well)
        # print 'Selected Wells: '
        # print well_string
        return well_string, well_label, well_index

    def get_well_status(self):
        return self.__well_status

    def clear_wells(self):
        self.__well_status = []
        self.__well_names = []

    def select_all_wells(self):
        for i in range(0, len(self.__well_status)):
            self.__well_status[i] = 'ON'

    def select_wells(self, well_list):
        if not self.__well_status:
            self.initialize_wells()
        for well in well_list:
            self.__well_status[well] = 'ON'