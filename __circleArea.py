import math

def calculateArea(r = 0.0):
    area = 2 * math.pi * r
    return area

def getRaidus():
    return input ("Enter the radius of circle : ")
    
def main():
    radius =  float(getRaidus())
    print ("Area of the circle is: ", round (calculateArea (radius), 2))

main()