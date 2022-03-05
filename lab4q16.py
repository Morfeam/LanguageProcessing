#Matthew Morfea - 2/19/20
import sys
n = int(input("Enter a positive integer: "))
for i in range(1,n+2):
    for j in range(1,i):
        print(j, end='')
    print()
