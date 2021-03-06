'''
Write a Python program that accept two strings and test if the
letters in the second string are present in the first string. 
Sample Input:
["python", "ypth"]
["python", "ypths"]
["python", "ypthon"]
["123456", "01234"]
["123456", "1234"]
Sample Output:
True
False
True
False
True
'''
#compare data between two strings
def string_letter_check(list_data):
      
      return all([char in list_data[0].lower() for char in list_data[1].lower()])

print(string_letter_check(["python", "ypth"]))
print(string_letter_check(["python", "ypths"]))
print(string_letter_check(["python", "ypthon"]))
print(string_letter_check(["123456", "01234"]))
print(string_letter_check(["123456", "1234"]))
print(string_letter_check(["123456", "456"]))
