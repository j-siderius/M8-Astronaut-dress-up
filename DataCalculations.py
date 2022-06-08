"""
This class takes care of retrieving the data from the .csv file and does the calculations with it
"""

import csv
import pandas as pd

class DatCalc:

    def __init__(self):
        "Insert stuff"
        self.dataConnect()

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
                print(self.rows[i])

    def survivalCalc(self):
        """
        This function calculates whether the astronaut will survive or not and in which areas
        """

    def gearScoreCalc(self):
        """
        This function calculates the values for physicalizing the planet data and passing to survivalcalc
        """

    def planetScoreCalc(self):
        """
        This function calculates the properties of the gear from the astraut to pass to survivalcalc
        """


connect = DatCalc()