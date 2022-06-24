"""
This class handles the serial connection between laptop and arduino
"""

import serial
import serial.tools.list_ports
import threading
import time


class Serial:

    def __init__(self, port=None, baudrate=9600):
        """
        Initializes the serial object
        :param port: serial port that the controller is connected to
        :param baudrate: communication baud rate for talking to the serial device
        """

        # if no port is specified, the program will automatically try to find and connect to a connected Arduino device
        if not port:
            device = self.getSerialPort()
            self.port = serial.Serial(device, baudrate)
        # if a port is specified, the program will connect to that
        else:
            self.port = serial.Serial(device, baudrate)

        # build a thread for the serial receiving function
        serialThread = threading.Thread(target=self.readSerial)
        serialThread.start()

    def getSerialPort(self):
        """
        This function will return the port/device of the first connected arduino
        :return: device of first connected arduino
        """
        # get all available ports
        ports = list(serial.tools.list_ports.comports())
        device = ""
        for p in ports:
            # look through all ports and find the one a with Arduino device
            if "Arduino" in str(p.manufacturer):
                print("Arduino found, connecting to port: ", p.device)
                device = p.device
                break
        if device == "":
            print("ERROR: no Arduino found")
            exit()
        else:
            return device

    def writeSerial(self, argument):
        """
        This function will send a message to arduino
        :param argument: the serial message to send
        """

        # convert the argument to the proper encoding
        arg = bytes(argument.encode())
        self.port.write(arg)

    def readSerial(self):
        """
        This function will check received messages from arduino
        """

        # this function runs within a thread, so we can introduce a infinite loop
        while True:
            # read all available from the serial port and print to serial
            # TODO: change handling of incoming data
            print(self.port.readline().decode())
            time.sleep(0.001)

    def messageQueue(self):
        """
        This function will contain the queue for messages
        """
        # TODO: implement queue system
