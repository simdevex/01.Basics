'''
Write a Python program to find the lengths of a given list of non empty strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]
'''

#License: https://bit.ly/3oLErEI
def test(strs):
    '''
    map() is a built-in function that allows you to process and transform 
    all the items in an iterable without using an explicit for loop, a technique 
    commonly known as mapping. map() is useful when you need to apply a transformation 
    function to each item in an iterable and transform them into a new iterable.
    *map() the iterable returned from map() will be unpacked as arguments to the function. 
    That is, rather than calling the function and passing the iterable object as a single parameter, 
    the individual elements of the iterable are passed as individual parameters.

    '''
    #compact way to get lenghth of strings in a list.
    return [*map(len, strs)]

strs =  ['cat', 'car', 'fear', 'center']
print("Original strings:")
print(strs)
print("Lengths of the said list of non-empty strings:")
print(test(strs))
strs =  ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print("\nOriginal strings:")
print(strs)
print("Lengths of the said list of non-empty strings:")
print(test(strs))
