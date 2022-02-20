'''
Python program to create a bytearray from a list.
'''

'''
The Python bytearray() function converts strings or collections of integers into a mutable sequence of bytes. 
It provides developers the usual methods Python affords to both mutable and byte data types. 
Python's bytearray() built-in allows for high-efficiency manipulation of data in several common situations
The Python bytearray() function's powerful features do come with some responsibility. 
Developers must be mindful of encodings, be aware of source data format, and have a basic working knowledge 
of common character sets like ASCII.
'''

print()
nums = [10, 20, 56, 35, 17, 99]
# Create bytearray from list of integers.
values = bytearray(nums)
for x in values: print(x)
print()
