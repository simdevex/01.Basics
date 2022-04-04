'''
Python program to get the index number of all lower case letters in a given string
Original string: Python
Indices of all lower case letters of the said string: [1, 2, 3, 4, 5]
Original string: JavaScript
Indices of all lower case letters of the said string: [1, 2, 3, 5, 6, 7, 8,9] Original string: PHP
Indices of all lower case letters of the said string: []
'''

def test(text):
    #single line of return statement with for
    return [x for x in range(len(text)) if text[x].islower()]

text = "Python";
print("Original string:",text)
print("Indices of all lower case letters of the said string:\n",test(text))

text = "JavaScript";
print("Original string:",text)
print("Indices of all lower case letters of the said string:\n",test(text))

text = "PHP";
print("Original string:",text)
print("Indices of all lower case letters of the said string:\n",test(text))
