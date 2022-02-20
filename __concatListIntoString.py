'''
A Python program to concatenate all elements in a list into a string and return it.
'''

def getStringFromList (inputList):
    localList = list(inputList)
    localStr =''
    for item in localList:
        localStr = localStr + item
        
    return localStr

def main ():
    mainList = input ("Input a comma separate list : ")
    mainStr = getStringFromList(mainList)
    print ("Output string is : ", mainStr )
    
main ()
