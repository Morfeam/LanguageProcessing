#Matthew Morfea 2/7/20
n = int(input("Enter a Number: "))
numCount = 0
i = 1
while i < n : 
    if (n % i==0) : 
        numCount = numCount + i
    i = i + 1
if numCount == n:
    print("True")
else:
   print("False")
