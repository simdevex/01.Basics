'''
Write a Python program that takes three integers and check whether the last digit 
of first number * the last digit of second number = the last digit of third number.

Sample Input:
(12, 22, 44)
(145, 122, 1010)
(0, 22, 40)
(1, 22, 40)
(145, 122, 101)
Sample Output:
True
True
True
False
False
'''

def check_last_digit(x, y, z):
      print ("Digit", str(x+y)[-1] )
      print ("Digit", str(z)[-1] )
      #Add integer, convert to string, slice from right to left
      return str(x+y)[-1] == str(z)[-1]

print(check_last_digit(12, 26, 44))
print(check_last_digit(145, 122, 1010))
print(check_last_digit(0, 20, 40))
print(check_last_digit(1, 22, 40))
print(check_last_digit(145, 129, 104))
