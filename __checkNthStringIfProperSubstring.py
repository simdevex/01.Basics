'''
Python program to check the nth-1 string is a proper
substring of nth string in a given list of strings
Count the total number of strings in a list, and then the 2nd last string is a subset of last string
Input:
['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
Output:
True
Input:
['a', 'abb', 'sfs', 'oo', 'ee', 'sfde']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwrew']
Output:
False
Input:
['a', 'abb', 'sad', 'ooaaesdfe', 'sfsdfde', 'sfsd', 'sfsdf', 'qwsfsdfrew']
Output:
True
'''

#License: https://bit.ly/3oLErEI

def test(str1):
    #Advance string manipulation in return statement
    return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]

str11 = ["a","abb","sfs", "oo", "de", "sfde"]
print("Original list:")
print(str11)
print("Check the nth-1 string is a proper substring of nth string of the said list of strings:")
print(test(str11))
str11 = ["a","abb","sfs", "oo", "ee", "sfde"]
print("\nOriginal list:")
print(str11)
print("Check the nth-1 string is a proper substring of nth string of the said list of strings:")
print(test(str11))
str11 = ["a","abb","sad", "ooaa" "esdfe", "sfsdfde", "sfsd", "sfsdf", "qwrew"]
print("\nOriginal list:")
print(str11)
print("Check the nth-1 string is a proper substring of nth string of the said list of strings:")
print(test(str11)) 
str11 = ["a","abb","sad", "ooaa" "esdfe", "sfsdfde", "sfsd", "sfsdf", "qwsfsdfrew"]
print("\nOriginal list:")
print(str11)
print("Check the nth-1 string is a proper substring of nth string of the said list of strings:")
print(test(str11))
