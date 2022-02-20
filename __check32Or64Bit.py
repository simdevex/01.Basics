'''
Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system
'''

#Sample Solution-1:

import struct
print(struct.calcsize("P") * 8)
