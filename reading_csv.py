import csv

with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    for row in rdr:
        row[0] = int(row[0])
        row[-1] = row[-1].upper()
        print(row)
print()

with open('DATA/airport_boardings.csv') as ab_in:
    rdr = csv.reader(ab_in)
    header = next(rdr)  # consume next row (ie, first line of file)
    for row in rdr:
        print(row)

