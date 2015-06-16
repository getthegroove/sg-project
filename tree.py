from sklearn import tree
from sklearn.externals.six import StringIO
import sys
import csv
import numpy as np

files = []
Y = []

for i in range(1,len(sys.argv)):
    with open(sys.argv[i],"r") as csvfile:
        tmp_list = []
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
           files = files + [row]
           Y.append(i)
          
print(files)
print(Y)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(files, Y)

with open("iris.dot", "w") as f:
    f = tree.export_graphviz(clf, out_file=f)
