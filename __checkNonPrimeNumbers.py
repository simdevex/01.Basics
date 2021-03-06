'''
Write a Python program to identify nonprime numbers between 1 to 100 (integers). Print the nonprime numbers. 
Sample Input:
range(1, 101)
Sample Output:
Nonprime numbers between 1 to 100:
4
6
8
9
10
..
96
98
99
100
'''

import math
def is_not_prime(n):
    ans = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            ans = True
    return ans

print("Nonprime numbers between 1 to 100:")
for x in filter(is_not_prime, range(1, 101)):
    print(x)
