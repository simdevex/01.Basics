'''
Python program to check whether the average value
of the elements of a given array of numbers is a whole number or not. 
Original array:
1 3 5 7 9
Check the average value of the elements of the said array is a
whole number or not: True
Original array:
2 4 2 6 4 8
Check the average value of the elements of the said array is a
whole number or not:
False

'''

import array as arr
def test(nums):
    return sum(nums) % len(nums) == 0

#aar.array first parameter is a code which gives the type of array, for example i is signed int
array_num = arr.array('i', [1, 3, 5, 7, 9])
print("Original array:")

for i in range(len(array_num)):    
    print(array_num[i], end=' ')

print("\nCheck the average value of the elements of the said array is a whole number or not:\n",test(array_num))
array_num = arr.array('i', [2, 4, 2, 6, 4, 8])
print("\nOriginal array:")

for i in range(len(array_num)):    
    print(array_num[i], end=' ')

print("\nCheck the average value of the elements of the said array is a whole number or not:\n",test(array_num)) 
