'''a Python program that will return true if the two given integer values are equal or 
their sum or diff erence is 5.'''

def calculateDiff (inputNum01, inputNum02):
    localInt01 = int (inputNum01)
    localInt02 = int (inputNum02)
    if localInt01 == localInt02 or abs (localInt01 + localInt02) == 5 or abs (localInt01 + localInt02) == 5:
        return True
    else:
        return False
    
def main ():
    a,b = [int(x) for x in input("Enter two values\n").split(',')]
    print ("Two given integer values are equal or their sum or diff erence is 5 ", calculateDiff(a,b))

main ()