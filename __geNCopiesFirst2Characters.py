'''
A Python program to get the n (non-negative integer) copies ofthe first 2 characters of a given string. 
Return the n copies of the wholestring if the length is less than 2.
'''

def getCopies (inputStr, nCopies):
    
    subStr = inputStr[0:2]
    inputNumber = int(nCopies)
    outStr =""
    
    for i in range(inputNumber):
        outStr = outStr + subStr 
            
    print (outStr)
        
def main ():
    myStr = input ("Write a sentence")
    myCopies = input ("Enter number of copies:")
    getCopies(myStr, myCopies )
    
main ()

