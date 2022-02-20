'''
A Python program to get the least common multiple (LCM) oftwo positive integers
'''

from functools import reduce
from math import gcd

def lcmCalculate (inputNum1, inputNum2, lcmOption = 1):
    lInputNum1 = int (inputNum1)
    lInputNum2 = int (inputNum2)
 
    if int(lcmOption) == 1:
        print ("In option 1 ")
        return lcmMethodOne (lInputNum1, lInputNum2)
    elif int(lcmOption) == 2:
        inputNum = list ([inputNum1, inputNum2])
        return lcmMethodTwo (inputNum)
    elif int(lcmOption) == 3:
        return lcmMethodThree (lInputNum1, lInputNum2)
    else:
        return 0

# Method 1 
def lcmMethodOne(x, y):
    if x > y:
        z = x
    else:
        z = y
        while(True):
            if((z % x == 0) and (z % y == 0)):
                lcm = z
                break
            z += 1
    return lcm

# Method 2
def lcmMethodTwo(numbers):
      return reduce((lambda x, y: int(x * y / gcd(x, y))), numbers)

# Method 3 - The product of the HCF and LCM of two numbers is equal to the product of the two numbers.
def lcmMethodThree(a, b):
     return (a * b) // gcd(a,b) 


def main():
    lcmOption = input ("Select the calculation option") 
    a, b = [int(x) for x in input("Enter two values\n").split(', ')]
    lcmValue = lcmCalculate (a, b, lcmOption)
    print ("LCM value is : ", lcmValue )


main ()