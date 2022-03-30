'''
Write a Python program to test whether a given integer is pandigital number or not.

From Wikipedia,
A number is said to be pandigital if it contains each of the digits from 0 to 9 
(and whose leading digit must be nonzero). However, "zeroless" pandigital quantities 
contain the digits 1 through 9. Sometimes exclusivity is also required so that each digit 
is restricted to appear exactly once. For example, 6729/13458 is a (zeroless, restricted) 
pandigital fraction and 1023456789 is the smallest (zerofull) pandigital number

In mathematics, a pandigital number is an integer that in a given 
base has among its significant digits each digit used in the base at least once.

For example,
1223334444555556666667777777888888889999999990 is a  pandigital number in base 10.

The first few pandigital base 10 numbers are given by:
1023456789, 1023456798, 1023456879, 1023456897,
1023456978, 1023456987, 1023457689
Sample Input:
(1023456897)
(1023456798)
(1023457689)
(1023456789)
(102345679)
Sample Output:
True
True
True
True
False

'''

def is_pandigital_num(n):
    return len(set(str(n))) == 10 #remove duplicates, reduce to first ten digits 0123456789

n = 1023456897
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))
n = 1023456798
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))
n = 1023457689
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))
n = 1023456789
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))
n = 102345679
print("Original number:",n)
print("Check the said number is Pandigital number or not?")
print(is_pandigital_num(n))

