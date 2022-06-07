"""
This class takes care of retrieving the data from the .csv file and does the calculations with it
"""

import csv
import pandas as pd

class DatCalc:

    def __init__(self):
        "Insert stuff"

    def dataConnect(self):
        """
        This function will connect to the .csv file.
        """
        file = open('Planet Data.csv')
        type (file)
        csvreader = csv.reader(file)
        self.header = []
        self.header = next(csvreader)
        self.rows = []
        for row in csvreader:
            self.rows.append(row)
        file.close()
        print(self.header)
        print(self.rows[2])
        '''
        data = pd.read_csv("Planet Data.csv")
        data.Mercury()
        '''

    def dataRetrieve(self):
        """
        This function will retrieve data from the .csv file.
        """

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

