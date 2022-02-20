'''
A Python program to solve (x + y) * (x + y).
'''

def computeExpressions (x, y):
    return round (pow(float(x) + float(y), 2), 2)


def main ():
    a,b = [float(x) for x in input("Enter two values\n").split(',')]
    print ("Result ", computeExpressions(a,b))

main ()
