"""
This class takes care of retrieving the data from the .csv file and does the calculations with it
"""

import csv
import pandas as pd

class DatCalc:

    def __init__(self):
        "Insert stuff"
        self.dataConnect()
        self.curData = []
        self.boots = "none"
        self.legs = "none"
        self.torso = "none"
        self.helmet = "none"

        self.gravityLimit = []
        self.temperatureLimit = []

    def dataConnect(self):
        """
        This function will connect to the .csv file.
        """

        file = open('Planet Data.csv')
        type (file)
        csvreader = csv.reader(file)
        self.rows = []
        for row in csvreader:
            self.rows.append(row)
        file.close()

        for i in range(0, len(self.rows)):
            pop = self.rows[i].pop(0)
            self.rows[i] = pop.split(';')

        self.dataRetrieve()

    def dataRetrieve(self):
        """
        This function will retrieve data from the .csv file.
        """
        self.planet = "Mercury"
        for i in range(0, len(self.rows)):
            if self.planet in self.rows[i]:
                self.curData = self.rows[i]
                print(self.rows[i])

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
        self.gravityCalc(self.curData[1])

    def gravityCalc(self, data):
        pass

    def toxicityCalc(self, data):
        pass

    def oxygenCalc(self, data):
        pass

    def temperatureCalc(self, data):
        pass

    def gasGiantCalc(self, data):
        pass

    def gearScoreCalc(self):
        """
        This function calculates the properties of the gear from the astraut to pass to survivalcalc
        """

        self.dataConnect()
        self.curData = []
        self.boots = "none"
        self.legs = "none"
        self.torso = "none"
        self.helmet = "none"

    def humanSurvivabilityCalc(self):
        """
        This function calculates the limits of human survivability
        """
        self.gravityLimit.append(0.85)
        self.gravityLimit.append(1.15)


    def planetScoreCalc(self):
        """
        This function calculates the values for physicalizing the planet data and passing to survivalcalc
        """


connect = DatCalc()