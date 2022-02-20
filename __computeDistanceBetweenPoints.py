'''
A Python program to compute the distance between the points
'''
import math

def computeDistanceBetweenPoints (point1, point2):
    return math.sqrt ((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2)

def main():

    mainPoint1 = tuple (float(x) for x in input("Enter first point\n").split(','))
    mainPoint2 = tuple (float(x) for x in input("Enter second point\n").split(','))
    print ("Distance is  ", computeDistanceBetweenPoints(mainPoint1,mainPoint2))

main()