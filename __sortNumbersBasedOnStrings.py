'''
Python program to sort numbers based on strings.
Input: six one four one two three
Output:
one two three four six
Input: six one four three two nine eight
Output:
one two three four six eight nine
Input: nine eight seven six five four three two one
Output:
one two three four five six seven eight nine
'''

#License: https://bit.ly/3oLErEI

def test(strs):
    return ' '.join([x for x in 'one two three four five six seven eight nine'.split() if x in strs])

strs = "six one four one two three"
print("Original string:",strs)
print("Sort numbers based on said strings:")
print(test(strs))
strs = "six one four three two nine eight"
print("\nOriginal string:",strs)
print("Sort numbers based on said strings:")
print(test(strs))
strs = "nine eight seven six five four three two  one"
print("\nOriginal string:",strs)
print("Sort numbers based on said strings:")
print(test(strs))
