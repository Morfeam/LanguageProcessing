#Matthew Morfea - 2/4/20
def getgrade(x):
    if x >= 75:
        print("First Quartile")
    if x < 75 and x >= 50:
        print("Second Quartile")
    if x < 50 and x >= 25:
        print("Third Quartile")
    if x < 25 and x >= 0:
        print("Fourth Quartile")

print("Enter a Grade between 0 to 100")
x = int(input())
if x > 100 or x < 0:
    print("Runtime Error")
getgrade(x)
