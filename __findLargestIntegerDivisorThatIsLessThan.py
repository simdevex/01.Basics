'''
Python program to find the largest integer divisor of a number n that is less than n.
Input: 18
Output:
9
Input: 100
Output:
50
Input: 102
Output:
51
Input: 500
Output:
250
Input: 1000
Output:
500
Input: 6500
Output:
3250
'''

#License: https://bit.ly/3oLErEI

def test(n):
     return next(d for d in range(n - 1, 0, -1) if n % d == 0)
 
n = 18
print("Original number:",n)
print("Largest integer divisor of a number n that is less than n:")
print(test(n))
n = 100
print("Original number:",n)
print("Largest integer divisor of a number n that is less than n:")
print(test(n))
n = 102
print("Original number:",n)
print("Largest integer divisor of a number n that is less than n:")
print(test(n))
n = 500
print("Original number:",n)
print("Largest integer divisor of a number n that is less than n:")
print(test(n))
n = 1000
print("Original number:",n)
print("Largest integer divisor of a number n that is less than n:")
print(test(n))
n = 6500
print("Original number:",n)
print("Largest integer divisor of a number n that is less than n:")
print(test(n))
