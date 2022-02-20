'''
Python program to compute 
the future value of a specific principal amount, rate of interest, and a number of years
'''

def floatFutureValue (principal, interest, years):
    return round (float (principal * pow((1 + float(interest/100)), years)), 2)

def main ():
    a,b,c = [float(x) for x in input("Enter principal, interest, years values\n").split(',')]
    print ("Fuure value is:  ", floatFutureValue(a,b,c))
    
main ()

