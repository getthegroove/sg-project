import sys
def m(values):
	x = 0
	y = 0
	z = 0
	for v in values:
		x = x + float(v[0])
		y = y + float(v[1])
		z = z + float(v[2])
	return [x/len(values), y / len(values), z / len(values)]




window_size = int(sys.argv[2])
templist = []
mittelwerte = []

import csv 
with open(sys.argv[1]) as csvfile:
       reader = csv.reader(csvfile, delimiter=',', quotechar='|')
       for row in reader:
          t = int(row[0])
          x,y,z = row[1],row[2],row[3]
          vector = [x,y,z]
          templist.append(vector)
          if t % window_size == 0 and t!=0:
             mittelwerte.append(m(templist))
             templist = []

for x in mittelwerte:
	print (x)


