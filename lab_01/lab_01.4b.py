# Program to read in data.csv file and output average age.
# Author: Eoghan Walsh

import csv

FILENAME = "data.csv"
DATADIR = "../lab_01/"

print(DATADIR + FILENAME)

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    linecount = 0
    for line in reader:
        if not linecount:
            pass
        else:
            total += line[1]
        linecount += 1
    print(f"The average age is {total/(linecount - 1)}")
