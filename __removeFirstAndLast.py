'''
Python program to remove the first and last elements
from a given string.
Original string: PHP
Removing the first and last elements from the said string: H
Original string: Python
Removing the first and last elements from the said string: ytho
Original string: JavaScript
Removing the first and last elements from the said string: avaScrip
'''

def test(str):
    #check length first, and then remove first and last charecter if the length is 3 or more
    return str if len(str) < 3 else str[1:-1]

str = "PHP"
print("Original string: ",str)
print("Removing the first and last elements from the said string: ",test(str))
str = "Python"
print("\nOriginal string: ",str)
print("Removing the first and last elements from the said string: ",test(str))
str = "JavaScript"
print("\nOriginal string: ",str)
print("Removing the first and last elements from the said string: ",test(str))
