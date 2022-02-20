'''
Python program to check the priority of the four operators (+, -, *, /)
'''
from collections import deque
import re

__priority__ = {
    '-': 1,
    '+': 2,
    '*': 3,
    '/': 4,
}

def test_higher_priority (operator1, operator2):
    return __priority__[operator1] > __priority__[operator2]

print(test_higher_priority('*','-'))
print(test_higher_priority('+','-'))
print(test_higher_priority('+','*'))
print(test_higher_priority('+','/'))
print(test_higher_priority('*','/'))
