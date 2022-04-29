'''
Python program find the longest string of a given list of strings.
Input:
['cat', 'car', 'fear', 'center']
Output:
center
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
shatter
[[0, 4], [1, 0], [1, 3], [4, 1]]
Input:
[([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2]
Output:
[[0, 1], [0, 3], [2, 2]]

'''

def test(words):
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
