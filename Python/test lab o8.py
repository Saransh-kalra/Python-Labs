import csv
a_file=open("lottotexas.csv","r")
reader=csv.reader(a_file)
for row in reader:
    print(row)
