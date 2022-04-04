'''
Write a Python program to find the largest product of the pair of
adjacent elements from a given list of integers. 
Sample Input:
[1,2,3,4,5,6]
[1,2,3,4,5]
[2,3]
Sample Output:
30
20
6
'''

'''
The zip() function returns a zip object, which is an 
iterator of tuples where the first item in each passed iterator is paired together,
and then the second item in each passed iterator are paired together etc.
If the passed iterators have different lengths, the iterator with the least items decides 
the length of the new iterator.
iterables	can be built-in iterables (like: list, string, dict), or user-defined iterables
'''

def adjacent_num_product(list_nums):
    #create 2 tuples. The second tuple is right shifted and multiply the numbers
    return max(a*b for a, b in zip(list_nums, list_nums[1:]))

print(adjacent_num_product([1,2,3,4,5,6]))
print(adjacent_num_product([1,2,3,4,5]))
print(adjacent_num_product([2,3]))
