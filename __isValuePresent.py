'''
A Python program to check whether a specifi ed value iscontained in a group of values.

'''

def isVowel (inputStr):
    vowelTuple = ('1', '5', '8', '3', '9')
    
    for vowel in vowelTuple:
        if inputStr == vowel:
            return True
    return False
                
def main ():
    myStr = input ("Enter a letter")
    isStrVowel = isVowel(myStr)
    if isStrVowel:
        print ("You input is not from the list")
    else:
        print ("ou input is  from the list")
        
main()
    
            