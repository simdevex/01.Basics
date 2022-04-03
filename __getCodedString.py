'''
Write a Python program to create a coded string from a given
string, using specified formula. Go to the editor
Replace all 'P' with '9', 'T' with '0', 'S' with '1', 'H' with '6' and 'A' with
'8'
Original string: PHP
Coded string: 969
Original string: JAVASCRIPT
Coded string: J8V81CRI90

'''

def test(str):
    '''
    maketrans() method returns a mapping table for translation usable for translate() method. 
    It is a static method that creates a one to one mapping of a character to its translation/replacement.
    It creates a Unicode representation of each character for translation. This translation mapping 
    is then used for replacing a character to its mapped character when used in translate() method.       
    '''
    return str.translate(str.maketrans('PTSHA', '90168'))

str = "PHP"
print("Original string: ",str)
print("Coded string: ",test(str))
str = "JAVASCRIPT"
print("\nOriginal string: ",str)
print("Coded string: ",test(str))


txt = "Hello Sam!"
# mytable = txt.translate(txt.maketrans("S", "P"))
mytable = txt.maketrans("S", "P")
print(mytable) # {83: 80}
print(txt.translate (mytable)) # Hello Pam!
