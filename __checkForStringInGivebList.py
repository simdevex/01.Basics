'''
Python program to check, for each string in a given list,
whether the last character is an isolated letter or not. 
Return True or
False.
Input:
['cat', 'car', 'fear', 'center']
Output:
[False, False, False, False]
Input:
['ca t', 'car', 'fea r', 'cente r']
Output:
[True, False, True, True]
'''

#License: https://bit.ly/3oLErEI

def test(strs):
    
    testList = []
    for s in strs:
        testList.append(len(s.split(" ")[-1]) == 1)
    return testList    
    
    #return [len(s.split(" ")[-1])==1 for s in strs]

strs =  ['cat', 'car', 'fear', 'center']
print("Original strings:")
print(strs)
print("Check, for each string in the said list, whether the last character is an isolated letter:")
print(test(strs))
strs =  ['ca t', 'car', 'fea r', 'cente r']
print("\nOriginal strings:")
print(strs)
print("Check, for each string in the said list, whether the last character is an isolated letter:")
print(test(strs))
