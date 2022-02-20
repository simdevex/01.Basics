'''
Python program to convert an integer to binary keep leading zeros

Converting an integer to an n-bit binary number results in its binary representation containing leading zeros
up to length n. For example, to convert the integer 5 to a 6-bit binary results in 000101.
format(num, name) function with name as "0nb" to convert an integer num to a binary string with leading zeros up
to length n.

Sample data : x=12
Expected output : 00001100
0000001100
'''

x = 12
print(format(x, '08b'))
print(format(x, '010b'))

