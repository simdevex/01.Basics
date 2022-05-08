'''
Python program to find the indices of two numbers that sum to 0 in a given list of numbers.
Input:
[1, -4, 6, 7, 4]
Output:
[4, 1]
Input:
[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
Output:
[1, 7]

'''

#License: https://bit.ly/3oLErEI

def test(nums):
    s = set(nums)
    for i in s:
        if -i in s:
            # possible to return a list
            return [nums.index(i), nums.index(-i)]

nums = [1, -4, 6, 7, 4]
print("Original List:")
print(nums) 
print("Indices of two numbers that sum to 0 in the said list:")
print(test(nums))
nums=[1232, -20352, 12547, 12440, 741, 341, 525, 20352, 91, 20]
print("\nOriginal List:")
print(nums) 
print("Indices of two numbers that sum to 0 in the said list:")
print(test(nums)) 
