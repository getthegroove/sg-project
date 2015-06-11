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



input_file = open(sys.argv[1],"r")
window_size = int(sys.argv[2])
values = input_file.read().split('\n')
input_file.close()
templist = []
mittelwerte = []
for v in values:
	entry = v.split(', ')
	print( entry)
	if entry[0] == '':
		break
	t = int(entry[0])
	vector = entry[1:]
	templist.append(vector)
	if t % window_size == 0 and t != 0:
		mittelwerte.append(m(templist))
		templist = []

for x in mittelwerte:
	print (x)


