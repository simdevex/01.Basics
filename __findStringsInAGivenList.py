'''
Write a Python program to find the strings in a given list, starting with a given prefix.
Input:
[( ca,('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
Output:
['dog', 'donut']

'''

#License: https://bit.ly/3oLErEI

def test(strs, prefix):
    '''
    statList =[]
    for s in strs:
        if s.startswith(prefix) :
            statList.append (s)
    return statList
    '''
    #compact return statement
    return [s for s in strs if s.startswith(prefix)]

strs =  ['cat', 'car', 'fear', 'center']
prefix = "ca"
print("Original strings:")
print(strs)
print("Starting prefix:", prefix)
print("Strings in the said list starting with a given prefix:")
print(test(strs, prefix))

strs =  ['cat', 'dog', 'shatter', 'donut', 'at', 'todo']
prefix = "do"
print("\nOriginal strings:")
print(strs)
print("Starting prefix:", prefix)
print("Strings in the said list starting with a given prefix:")
print(test(strs, prefix))
