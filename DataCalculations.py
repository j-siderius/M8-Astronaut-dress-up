"""
This class takes care of retrieving the data from the .csv file and does the calculations with it
"""

import csv


class DatCalc:

    def __init__(self):
        "Insert stuff"

        '''Determines the current planet'''
        self.planet = "Mars"
        '''Create empty gear variables'''
        self.boots = "none"
        self.legs = "none"
        self.torso = "none"
        self.helmet = "none"

        '''Create (naked) human body limits'''
        self.gravityLimitUpper = 1.15
        self.gravityLimitLower = 0.85
        self.temperatureLimitUpper = 34
        self.temperatureLimitLower = 4

        '''Boolean to determine survival'''
        self.survivalBool = False

        '''Intermediate for using data'''
        self.curData = []

        '''For the exact levels of conditions'''
        self.gravity = 1
        self.toxic = 0
        self.oxygen = 21
        self.temperature = 15
        self.gasGiant = "No"

        '''Calls functions for testing'''
        self.gearScoreCalc()
        self.dataConnect()
        self.dataRelevant()
        self.survivalCalc()
        self.planetScoreCalc()

    def dataConnect(self):
        """
        This function will connect to the .csv file and store the data in a list.
        """
        '''Store data from .csv file in list'''
        file = open('Planet Data.csv')
        type(file)
        csvreader = csv.reader(file)
        self.rows = []
        for row in csvreader:
            self.rows.append(row)
        file.close()

        '''Split list so that variables can be used'''
        for i in range(0, len(self.rows)):
            pop = self.rows[i].pop(0)
            self.rows[i] = pop.split(';')

    def dataRelevant(self):
        """
        This function will determine which data is relevant.
        """
        for i in range(0, len(self.rows)):
            if self.planet in self.rows[i]:
                self.curData = self.rows[i]

    def survivalCalc(self):
        """
        This function calculates whether the astronaut will survive or not and in which areas
        """

        '''
        G-force = 1
        Toxic = 2
        Oxygen = 3
        Surface Temperature = 4
        Gas Giant = 5
        '''

        '''Calculates survivability and stores it in list'''
        survival = []
        survival.append(self.gravityCalc(float(self.curData[1])))
        survival.append(self.toxicityCalc(self.curData[2]))
        survival.append(self.oxygenCalc(self.curData[3]))
        survival.append(self.temperatureCalc(int(self.curData[4])))
        survival.append(self.gasGiantCalc(self.curData[5]))

        '''Prints survivability for testing purposes'''
        print(self.planet)
        print('gravity ' + str(self.gravityCalc(float(self.curData[1]))))
        print('toxicity ' + str(self.toxicityCalc(self.curData[2])))
        print('oxygen ' + str(self.oxygenCalc(self.curData[3])))
        print('temperature ' + str(self.temperatureCalc(int(self.curData[4]))))
        print('gasgiant ' + str(self.gasGiantCalc(self.curData[5])))

        '''Determines total survival based on the calculations'''
        if False in survival:
            self.survivalBool = False
        else:
            self.survivalBool = True

        print('survival ' + str(self.survivalBool))

    def gravityCalc(self, data):
        """
        Calculates the gravity survivability
        """
        if self.gravityLimitUpper > data > self.gravityLimitLower and self.boots == "none":
            return True
        elif data > self.gravityLimitUpper and self.boots == "light":
            return True
        elif data < self.gravityLimitLower and self.boots == "heavy":
            return True
        else:
            return False

    def toxicityCalc(self, data):
        """
        Calculates the toxicity survivability
        """
        if data == "No":
            return True
        elif self.helmet == "gas" or self.helmet == "gasoxygen":
            return True
        else:
            return False

    def oxygenCalc(self, data):
        """
        Calculates the oxygen survivability
        """
        if data == "Yes":
            return True
        elif self.helmet == "oxygen" or self.helmet == "gasoxygen":
            return True
        else:
            return False

    def temperatureCalc(self, data):
        """
        Calculates the temperature survivability
        """
        if self.temperatureLimitUpper > data > self.temperatureLimitLower and self.torso == "none":
            return True
        elif data > self.temperatureLimitUpper and self.torso == "cool":
            return True
        elif data < self.temperatureLimitLower and self.torso == "hot":
            return True
        else:
            return False

    def gasGiantCalc(self, data):
        """
        Calculates the gas giant survivability
        """
        if data == "No":
            return True
        elif self.legs == "rocket":
            return True
        else:
            return False

    def gearScoreCalc(self):
        """
        This function calculates the properties of the gear from the astraut to pass to survivalcalc
        """

        self.boots = "none"
        '''
        heavy, light, none
        '''
        self.legs = "rocket"
        '''
        rocket, none
        '''
        self.torso = "hot"
        '''
        cool, hot, none
        '''
        self.helmet = "oxygen"
        '''
        gas, gasoxygen, oxygen, none
        '''

    def planetScoreCalc(self):
        """
        This function calculates the values for physicalizing the planet data and passing to survivalcalc
        """

        '''
        Gravity = 1
        Toxic = 6
        Oxygen = 7
        Surface Temperature = 4
        Gas Giant = 5
        '''

        '''Puts data in the variables'''
        self.gravity = self.curData[1]
        self.toxic = self.curData[6]
        self.oxygen = self.curData[7]
        self.temperature = self.curData[4]
        self.gasGiant = self.curData[5]

        print('')
        print('Accurate data:')
        print('gravity ' + self.gravity)
        print('toxicity ' + self.toxic)
        print('oxygen ' + self.oxygen)
        print('temperature ' + self.temperature)
        print('gasgiant ' + self.gasGiant)


connect = DatCalc()
