import pickle
from sklearn import tree
import sys
import csv

files = []
result = []
filename = sys.argv[1]
clf = pickle.load(open("save_"+filename+".p","rb"))


with open(sys.argv[2],"r") as csvfile:
     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in reader:
         files = files + [row[2:8]]

result = clf.predict(files)

for i in result:
    if (i==0):
       print("static"+"\n")
    elif (i==1):
       print("right-left"+"\n")
    elif (i==2):
       print("forward-backward"+"\n")
    elif(i==3):
       print("up-down"+"\n")
