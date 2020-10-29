import csv

with open('DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    with open('potus.csv', 'w') as potus_out:
        wtr = csv.writer(potus_out)
        for row in rdr:
            wtr.writerow(row[:3])

