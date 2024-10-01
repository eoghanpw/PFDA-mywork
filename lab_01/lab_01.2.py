# Program to read in data.csv file and output each line as a list.
# Author: Eoghan Walsh

import csv

FILENAME = "data.csv"
DATADIR = "../lab_01/"

print(DATADIR + FILENAME)

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    for line in reader:
        print(line)
