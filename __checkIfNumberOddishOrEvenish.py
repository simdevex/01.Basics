'''
Write a Python program to check whether a given number is Oddish or Evenish.

A number is called "Oddish" if the sum of all of its digits is odd, and
a number is called "Evenish" if the sum of all of its digits is even.

Sample Input:
(120)
(321)
(43)
(4433)
(373)
Sample Output:
Oddish
Evenish
Oddish
Evenish
Oddish

'''

def oddish_evenish_num(n):
    '''
map() in Python is a function that works as an iterator and returns a 
list after applying a function to every item of an iterable 
(tuple, lists, string etc.). It is used when you want to apply a single 
transformation function to all the iterable elements
map(int, str(n)) converts each member of the string into an integer and 
returns a list of integers - default return type of map is a list
sum(map(int, str(n))) % 2 then sums all the integers in the list and checks 
if remainder is 0 when divided by 2. If remainder is 1, then Oddish, else Evenish (if remainder is 0) 

'''
    return 'Oddish' if sum(map(int, str(n))) % 2 else 'Evenish'

n = 120
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(120))
n = 321
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(321))
n = 43 
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(43))
n = 4433
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(4433))
n = 373
print("Original Number",n)
print("Check whether the sum of all digits of the said number is odd or even!")
print(oddish_evenish_num(373))
