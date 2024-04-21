import csv


with open('test.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

with open('test.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
