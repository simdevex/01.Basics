'''
Python program to find x that minimizes mean squared deviation from a given a list of numbers.

Input:
[4, -5, 17, -9, 14, 108, -9]
Output:
17.142857142857142
Input:
[12, -2, 14, 3, -15, 10, -45, 3, 30]
Output:
1.1111111111111112

Squared deviations from the mean (SDM) are involved in various calculations. In probability theory
and statistics, the definition of variance is either the expected value of the SDM (when considering 
a theoretical distribution) or its average value (for actual experimental data). Computations for 
analysis of variance involve the partitioning of a sum of SDM.
The problem requires minimizing the sum of squared deviations, which turns out to be the mean mu. 
Moreover, if mu is the mean of the numbers then a simple calculation.
'''

#License: https://bit.ly/3oLErEI

def test(nums):
    return sum(nums) / len(nums) 

nums = [4, -5, 17, -9, 14, 108, -9]
print("Original list:")
print(nums)
print("Minimizes mean squared deviation from the said list of numbers:")
print(test(nums))
nums = [12, -2, 14, 3, -15, 10, -45, 3, 30]
print("Original list:")
print(nums)
print("Minimizes mean squared deviation from the said list of numbers:")
print(test(nums))
