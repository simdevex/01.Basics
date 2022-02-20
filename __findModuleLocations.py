'''
Python program to find the location of Python modulesources
'''
#Location of Python module sources:

import imp
print("Location of Python os module sources:")
print(imp.find_module('os'))
print("\nLocation of Python sys module sources:")
print(imp.find_module('datetime'))

#List of directories of specific module:
import os
print("\nList of directories in os module:")
print(os.path)
print("\nList of directories in sys module:")
import sys
print(sys.path)
