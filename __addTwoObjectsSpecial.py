'''
A Python program to add two objects if both objects are an integer type.
'''
def areObjectsInteger (inputNum01, inputNum02):

    if not (isinstance(inputNum01, int) and isinstance(inputNum02, int)):
        return False
    return inputNum01 + inputNum02
    
def main ():
    a,b = [float(x) for x in input("Enter two values\n").split(',')]
    print ("Given both objects are integer type? ", areObjectsInteger(a,b))

main ()