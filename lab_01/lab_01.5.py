# Program to read in data.csv file as a dict and output average age.
# Author: Eoghan Walsh

import csv

FILENAME = "data.csv"
DATADIR = "../lab_01/"

print(DATADIR + FILENAME)

with open(DATADIR + FILENAME, "rt") as fp:
    reader = csv.DictReader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    count = 0
    for line in reader:
        total += line["age"]
        count += 1
    print(f"The average age is {total/count}")
