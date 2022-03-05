#Matthew Morfea 2/7/20
count = 0
slist = []
test = "pr"
for x in range(0,10):
    print("Enter a String")
    slist.append(input())
for i in range(0,10):
    if test in slist[i]:
        count = count + 1 
print(count)
