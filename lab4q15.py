#Matthew Morfea 2/8/20
import math

x = int(input("Enter a positive number: "))
for i in range(0,100):
    x = math.sqrt(x)
print(x)

#The value of x converges to the number 1.0 for every postive number execpt when x = 0.
#When x = 0, the number stays at a constand 0.0. 
