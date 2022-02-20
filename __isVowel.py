'''
A Python program to test whether a passed letter is a vowel ornot.

'''

def isVowel (inputStr):
    vowelTuple = ('a', 'e', 'i', 'o', 'u')
    
    for vowel in vowelTuple:
        if inputStr == vowel:
            return True
    return False
                
def main ():
    myStr = input ("Enter a letter")
    isStrVowel = isVowel(myStr)
    if isStrVowel:
        print ("You input a vowel")
    else:
        print ("You input a consonant")
        
main()
    
            