'''
Python program to select a string from a given list of strings with the most unique characters. 

Input:
['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo',
'unique']
Output:
abcdefhijklmnop
Input:
['Green', 'Red', 'Orange', 'Yellow', '', 'White']
Output:
Orange

'''

#License: https://bit.ly/3oLErEI
def test(strs):
    '''
    A great use of reducing multiple lines of code into a single line using set and lambda
    set removes any duplicates and gets the maximium unique charecters
    key=lambda x: len(set(x)) is a lambda function returns a the length of a string with unique characters
    '''
    return max(strs, key=lambda x: len(set(x)))

strs = ['cat', 'catatatatctsa', 'abcdefhijklmnop', '124259239185125', '', 'foo', 'unique']
print("Original list:")
print(strs)
print("Select a string from the said list of strings with the most unique characters:")
print(test(strs))
strs = ['Green', 'Red', 'Orange', 'Yellow', '', 'White']
print("\nOriginal list:")
print(strs)
print("Select a string from the said list of strings with the most unique characters:")
print(test(strs))

