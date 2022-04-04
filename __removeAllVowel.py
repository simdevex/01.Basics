'''
Python program to remove all vowels from a given string. 
Original string: Python
After removing all the vowels from the said string: Pythn
Original string: C Sharp
After removing all the vowels from the said string: C Shrp
Original string: JavaScript
After removing all the vowels from the said string: JvScrpt
'''

#using regular expressions
import re
def test(text):
    return re.sub(r'[aeiou]+', '', text, flags=re.IGNORECASE)

text = "Python";
print("Original string:",text)
print("After removing all the vowels from the said string: " + test(text))

text = "C Sharp"
print("\nOriginal string:",text)
print("After removing all the vowels from the said string: " + test(text))

text = "JavaScript"
print("\nOriginal string:",text)
print("After removing all the vowels from the said string: " + test(text))
