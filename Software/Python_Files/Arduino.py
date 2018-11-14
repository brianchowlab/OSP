import time
import warnings
import serial
import serial.tools.list_ports
import platform

class Arduino(object):
    def __init__(self, parent = None):
        if platform.system() == 'Windows': 
            ser_ports = [
                p.device
                for p in serial.tools.list_ports.comports()
                if 'Arduino' in p.description
            ]
        elif platform.system() == 'Darwin': 
            ser_ports = [
                p.device
                for p in serial.tools.list_ports.comports()
                if 'Arduino' in p.description
            ]
        elif platform.system() == 'Linux': 
            ser_ports = [
                p.device
                for p in serial.tools.list_ports.comports()
                if 'ACM' in p.description
            ]
        if not ser_ports:
            raise IOError("No ser found")
        else:
            self.ser = serial.Serial(ser_ports[0], 9600)
        if len(ser_ports) > 1:
            warnings.warn('Multiple sers found - using the first')
        if self.ser is None:
            print 'Device not found'

    def write(self, string):
        self.ser.write(string)

    def read(self):
        signal = self.ser.readline()
        return signal

    def close(self):
        self.ser.close()
