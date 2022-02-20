'''
Python program to count the number occurrence of a specifi ccharacter in a string.
'''
import re

#Using count() function:
def getOccuranceUsingCount():
    print ("***Using count() function***")
    s = "The quick brown fox jumps over the lazy dog." 
    print("Original string:")
    print(s)
    print("Number of occurrence of 'o' in the said string:")
    print(s.count("o"))

#Using loop
def getOccuranceUsingLoop():
    print ("***Using loop***") 
    s = "The quick brown fox jumps over the lazy dog."  
    print("Original string:")
    print(s)
    print("Number of occurrence of 'o' in the said string:")
    ctr = 0 
    for c in s:
        if c == 'o':
            ctr = ctr + 1
    print(ctr)

#Using collections.Counter()
def getOccuranceUsingCollection():
    print ("***Using Collections***") 
    from collections import Counter
    s = "The quick brown fox jumps over the lazy dog."  
    print("Original string:")
    print(s)
    print("Number of occurrence of 'o' in the said string:")
    ctr = Counter(s) 
    print (str(ctr['o']))


#Using Lambda functions
def getOccuranceUsingLambda():
    print ("***Lambda Functions***") 
    s = "The quick brown fox jumps over the lazy dog."  
    print("Original string:")
    print(s)
    print("Number of occurrence of 'o' in the said string:")
    ctr = sum(map(lambda x : 1 if 'o' in x else 0, s))
    print(ctr)


#Using Regular Expressions
def getOccuranceUsingRegEx():  
    print ("***Regular Expressions***") 
    s = "The quick brown fox jumps over the lazy dog."  
    print("Original string:")
    print(s)
    print("Number of occurrence of 'o' in the said string:")
    ctr = len(re.findall("o", s))
    print(ctr)

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|4|5|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : getOccuranceUsingCount,
                  2 : getOccuranceUsingLoop,
                  3 : getOccuranceUsingCollection,
                  4 : getOccuranceUsingLambda,
                  5 : getOccuranceUsingRegEx,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()