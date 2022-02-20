'''
Python program to get the ASCII value of a character.
'''


def getASCII (char):
    return ord(char)

def main ():
    inpASCII = str (input ("Input a charected to get ASCII value\n"))
    print ('ASCII number is', getASCII ( inpASCII ))
    
main ()