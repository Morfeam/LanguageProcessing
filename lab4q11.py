#Matthew Morfea 2/7/20
import sys
import string
letterCounter= dict(zip(string.ascii_lowercase,[0]*26))
with open('cookies.txt') as f1:
    for line in f1:
        for word in line.split():
            for letter in list(word):
                letterCounter[letter]+=1
print(letterCounter)
