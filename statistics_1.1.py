import sys
import math
def m(values):
	x = 0
	y = 0
	z = 0
	for v in values:
		x = x + float(v[0])
		y = y + float(v[1])
		z = z + float(v[2])
	return [x/len(values), y / len(values), z / len(values)]

def std(values,average):
    x,y,z = 0,0,0
    for v in values:
        x += (float(v[0])-average[0])**2
        y += (float(v[1])-average[1])**2
        z += (float(v[2])-average[2])**2
    return[math.sqrt(x/len(values)),math.sqrt(y/len(values)),math.sqrt(z/len(values))]


window_size = int(sys.argv[2])
templist = []
mittelwerte = []
standardabweichung = []
import csv 
with open(sys.argv[1]) as csvfile:
       reader = csv.reader(csvfile, delimiter=',', quotechar='|')
       for row in reader:
          t = int(row[0])
          x,y,z = row[1],row[2],row[3]
          vector = [x,y,z]
          templist.append(vector)
          if t % window_size == 0 and t!=0:
             average = m(templist)
             mittelwerte.append(average)
             standardabweichung.append(std(templist,average))
             templist = []

for x in mittelwerte:
	print (x)
print("\n")

for x in standardabweichung:
        print(x)


