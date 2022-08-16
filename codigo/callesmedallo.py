import csv
f= open("calles_de_medellin_con_acoso.csv")
reader = csv.reader(f)
for row in reader:
    print (row)   