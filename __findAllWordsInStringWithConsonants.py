'''
Python program to find all words in a given string with n consonants.
Input: this is our time
Output:
Number of consonants: 3
Words in the said string with 3 consonants:
['this']
Number of consonants: 2
Words in the said string with 2 consonants:
['time']
Number of consonants: 1
Words in the said string with 1 consonants:
['is', 'our']
Click me to see the sample solution
'''

#License: https://bit.ly/3oLErEI

def test(strs, n):
    return [w for w in strs.split() if sum([c not in "aeiou" for c in w.lower()]) == n]

strs = "this is our time"
print("Original string:",strs)
n = 3
print("Number of consonants:",n)
print("Words in the said string with",n,"consonants:")
print(test(strs, n))
n = 2
print("\nNumber of consonants:",n)
print("Words in the said string with",n,"consonants:")
print(test(strs, n))
n = 1
print("\nNumber of consonants:",n)
print("Words in the said string with",n,"consonants:")
print(test(strs, n))
