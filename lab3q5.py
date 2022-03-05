#Matthew Morfea - 2/4/20
nlist = []
for x in range(0,10):
    nlist.append(input("Enter a Number:"))
print("First to Last Order")
for y in range(0,10):
    print(nlist[y])
print("Last to First Order")
for z in reversed(nlist):
    print(z)
print("Last to First Order using '.pop()' function")
for i in range(0,10):
    print(nlist.pop())

    
