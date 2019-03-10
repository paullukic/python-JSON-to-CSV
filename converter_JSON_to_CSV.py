import csv
import json

inputFile = open("jupyter\supermarkets.json", "r")  # open JSON
outputFile = open("jupyter\supermarkets_csv.csv", "w")  # load CSV
data = json.load(inputFile)  # gather data from JSON file
inputFile.close()  # close file *must*

writer = csv.writer(outputFile)  # create a csv.write

writer.writerow(data[0].keys())  # header row

for row in data:
    writer.writerow(row.values())  # values row
