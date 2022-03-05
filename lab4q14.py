#Matthew Morfea 2/8/20
import sys
s = 0
x = 0
n = int(input("Enter a positive integer: "))
while x <= n:
    if x % 2 == 1:
        s = s + x
    x = x + 1
print(n)
print(s)

#The computed sum is always the square of the number of the ceiling(input/2).
#The ceiling function rounding up the decimal to the next whole number.
