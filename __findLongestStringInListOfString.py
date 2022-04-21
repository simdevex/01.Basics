'''
Write a Python program find the longest string of a given list of
strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter
'''

def test(words):
    #compact return statement for longest string in a list
    
    '''
    max(iterable, *iterables, key, default)
    iterable - an iterable such as list, tuple, set, dictionary, etc.
    *iterables (optional) - any number of iterables; can be more than one
    key (optional) - key function where the iterables are passed and comparison is performed based on its return value
    default (optional) - default value if the given iterable is empty
    
    If one positional argument is provided, iterable must be a non-empty
    iterable (such as a non-empty string, tuple or list). 
    The largest item in the iterable is returned. 
    If two or more positional arguments are provided, the largest of the positional arguments is returned.
    The optional key argument specifies a one-argument ordering function like that used for list.sort(). 
    The key argument, if supplied, must be in keyword form (for example, max(a,b,c,key=func)).
    
    Other ways to do it max(len(w) for w in words)
    max(map(len, words))

    '''
    return  max(words, key=len) 

strs =  ['cat', 'car', 'fear', 'center']
print("Original strings:")
print(strs)
print("Longest string of the said list of strings:")
print(test(strs))
strs =  ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print("\nOriginal strings:")
print(strs)
print("Longest string of the said list of strings:")
print(test(strs))
