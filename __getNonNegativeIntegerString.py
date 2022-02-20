'''
A Python program to get a string which is n (non-negative integer) copies of a given string
'''

def getNCopyOfStrings (numberOfCopies,  inputString = ''):
    myString = inputString
    for count in range (numberOfCopies):
        myString = myString + '\n'+ inputString
    return myString   

def main() :
    print ("The string is : ", getNCopyOfStrings (3, "This is me"))
    
main ()

