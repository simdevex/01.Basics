'''
Write a Python program to replace all but the last five
characters of a given string into "*" and returns the new masked
string.
Sample Input:
("kdi39323swe")
("12345abcdef")
("12345")
Sample Output:
******23swe
******bcdef
12345
'''

# masking example. Start from  end of first 5 and move backwards to beginning to mask first 5
# a[:-1] from the end move backwards by one digit
# a[-1:] from the first move backward by one digit
def mask_string(str1):
      return '*'*(len(str1)-5) + str1[-5:]

print(mask_string("kdi39323swe"))
print(mask_string("12345abcdef"))
print(mask_string("12345")) 
