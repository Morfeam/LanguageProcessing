#Matthew Morfea 2/7/20
s = input("Enter a String: ")
slist = []
rev = ""
for x in range(0,len(s)):
    slist.append(s[x])
for i in range(0,len(s)):
    rev = rev + slist.pop()
if s == rev:
    print(s + " is a palindrome")
else:
    print(s + " is not a palindrome")
