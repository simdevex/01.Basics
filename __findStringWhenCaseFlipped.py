'''
Python program to find string "s" that, when case is flipped gives target where 
vowels are replaced by chars two later. 
Input: Python
Output:
pYTHQN
Input: aeiou
Output:
CGKQW
Input: Hello, world!
Output:
hGLLQ, WQRLD!
Input: AEIOU
Output:
cgkqw
'''

#License: https://bit.ly/3oLErEI

def test(strs):
    '''
    Python ord() function returns the Unicode code from a given character. 
    This function accepts a string of unit length as an argument and returns 
    the Unicode equivalence of the passed argument.
    
    swapcase() method returns the string where all uppercase characters are converted 
    to lowercase, and lowercase characters are converted to uppercase.

    '''
    return strs.translate({ord(c):ord(c)+2 for c in "aeiouAEIOU"}).swapcase()

strs = "Python" 
print("Original string:",strs)
print("Find string s that, when case is flipped gives target where vowels are replaced by chars two later:")
print(test(strs))
strs = "aeiou" 
print("\nOriginal string:",strs)
print("Find string s that, when case is flipped gives target where vowels are replaced by chars two later:")
print(test(strs))
strs = "Hello, world!" 
print("\nOriginal string:",strs)
print("Find string s that, when case is flipped gives target where vowels are replaced by chars two later:")
print(test(strs))
strs = "AEIOU" 
print("\nOriginal string:",strs)
print("Find string s that, when case is flipped gives target where vowels are replaced by chars two later:")
print(test(strs)) 
