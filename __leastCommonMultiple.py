'''
Python program to get the Least Common Multiple (LCM) of more than two numbers. 
Take the numbers from a given list of positive integers. 

In arithmetic and number theory, the least common multiple, lowest
common multiple, or smallest common multiple of two integers a
and b, usually denoted by lcm(a, b), is the smallest positive integer
that is divisible by both a and b. Since division of integers by zero
is undefined, this definition has meaning only if a and b are both
different from zero. However, some authors define lcm(a,0) as 0
for all a, which is the result of taking the lcm to be the least upper
bound in the lattice of divisibility.
Original list elements: [4, 6, 8]
LCM of the numbers of the said array of positive integers: 24
Original list elements: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
LCM of the numbers of the said array of positive integers: 2520
Original list elements: [48, 72, 108]
LCM of the numbers of the said array of positive integers: 432
'''
from functools import reduce

def test(nums):
    return reduce(lambda x,y:lcm(x,y),nums)
# gcd()
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

# lcm()
def lcm(a, b):
    return a*b // gcd(a, b)

nums = [ 4, 6, 8 ]
print("Original list elements:")
print(nums)
print("LCM of the numbers of the said array of positive integers: ", test(nums))
nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print("\nOriginal list elements:")
print(nums)
print("LCM of the numbers of the said array of positive integers: ", test(nums))
nums = [ 48, 72, 108  ]
print("\nOriginal list elements:")
print(nums)
print("LCM of the numbers of the said array of positive integers: ", test(nums))
