'''
Write a Python program to check if two given numbers are Co
Prime or not. Return True if two numbers are Co Prime otherwise
return false. Go to the editor
Sample Input:
(17, 13)
(17, 21)
(15, 21)
(25, 45)
Sample Output:
True
True
False
False

'''

def gcd(p,q):
    # Create the gcd of two positive integers.
    while q != 0:
        #GCD shorthand code - pick the first (highest) number that divides the number
        #Assignment operator can handle multiple variables
        p, q = q, p%q
        print ('p', p)
        print ('q', q)
    return p
def is_coprime(x, y):
    return gcd(x, y) == 1

print(is_coprime(17, 13))
print(is_coprime(17, 21))
print(is_coprime(15, 21))
print(is_coprime(25, 45))
