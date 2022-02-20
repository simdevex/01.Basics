import math

def getVolume (radius = 0.0):
    return 4/3 * math.pi * pow (radius, 3)

def getRadius():
    return float(input("Enter radius : "))

def main ():
    myRadius = getRadius()
    print ("Sphere volume :", round(getVolume (myRadius), 2) , sep = ' ')
    
main ()