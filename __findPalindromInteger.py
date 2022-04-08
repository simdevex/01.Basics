'''
Python program to find the closest palindrome
number of a given integer. If there are two palindrome numbers in
absolute distance return the smaller number.
A palindromic number is a number that remains the same when its digits are reversed
Original number: 120
Closest Palindrome number of the said number: 121
Original number: 321
Closest Palindrome number of the said number: 323
Original number: 43
Closest Palindrome number of the said number: 44
Original number: 1234
Closest Palindrome number of the said number: 1221
'''

def test(n):
    x = n
    y = n
    while True:
        if str(x) == str(x)[::-1]:
            return x
        x -=  1
        if str(y) == str(y)[::-1]:
            return y
        y += 1
    return int(bin(n)[::-1][:-2], 2)

n = 120;
print("Original number: ", n);
print("Closest Palindrome number of the said number: ",test(n));
n = 321;
print("Original number: ", n);
print("Closest Palindrome number of the said number: ",test(n));
n = 43;
print("Original number: ", n);
print("Closest Palindrome number of the said number: ",test(n));
n = 1234;
print("Original number: ", n);
print("Closest Palindrome number of the said number: ",test(n));
