import sys
import math
import csv 

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
filename = sys.argv[3]
file = open(filename,"a")
templist = []
werte = []
rowlist = []

# Werte des CSV in eine Liste packen
with open(sys.argv[1]) as csvfile:
       reader = csv.reader(csvfile, delimiter=',', quotechar='|')
       for row in reader:
         rowlist.append(row)

i = 0
istart = 0
count = 0

# Zaehle Schritte bis zu naechstem Fenster(count), gehe um Haelfte der Schritte zurueck und wiederhole das ganze.
# Pruefe dazu, ob der Zeitwert des unteruchten Elements mindestens so gross ist, wie Startzeit des Fensters(Zeit bei istart)+window_size.
# Falls dies der Fall, fuehre Berechnungen fuer aktuelles Fenster aus, setze i auf int(count/2), istart auf i und count wieder auf Null.

while(i < len(rowlist)):
     t = int(rowlist[i][0])
     x,y,z = rowlist[i][1],rowlist[i][2],rowlist[i][3]
     vector = [x,y,z]
     templist.append(vector)
     count += 1
     if(t >= int(rowlist[istart][0])+window_size):
       average = m(templist)
       # Werte fuer Zeitfenster mit Start- und Endzeit in Ergebnisliste eintragen
       werte.append([int(rowlist[istart][0])]+[int(rowlist[i][0])]+average+std(templist,average))
       templist = []
       i -= int(count/2)
       istart = i
       count=0
     i+=1
       



print("Werte:\n")
for x in werte:
        print (x)
        file.write(str(x[0])+","+str(x[1])+","+str(x[2])+","+str(x[3])+","+str(x[4])+","+str(x[5])+","+str(x[6])+","+str(x[7])+"\n")
print("\n")

file.close()


