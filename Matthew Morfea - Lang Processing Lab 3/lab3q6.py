#Matthew Morfea - 2/4/20
def concatlists(L1,L2):
    for x in L2:
        L1.append(x)
list1 = []
list1.append("Hello")
list2 = []
list2.append("World")
print(list1)
concatlists(list1,list2)
print(list1)

