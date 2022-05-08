'''
Write a Python program to rescale and shift numbers of a given list, so that they cover the range [0, 1].
Input:
[18.5, 17.0, 18.0, 19.0, 18.0]
Output:
[0.75, 0.0, 0.5, 1.0, 0.5]
Input:
[13.0, 17.0, 17.0, 15.5, 2.94]
Output:
[0.7155049786628734, 1.0, 1.0, 0.8933143669985776, 0.0]

'''

def test(nums):
    a = min(nums)
    b = max(nums)
    if b - a == 0:
        return [0.0] + [1.0] * (len(nums) - 1)
    for i in range(len(nums)):
        nums[i] = (nums[i] - a) / (b - a)
    return nums

nums = [18.5, 17.0, 18.0, 19.0, 18.0]
print("Original list:")
print(nums)
print("Rescale and shift the numbers of the said list so that they cover the range [0, 1]:")
print(test(nums))
nums = [13.0, 17.0, 17.0, 15.5, 2.94]
print("\nOriginal list:")
print(nums)
print("Rescale and shift the numbers of the said list so that they cover the range [0, 1]:")
print(test(nums))
