'''
Python program to find the sum of the numbers of a
given list among the first k with more than 2 digits.
Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
Value of K: 4
Output:
0
Input: [4, 5, 17, 9, 14, 108, -9, 12, 76]
Value of K: 6
Output:
108
Input: [114, 215, -117, 119, 14, 108, -9, 12, 76]
Value of K: 5
Output:
331
Input: [114, 215, -117, 119, 14, 108, -9, 12, 76]
Value of K: 1
Output:
114
'''

#License: https://bit.ly/3oLErEI

def test(nums, k):
    s = 0
    for i in range(len(nums))[:k]:
        if len(str(abs(nums[i])))>2:
            s = s + nums[i]
    return s

nums = [4, 5, 17, 9, 14, 108, -9, 12 ,76]
print("Original list:",nums)
K = 4
print("Value of K:",K)
print("sum of the numbers among the first k with more than 2 digits")
print(test(nums, K))
nums = [4, 5, 17, 9, 14, 108, -9, 12 ,76]
print("\nOriginal list:",nums)
K = 6
print("Value of K:",K)
print("sum of the numbers among the first k with more than 2 digits")
print(test(nums, K))
nums = [114, 215, -117, 119, 14, 108, -9, 12 ,76]
print("\nOriginal list:",nums)
K = 5
print("Value of K:",K)
print("sum of the numbers among the first k with more than 2 digits")
print(test(nums, K)) 
print("\nOriginal list:",nums)
K = 1
print("Value of K:",K)
print("sum of the numbers among the first k with more than 2 digits")
print(test(nums, K))  
