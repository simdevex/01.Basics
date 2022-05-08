'''
Write a Python program to compute the product of the odd digits in a given number, or 0 if there aren't any. 
Input: 123456789
Output:
945 Input: 2468
Output:
0 Input: 13579
Output:
945
'''

#License: https://bit.ly/3oLErEI

def test(n):
    if any(int(c) % 2 for c in str(n)):
        prod = 1
        for c in str(n):
            if int(c) % 2 == 1:
                prod *= int(c)
        return prod
    return 0

n = 123456789
print("Original Number:",n)
print("Product of the odd digits in the said number, or 0 if there aren't any")
print(test(n))
n = 2468
print("\nOriginal Number:",n)
print("Product of the odd digits in the said number, or 0 if there aren't any")
print(test(n))
n = 13579
print("\nOriginal Number:",n)
print("Product of the odd digits in the said number, or 0 if there aren't any")
print(test(n))
