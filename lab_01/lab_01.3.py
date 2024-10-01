# Program to read in data.csv file and output each line as a list,
# and deal with the header line separately.
# Author: Eoghan Walsh

import csv

FILENAME = "data.csv"
DATADIR = "../lab_01/"

print(DATADIR + FILENAME)

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",")
    linecount = 0
    for line in reader:
        if not linecount:
            print(f"{line}\n--------------------")
        else:
            print(line)
        linecount += 1
