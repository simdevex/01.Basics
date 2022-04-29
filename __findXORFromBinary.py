'''
Python program to find the XOR of two given strings interpreted as binary numbers. 

Input:
['0001', '1011']
Output:
0b1010
Input:
['100011101100001', '100101100101110']
Output:
0b110001001111
'''

#License: https://bit.ly/3oLErEI
def test(nums):
    return bin(int(nums[0],2) ^ int(nums[1],2))

nums =  ["0001", "1011"]
print("Original strings:")
print(nums)
print("XOR of two said strings interpreted as binary numbers:")
print(test(nums))
nums =  ["100011101100001", "100101100101110"]
print("\nOriginal strings:")
print(nums)
print("XOR of two said strings interpreted as binary numbers:")
print(test(nums))