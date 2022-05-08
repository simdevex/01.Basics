'''
Python program to find which characters of a hexadecimal number correspond to prime numbers.
Input: 123ABCD
Output:
[False, True, True, False, True, False, True]
Input: 123456
Output:
[False, True, True, False, True, False]
Input: FACE
Output:
[False, False, False, False]
'''

#License: https://bit.ly/3oLErEI

def test(hn):
    return [c in "2357BD" for c in hn] 

hn = "123ABCD"
print("Original hexadecimal number:",hn) 
print("Characters of the said hexadecimal number correspond to prime numbers:")
print(test(hn))
hn = "123456"
print("\nOriginal hexadecimal number:",hn) 
print("Characters of the said hexadecimal number correspond to prime numbers:")
print(test(hn))
hn = "FACE"
print("\nOriginal hexadecimal number:",hn) 
print("Characters of the said hexadecimal number correspond to prime numbers:")
print(test(hn))
