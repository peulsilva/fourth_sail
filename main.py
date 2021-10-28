# Given an array which may contain duplicates, print all elements and their frequencies in descending order.
# Your code solution should be sent to the result printed.

from CharObject import CharObject
from utils import exists, printArray

sep= ' '

fileName= "textFile.txt"

file = open(fileName,"r")

line = file.readline()

charArray=[]
for char in line:
    if not char == sep:
        charObj = CharObject(char)
        if not exists(char,charArray):
            charArray.append(charObj)

charArray = sorted(charArray, key= lambda x: x.count, reverse= True)
        
printArray(charArray)