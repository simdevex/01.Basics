'''
Write a Python program to generate and prints a list of numbers from 1 to 10.
Sample Input:
range(1,10)
Sample Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9]
['1', '2', '3', '4', '5', '6', '7', '8', '9']

'''

'''
Use of map() to execute a specific function
'''
nums = range(1,10)
print(list(nums))
print(list(map(str, nums)))
