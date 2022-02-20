'''a Python program to compute the greatest common divisor(GCD) of two positive integers'''
from functools import reduce
from math import gcd as _gcd

def gcdCalculate (inputNum1, inputNum2, gcdOption = 1):
    lInputNum1 = int (inputNum1)
    lInputNum2 = int (inputNum2)
 
    if int(gcdOption) == 1:
        print ("In option 1 ")
        return gcdMethodOne (lInputNum1, lInputNum2)
    elif int(gcdOption) == 2:
        return gcdMethodTwo (lInputNum1, lInputNum2)
    elif int(gcdOption) == 3:
        return gcdMethodThree (lInputNum1, lInputNum2)
    else:
        return 0
    
def gcdMethodOne(x, y):
    gcd = 1   
    if x % y == 0:
        return y   
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
           gcd = k
           break 
    return gcd

def gcdMethodTwo(x, y):
    z = x % y
    while z:
        x = y
        y = z
        z = x % y
    return y

def gcdMethodThree(nums):
      return reduce(_gcd, nums)

def main ():
    
    gcdOption = input ("Select the calculation option") 
    a, b = [int(x) for x in input("Enter two values\n").split(', ')]
    gcdValue = gcdCalculate (a, b, gcdOption)
    print ("GCD value is : ", gcdValue )
    
main ()
