'''
Write a Python program to compute the sum of the three
lowest positive numbers from a given list of numbers. 
Sample Input:
[10, 20, 30, 40, 50, 60, 7]
[1, 2, 3, 4, 5]
[0, 1, 2, 3, 4, 5]
Sample Output:
37
6
6
'''

def sum_three_smallest_nums(lst):
        # [:3] means sort from lowest to highest and get first three lowest possible
        # Then sum
    	return sum(sorted([x for x in lst if x > 0])[:3])

print(sum_three_smallest_nums([10, 20, 30, 40, 50, 60, 7]))
print(sum_three_smallest_nums([1, 2, 3, 4, 5]))
print(sum_three_smallest_nums([0, 1, 2, 3, 4, 5]))
