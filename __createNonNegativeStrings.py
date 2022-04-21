'''
Python program to create string consisting of the nonnegative
integers up to n inclusive.
Input:
4
Output:
0 1 2 3 4
Input:
15
Output:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
'''

def test(n):
    #compact return statement for ' '.join, map(), and range()
    return ' '.join(map(str,range(n+1)))

n = 4
print("Non-negative integer:")
print(n)
print("Non-negative integers up to n inclusive:")
print(test(n))
n = 15
print("\nNon-negative integer:")
print(n)
print("Non-negative integers up to n inclusive:")
print(test(n)) 
