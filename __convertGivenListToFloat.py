'''
Python program to convert all items in a given list to
float values.
Original list:
['0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54', '0.54',
'0.55', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54']
List of Floats:
[0.49, 0.54, 0.54, 0.54, 0.54, 0.54, 0.55, 0.54, 0.54, 0.54, 0.55,
0.55, 0.55, 0.54, 0.55, 0.55, 0.54, 0.55, 0.55, 0.54]
'''

nums = ['0.49', '0.54', '0.54', '0.54', '0.54', '0.54', '0.55', '0.54', '0.54',  '0.54', 
 '0.55', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54', '0.55', '0.55', '0.54']

print("Original list:")
print(nums)
print("\nList of Floats:")
nums_of_floats = []
for item in nums:
    nums_of_floats.append(float(item))
print(nums_of_floats)
