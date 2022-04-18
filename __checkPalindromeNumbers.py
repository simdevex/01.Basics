'''
Write a Python program to check whether the given strings are
palindromes or not. Return True, False.

A string is a palindrome when it reads the same backward as forward

Input:
['palindrome', 'madamimadam', '', 'foo', 'eyes']
Output:
[False, True, True, False, False]
'''

#License: https://bit.ly/3oLErEI

def test(strs):
    
    statList = []
    '''
    for s in strs:
        statList.append(s == s[::-1])
        
    return statList
    '''
    # compact return statement
    return [s == s[::-1] for s in strs]

strs = ['palindrome', 'madamimadam', '', 'foo', 'eyes']
print("Original strings:")
print(strs)
print("\nTest whether the given strings are palindromes or not:")
print(test(strs))
