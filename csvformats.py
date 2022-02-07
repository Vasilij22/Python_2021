#Var izmantot iebūvēto moduli csv

import csv

file = open("csv_meg.csv")

print(type(file))

lasit_csv = csv.reader(file)

print(lasit_csv)

#Kolonnu nosaukumi

header = []
header = next(lasit_csv)
print(header)