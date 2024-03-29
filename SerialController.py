"""
This class handles the serial connection between laptop and arduino
"""

import serial
import serial.tools.list_ports
import threading
import time


class Serial:

    def __init__(self, dataObj, port=None, baudrate=9600):
        """
        Initializes the serial object
        :param dataObj: dataCalculation object (to pass variables)
        :param port: serial port that the controller is connected to
        :param baudrate: communication baud rate for talking to the serial device
        """

        self.dataObj = dataObj

        # confirmation ckeck and queue for messages
        self.waitingForConfirmation = False
        self.confirmToken = ""
        self.messageBuffer = []
        self.previous_time = time.perf_counter()

        # to check whether the button has been pressed
        self.launched = False

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

        print("Write: " + argument)
        if not self.waitingForConfirmation:
            # send the message
            # convert the argument to the proper encoding
            arg = bytes(argument.encode())
            self.port.write(arg)
            self.confirmToken = str(arg[0])
            self.waitingForConfirmation = True
            print(argument)
        else:
            # still waiting for confirmation, wait with sending and add to buffer
            self.messageBuffer.append(argument)

    def readSerial(self):
        """
        This function will check received messages from arduino
        """

        # this function runs within a thread, so we can introduce a infinite loop
        while True:
            # read all available from the serial port and print to serial
            try:
                buffer = self.port.readline()
                print(buffer)
                buffer = buffer.decode()
                print("Incoming serial:", buffer)  # debugging
                self.decode(buffer)
            except UnicodeDecodeError:
                pass
            # time.sleep(0.001)  # debugging

            # check periodically if we have messages in the buffer still to send
            self.elapsed_time = time.perf_counter() - self.previous_time
            if self.elapsed_time > 1 / 5:
                self.previous_time = time.perf_counter()
                self.messageQueue()

    def decode(self, message):
        """
        Decodes incoming serial messages and call applicable functions in the data class
        :param  message: incoming serial message   
        """
        if "PA" in message:
            # planet array (8 planets)
            index = message.index("PA")+2
            planetArray = message[index:index+8]
            self.dataObj.setPlanet(planetArray)
        elif "AA" in message:
            # astronaut array (11 parts)
            index = message.index("AA")+2
            astronautArray = message[index:index+16]
            self.dataObj.setBodyParts(astronautArray)
        elif "L" in message:
            # launch confirmation
            index = message.index("L")+1
            launchConfirm = message[index:index+1]
            self.launched = True
            print("launchConfirm", launchConfirm)
        elif "C" in message:
            # message received confirmation
            if message[1] != self.con.firmToken:
                print("Confirmation receipt error: Confirmation does not match the sent function!")
            else:
                self.waitingForConfirmation = False

        elif "Initialized" in message:
            time.sleep(0.25)
            arg = bytes("F0".encode())
            self.port.write(arg)

        else:
            print("Serial message could not be decoded:", message)

    def encoder(self, function, data=None):
        """
        Encodes serial message to send to arduino
        :param  function: which type of message to send
        :param  data: data to include in the send
        """            
        if function == "planetData":
            # incoming data format:
            # ['Jupiter', '2.541', 'No', 'No', '-110', 'Yes', '0', '0', '0', '0', '90', '10', '10', '779']
            # Planet,G-force,Toxic,Oxygen,Surface Temperature,Gas Giant,CO2,N2,O2,CH4,H2,He,Surface pressure,Distance

            # outgoing data format:
            # G-force|Toxic|Oxygen|SurfaceTemperature|GasGiant|CO2|N2|O2|CH4|H2|He|SurfacePressure|Distance
            #     F| T|  O|     K| G|  E|   |   |   |   |   |     P|      D
            # 0.000| 0|  0|  -000| 0| 00| 00| 00| 00| 00| 00| 0.000|  0.000
            # example: F0.908T1O0K-195G1E0|0|0|2|83|15P1000D2867

            if data is not None and len(data) == 14:
                msg = 'D'
                msg += 'F' + str(data[1])  # g-force
                tox = 1 if str(data[2]) == "Yes" else 0
                msg += 'T' + str(tox)  # toxicity
                oxy = 1 if str(data[3]) == "Yes" else 0
                msg += 'O' + str(oxy)  # oxygen
                msg += 'K' + str(data[4])  # temperature
                gas = 1 if str(data[5]) == "Yes" else 0
                msg += 'G' + str(gas)  # gasgiant
                msg += 'E' + str(data[6]) + '|' + str(data[7]) + '|' + str(data[8]) + '|' + str(data[9]) + '|' + str(data[10]) + '|' + str(data[11])  # Elements: CO2|N2|O2|CH4|H2|He
                msg += 'P' + str(data[12])  # pressure
                msg += 'D' + str(data[13])  # distance
                # self.writeSerial(msg)

                arg = bytes(msg.encode())
                self.port.write(arg)
            else:
                print("data array is not correct!")

        elif function == "planetName":
            # incoming data is data array, name is pos 0
            # outgoing data format: N[name]
            if data is not None: #TODO: fix the planetName encoding
                msg = 'N' + str(data) + '\n'  # name
                # self.writeSerial(msg)

                arg = bytes(msg.encode())
                self.port.write(arg)
                print(arg)
            else:
                print("data array is not correct!")

        elif function == "astronautSurvival":
            # Granular data: an array of 4 variables. Only used once the astronaut has landed on the planet
            # first value = toxicity; 0 = no toxic, 1 = toxic
            # second value = oxygen; 0 = no oxygen, 1 = oxygen
            # third value = temperature; 0 = cold, 1 = normal, 2 is hot
            # fourth value = gas giant; 0 = no gas giant, 1 = gas giant
            # For example: [0, 1, 2, 0]

            if data is not None and len(data) == 4:
                msg = 'S'
                msg += str(data[0]) + str(data[1]) + str(data[2]) + str(data[3])
                # self.writeSerial(msg)

                arg = bytes(msg.encode())
                self.port.write(arg)
            else:
                print("data array is not correct!")

        elif function == "flowState":
            # sends current state
            if data is not None:  # and data.isnumeric()
                msg = 'F' + str(data)
                # self.writeSerial

                arg = bytes(msg.encode())
                self.port.write(arg)
                print(arg)

        elif function == "travelTime":
            # sends the travel time to the planet
            if data is not None:
                msg = 'T' + str(data)
                # self.writeSerial(msg)

                arg = bytes(msg.encode())
                self.port.write(arg)
                print(arg)

        elif function == "launchConfirm":
            if data is not None:
                msg = 'L' + str(data)
                # self.writeSerial(msg)

                arg = bytes(msg.encode())
                self.port.write(arg)

    def messageQueue(self):
        """
        This function will contain the queue for messages
        """
        # check if we still have messages waiting
        if not self.waitingForConfirmation and len(self.messageBuffer) > 0:
            # try to send next message in buffer if we are not waiting for confirmation anymore
            self.writeSerial(self.messageBuffer.pop(0))

    def getLaunched(self):
        return self.launched

    def setLaunched(self, launched):
        self.launched = launched
