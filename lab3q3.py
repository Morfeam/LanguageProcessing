#Matthew Morfea - 2/4/20
import sys

f1 = open(sys.argv[1],"r")
f2 = open(sys.argv[2],"w")
for y in range(1, 11):
	line = f1.readline()
	print(str(y) + line)
	f2.write(str(y) + line)
f1.close()
f2.close()
