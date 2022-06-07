#This is a code snippet that can be used to import a csv and store its content

import csv

data = open("Planet Data.csv")

readCsv = csv.reader(data)
measureNames = next(readCsv)
#print(measureNames)
rows = []
for row in readCsv:
    rows.append(row)
#print(rows)
#accessing only one planet
print(rows[0])
data.close()