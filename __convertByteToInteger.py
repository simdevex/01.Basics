'''
Python program to convert a byte string to a list of integers.

A prefix of 'b' or 'B' is ignored in Python 2; it indicates that
the literal should become a bytes literal in Python 3 (e.g. when code is automatically converted with 2to3). 
A 'u' or 'b' prefix may be followed by an 'r' prefix.

A prefix of 'b' or 'B' is ignored in Python 2; it indicates that 
the literal should become a bytes literal in Python 3 (e.g. when code is automatically converted with 2to3). 
A 'u' or 'b' prefix may be followed by an 'r' prefix.
'''

def convertByteToIntegerOptionOne():
    S = "ABC"    
    print("Original string:")
    '''
    The b' notation is used to specify a bytes string in Python. Compared to the regular strings, 
    which have ASCII characters,  the bytes string is an array of byte variables where each hexadecimal 
    element has a value between 0 and 255. The b" notation is used to specify a bytes string in Python. 
    Compared to the regular strings, which have ASCII characters, the bytes string is an array of byte 
    variables where each hexadecimal element has a value between 0 and 255.

    '''
    x = b'ABC'
    print("Original string:")
    print(S)
    print("\nConvert bytes of the said string to a list of integers:")
    print(list(x))
    print()

def convertByteToIntegerOptionTwo():
    S = "The quick brown fox jumps over the lazy dog."  
    print("Original string:")
    print(S)
    nums = []
    print("\nConvert bytes of the said string to a list of integers:")
    for chr in S:
        nums.append(ord(chr))
    print(nums)
    
def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : convertByteToIntegerOptionOne,
                  2 : convertByteToIntegerOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()