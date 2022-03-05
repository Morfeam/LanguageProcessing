#Matthew Morfea 2/8/20
import math
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
    
sum = 2
print(sum)
for n in range(2,100):
    sum = sum + (1/factorial(n))
print(sum)

#This number is equal to the constant 'e' in mathematics, used in describing
#logirithms and natural logs.


