'''
Python program to get a new string from a given string where"Is" has been added to the front. 
If the given string already begins with"Is" then return the string unchanged
'''

def checkString (inputString =''):
    if inputString[0:2] == "Is":
        return inputString
    else:
        return "Is " + inputString
    
def main():
    myString = input ("Please type a sentence: ")
    print (checkString (myString))
    
main ()

        
    