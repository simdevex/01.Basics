'''
Python program to find the number of zeros at the end of a factorial of a given positive number
'''

def factendzero (n):
    factorial = 1
    x = n // 5
    y = x
    if n < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,n + 1):
            factorial = factorial*i
    print("The factorial of",n,"is",factorial)
    
    while x > 0:
        x /= 5
        y += int (x)
    return y

print (factendzero (5))
print (factendzero (12))
print (factendzero (100))
    