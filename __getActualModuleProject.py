'''
Python program to get the actual module object for a givenobject.
'''

'''
The inspect module provides several useful functions to help get information about live objects 
such as modules, classes, methods, functions, tracebacks, frame objects, and code objects. 
For example, it can help you examine the contents of a class, retrieve the source code of a method, 
extract and format the argument list for a function, or get all the information you need to display 
a detailed traceback.

'''


#Sample Solution-1
from inspect import getmodule
from math import sqrt
print("Sample Solution 1: ", getmodule(sqrt))

#Sample Solution-2:
import inspect
def add(x, y):
    return x + y
print("Sample Solution 2: ", inspect.getmodule(add))

