'''
Python program to sum of three given integers. However, iftwo values are equal sum will be zero
'''
def calculateSum (inputNum01, inputNum02, inputNum03 ):
    
    if inputNum01 == inputNum02  or inputNum01 == inputNum03 or inputNum02 == inputNum03:
        return 0
    else: 
        return inputNum01 + inputNum02 + inputNum03

def main ():
    a,b,c = [int(x) for x in input("Enter two values\n").split(',')]
    print ("Sum is : ", calculateSum(a,b,c))

main ()