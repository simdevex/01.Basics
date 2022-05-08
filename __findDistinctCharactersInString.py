'''
Python program to find the set of distinct characters in a given string, ignoring case.
Input: HELLO
Output:
['h', 'o', 'l', 'e']
Input: HelLo
Output:
['h', 'o', 'l', 'e']
Input: Ignoring case
Output:
['s', 'n', 'c', 'o', 'e', 'i', 'r', 'g', 'a', ' ']

'''

#License: https://bit.ly/3oLErEI

def test(strs):
    return [*set(strs.lower())]
 
strs = "HELLO"
print("Original string:",strs)
print("Set of distinct characters in the said string, ignoring case:")
print(test(strs))
strs = "HelLo"
print("\nOriginal string:",strs)
print("Set of distinct characters in the said string, ignoring case:")
print(test(strs))
strs = "Ignoring case"
print("\nOriginal string:",strs)
print("Set of distinct characters in the said string, ignoring case:")
print(test(strs))
