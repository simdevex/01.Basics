'''
Python program find the strings in a given list containing
a given substring.
Input:
[(ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(o,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']
Input:
[(oe,('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
[]
'''

def test(strs, substr):
    #Compact return statement with a for loop. Simplified version of substring
    '''
    for s in strs:
        if substr in s:
            return s
    '''
    
    return [s for s in strs if substr in s]

strs =  ['cat', 'car', 'fear', 'center']
print("Original strings:")
print(strs)
substrs = 'ca'
print("Substring: "+substrs)
print("Strings in the said list containing a given substring:")
print(test(strs, substrs))
strs =  ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print("\nOriginal strings:")
print(strs)
substrs = 'o'
print("Substring: "+substrs)
print("Strings in the said list containing a given substring:")
print(test(strs, substrs))
strs =  ['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
print("\nOriginal strings:")
print(strs)
substrs = 'oe'
print("Substring: "+substrs)
print("Strings in the said list containing a given substring:")
print(test(strs, substrs))
