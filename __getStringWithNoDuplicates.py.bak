'''
Python program to create a new string with no
duplicate consecutive letters from a given string. Go to the editor
Sample Input:
("PPYYYTTHON")
("PPyyythonnn")
("Java")
("PPPHHHPPP")
Sample Output:
PYTHON
Python
Java
PHP

'''

def no_consecutive_letters (txt):
    # create a string by iterating over a string, and if you don't find consecutive duplicates
    # And if you do find duplicates then remove it
    return txt[0] + ''.join(txt[i] for i in range(1,len(txt)) if txt[i] != txt[i-1])

print(no_consecutive_letters("PPYYYTTHON"))
print(no_consecutive_letters("PPyyythonnn"))
print(no_consecutive_letters("Java"))
print(no_consecutive_letters("PPPHHHPPP")) 
