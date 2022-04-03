'''
Python program to reverse a given string in lower case. 
Original string: PHP
Reverse the said string in lower case: php
Original string: JavaScript
Reverse the said string in lower case: tpircsavaj
Original string: PHPP
Reverse the said string in lower case: pphp
'''

def test(str1):
    #reverse string, and then convert to lower case
    return str1[::-1].lower()

str = "PHP"
print("Original string:",str)
print("Reverse the said string in lower case:",test(str))
str = "JavaScript"
print("\nOriginal string:",str)
print("Reverse the said string in lower case:",test(str))
str = "PHPP"
print("\nOriginal string:",str)
print("Reverse the said string in lower case:",test(str)) 
