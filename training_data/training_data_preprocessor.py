import sys
import csv
#Progamm, dass den Startzeitpunkt jedes Klimmzug-Zeitfenster-File auf ~0 setzt, damit es spaeter einfacher bearbeitet werden kann. Ausserdem wird nur noch die Startzeit des jeweiligen Zeitfensters in das Ergebnis-File geschrieben.

outputfile = sys.argv[2]

with open(sys.argv[1]) as csvfile:
       file = open(outputfile,"w")
       reader = csv.reader(csvfile, delimiter=',', quotechar='|')
       rows = list(reader)
       startValue = int(rows[0][0])
       print(startValue)
       for row in rows:
           print(row)
           file.write(str(int(row[1])-startValue)+","+str(row[2])+","+str(row[3])+","+str(row[4])+","+str(row[5])+","+str(row[6]))
           file.write(","+str(row[7])+"\n")
       file.close()
           
         
