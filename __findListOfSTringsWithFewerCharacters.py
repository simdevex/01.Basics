'''
Write a Python program to find the list of strings that has fewer total characters (including repetitions).
Input:
[['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
Output: ['this', 'list', 'is', 'narrow']
Input:
[['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
Output:
['Red', 'Black', 'Pink']
'''

#License: https://bit.ly/3oLErEI

def test(strs):
    #multi-dimensional string manimulation using lambda
    return min(strs, key=lambda x: sum(len(i) for i in x)) 

strs = [['this', 'list', 'is', 'narrow'], ['I', 'am', 'shorter but wider']]
print("Original List:")
print(strs) 
print("\nFind the given list of strings that has fewer total characters:")
print(test(strs))
strs = [['Red', 'Black', 'Pink'], ['Green', 'Red', 'White']]
print("\nOriginal List:")
print(strs) 
print("\nFind the given list of strings that has fewer total characters:")
print(test(strs))
