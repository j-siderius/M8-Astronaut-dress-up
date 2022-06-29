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
        self.granular = []

        self.bodyError = []
        self.error = []

        self.frameRate = 60
        self.travelDuration = 10

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
        self.granular.clear()
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
            self.granular.append(0)
            return True
        elif self.helmet == "gas":
            self.granular.append(0)
            return True
        else:
            self.granular.append(1)
            return False

    def oxygenCalc(self, data):
        """
        Calculates the oxygen survivability
        """
        if data == "Yes":
            self.granular.append(1)
            return True
        elif self.helmet == "oxygen" or self.helmet == "gas":
            self.granular.append(1)
            return True
        else:
            self.granular.append(0)
            return False

    def temperatureCalc(self, data):
        """
        Calculates the temperature survivability
        """
        if self.temperatureLimitUpper > data > self.temperatureLimitLower and self.torso == "regular":
            self.granular.append(1)
            return True
        elif data > self.temperatureLimitUpper and self.torso == "cool":
            self.granular.append(1)
            return True
        elif data < self.temperatureLimitLower and self.torso == "hot":
            self.granular.append(1)
            return True
        elif data > self.temperatureLimitUpper and self.torso != "hot":
            self.granular.append(2)
            return False
        elif data < self.temperatureLimitLower and self.torso != "cool":
            self.granular.append(0)
            return False
        elif self.temperatureLimitUpper > data > self.temperatureLimitLower and self.torso == "hot":
            self.granular.append(2)
            return False
        elif self.temperatureLimitUpper > data > self.temperatureLimitLower and self.torso == "cool":
            self.granular.append(0)
            return False

    def gasGiantCalc(self, data):
        """
        Calculates the gas giant survivability
        """
        if data == "No":
            self.granular.append(0)
            return True
        elif self.legs == "rocket":
            self.granular.append(0)
            return True
        else:
            self.granular.append(1)
            return False

    def setBodyParts(self, astronautArray):
        """
        Sets value of the bodyparts, based on what the user selected
        """

        self.bodyError.clear()

        bootsMSG = astronautArray[0:3]
        if bootsMSG.count("1") == 1:
            if bootsMSG[0] == "1":
                self.boots = "light"
            elif bootsMSG[1] == "1":
                self.boots = "medium"
            elif bootsMSG[2] == "1":
                self.boots = "heavy"
            self.bodyError.append(0)
        elif "1" not in bootsMSG:
            self.boots = "none"
            self.bodyError.append(1)
        elif bootsMSG.count("1") > 1:
            self.boots = "none"
            self.bodyError.append(1)

        # TODO: fix to current body parts
        legsMSG = astronautArray[3:5]
        if legsMSG.count("1") == 1:
            if legsMSG[0] == "1":
                self.legs = "regular"
            elif legsMSG[1] == "1":
                self.boots = "rocket"
            self.bodyError.append(0)
        elif "1" not in legsMSG:
            self.boots = "none"
            self.bodyError.append(1)
        elif legsMSG.count("1") > 1:
            self.boots = "none"
            self.bodyError.append(1)

        torsoMSG = astronautArray[5:8]
        if torsoMSG.count("1") == 1:
            if astronautArray[5] == "1":
                self.torso = "cool"
            elif astronautArray[6] == "1":
                self.torso = "regular"
            elif astronautArray[7] == "1":
                self.torso = "hot"
            self.bodyError.append(0)
        elif "1" not in torsoMSG:
            self.torso = "none"
            self.bodyError.append(1)
        elif torsoMSG.count("1") > 1:
            self.torso = "none"
            self.bodyError.append(1)

        helmetMSG = astronautArray[8:11]
        if helmetMSG.count("1") == 1:
            if astronautArray[8] == "1":
                self.helmet = "gas"
            elif astronautArray[9] == "1":
                self.helmet = "oxygen"
            elif astronautArray[10] == "1":
                self.helmet = "no"
            self.bodyError.append(0)
        elif "1" not in helmetMSG:
            self.helmet = "none"
            self.bodyError.append(1)
        elif helmetMSG.count("1") > 1:
            self.helmet = "none"
            self.bodyError.append(1)

    def setPlanet(self, planetArray):
        """
        Sets value of planet, based on what the user selected
        """

        if planetArray.count("1") > 1:
            self.planet = "Too many"
            print("Too many planets")
        elif planetArray[0] == "1":
            self.planet = "Mercury"
        elif planetArray[1] == "1":
            self.planet = "Venus"
        elif planetArray[2] == "1":
            self.planet = "Moon"
        elif planetArray[3] == "1":
            self.planet = "Mars"
        elif planetArray[4] == "1":
            self.planet = "Jupiter"
        elif planetArray[5] == "1":
            self.planet = "Saturn"
        elif planetArray[6] == "1":
            self.planet = "Uranus"
        elif planetArray[7] == "1":
            self.planet = "Neptune"
        elif "1" not in planetArray:
            self.planet = "Earth"

    def getSurvival(self):
        return self.survival, self.survivalBool

    def getPlanetData(self):
        return self.curData

    def getGranularData(self):
        """
        Granular data: an array of 4 variables. Only used once the astronaut has landed on the planet
        first value = toxicity; 0 = no toxic, 1 = toxic
        second value = oxygen; 0 = no oxygen, 1 = oxygen
        third value = temperature; 0 = cold, 1 = normal, 2 is hot
        fourth value = gas giant; 0 = no gas giant, 1 = gas giant
        """
        return self.granular

    def returnDist(self):
        return self.curData[12]

    def returnError(self):
        self.error.clear()
        if self.planet == "Earth":
            self.error.append(1)
        elif self.planet == "Too many":
            self.error.append(2)
        else:
            self.error.append(0)

        if 1 in self.bodyError:
            self.error.append(1)
        else:
            self.error.append(0)
        return self.error

    def getTravelTime(self):
        travelDelay = int((float(self.curData[12]) ** 0.25) * self.frameRate * self.travelDuration)
        return travelDelay
