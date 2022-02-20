'''
a Python program to find whether a given number (accept fromthe user) is even or odd, 
print out an appropriate message to the user.
'''

def checkNumberType (inputNum):
    funcNum = int (inputNum)
    if (funcNum % 2) == 0:
        return "Even number"
    else:
        return "Odd number"
    
def main ():
    myNum = input("Input a number")
    print (checkNumberType (myNum))

main ()