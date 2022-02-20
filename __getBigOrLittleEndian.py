'''
Python program to test whether the system is a big-endianplatform or little-endian platform
'''

import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()
