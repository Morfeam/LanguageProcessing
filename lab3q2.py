#Matthew Morfea - 2/4/20
import sys

f1 = open(sys.argv[1],"r")
f2 = open(sys.argv[2],"w")
for x in range(1, 11):
	line = f1.readline()
	print(line)
	f2.write(line)
f1.close()
f2.close()
