'''
Python program to compute the summation of the absolute difference of all distinct pairs
in a given array (nondecreasing order).
'''

def sum_distinct_pairs (arr):
    result = 0 
    i = 0
    while i < len(arr):
        result += i*arr [i] - (len (arr) - i -1 ) * arr [i]
        print (arr)
        print (result)
        i += 1 
    return result

print (sum_distinct_pairs ([1,2,3]))
print (sum_distinct_pairs([1,4,5]))
print (sum_distinct_pairs([1,4,8,9]))