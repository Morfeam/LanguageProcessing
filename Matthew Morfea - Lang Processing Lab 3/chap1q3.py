file = open("p0103.txt","r")
mylist = []
dlist = []
alist = []
for i in file:
    this = i.split(" ")
    mylist.append(this)
    for char in this:
        if char[0].isdigit():
            dlist.append(char)
            
        else:
            alist.append(char)
            
print(alist)
print(dlist)
