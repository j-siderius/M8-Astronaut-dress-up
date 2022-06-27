"""
This class takes care of retrieving the data from the .csv file and does the calculations with it
"""

import csv


class DatCalc:

    def __init__(self):
        "Insert stuff"

        '''Determines the current planet'''
        self.planet = "Earth"
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
        self.survival = []

        '''Intermediate for using data'''
        self.curData = []

        '''For the exact levels of conditions'''
        self.gravity = 1
        self.toxic = 0
        self.oxygen = 21
        self.temperature = 15
        self.gasGiant = "No"

        '''Calls functions for testing'''
        #self.setBodyParts()
        #self.dataConnect()
        #self.dataRelevant()
        #self.survivalCalc()
        #self.planetScoreCalc()

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
            pop = []
            for j in range(0, len(self.rows[i])):
                pop.append(self.rows[i][j])
            self.rows[i] = pop

    def dataRelevant(self, planet):
        """
        This function will determine which data is relevant.
        """

        self.planet = planet

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
        self.survival.clear()
        '''Calculates survivability and stores it in list'''
        self.survival.append(self.gravityCalc(float(self.curData[1])))
        self.survival.append(self.toxicityCalc(self.curData[2]))
        self.survival.append(self.oxygenCalc(self.curData[3]))
        self.survival.append(self.temperatureCalc(int(self.curData[4])))
        self.survival.append(self.gasGiantCalc(self.curData[5]))

        '''Determines total survival based on the calculations'''
        if False in self.survival:
            self.survivalBool = False
        else:
            self.survivalBool = True

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

    def setBodyParts(self, astronautArray):
        """
        Sets value of the bodyparts, based on what the user selected
        """

        if astronautArray[0] == 1:
            self.boots = "light"
        elif astronautArray[1] == 1:
            self.boots = "medium"
        elif astronautArray[2] == 1:
            self.boots = "heavy"

        # TODO: fix to current body parts
        if astronautArray[3] == 1:
            self.legs = "rocket"
        else:
            self.boots = "none"

        if astronautArray[4] == 1:
            self.torso = "cool"
        elif astronautArray[5] == 1:
            self.torso = "none"
        elif astronautArray[6] == 1:
            self.torso = "hot"

        if astronautArray[7] == 1:
            self.helmet = "gas"
        elif astronautArray[8] == 1:
            self.helmet = "gasoxygen"
        elif astronautArray[9] == 1:
            self.helmet = "oxygen"
        elif astronautArray[10] == 1:
            self.helmet = "none"


    def setPlanet(self, planetArray):
        '''
        Sets value of planet, based on what the user selected
        '''

        if planetArray[0] == 1:
            self.planet = "Mercury"
        elif planetArray[1] == 1:
            self.planet = "Venus"
        elif planetArray[2] == 1:
            self.planet = "Moon"
        elif planetArray[3] == 1:
            self.planet = "Mars"
        elif planetArray[4] == 1:
            self.planet = "Jupiter"
        elif planetArray[5] == 1:
            self.planet = "Saturn"
        elif planetArray[6] == 1:
            self.planet = "Uranus"
        elif planetArray[7] == 1:
            self.planet = "Neptune"


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

    def getSurvival(self):
        return self.survival, self.survivalBool

    def getPlanetData(self):
        return self.curData

    def returnDist(self):
        return self.curData[12]


    #TODO: make a function for the granular data (aka the output data changes after launching the astronaut)
