'''
Python program to sort the numbers of a given list by the sum of their digits.
Input: [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Output:
[10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]
Input: [23, 2, 9, 34, 8, 9, 10, 74]
Output:
[10, 2, 23, 34, 8, 9, 9, 74]
'''
#License: https://bit.ly/3oLErEI

def test(nums):
     return sorted(nums, key=lambda n: sum(int(c) for c in str(n) if c != "-"))
 
nums = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Original list of numbers:",nums)
print("Sort the numbers of the said list by the sum of their digits:")
print(test(nums))
nums = [23,2,9,34,8,9,10,74]
print("\nOriginal list of numbers:",nums)
print("Sort the numbers of the said list by the sum of their digits:")
print(test(nums))
