'''
Python program to find the positions of all uppercase vowels (not counting Y) in even indices of a given string.
Input: w3rEsOUrcE
Output:
[6]
Input: AEIOUYW
Output:
[0, 2, 4]
A vowel is a syllabic speech sound pronounced without any stricture in the vocal tract. 
Vowels are one of the two principal classes of speech sounds, the other being the consonant. 
Vowels vary in quality, in loudness and also in quantity. 
There are six vowels in the English language: a, e, i, o, u and sometimes y.
'''

#License: https://bit.ly/3oLErEI

def test(strs):
    return [i for i, c in enumerate(strs) if i % 2 == 0 and c in "AEIOU"] 

strs = "w3rEsOUrcE "
print("Original List:",strs)
print("Positions of all uppercase vowels (not counting Y) in even indices:")
print(test(strs))
strs = "AEIOUYW "
print("\nOriginal List:",strs)
print("Positions of all uppercase vowels (not counting Y) in even indices:")
print(test(strs))
