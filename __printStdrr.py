'''
A Python program to print to stderr.
Stderr is the standard error message that is used to print the output on the screen or windows terminal. 
Stderr is used to print the error on the output screen or window terminal. 
Stderr is also one of the command output as stdout, which is logged anywhere by default.
'''
from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")
