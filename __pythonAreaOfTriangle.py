'''
Python program that will accept the base and height of atriangle and compute the area
'''

def calculateAreaOfTriangle (inputBase, inputHeight):
    localBase = float (inputBase)
    localHeight = float (inputHeight)
    
    return 0.5 * localBase * localHeight

def main ():
    mainBase = round(float(input ("Input base of triangle: ")), 2)
    mainHeight = round(float(input ("Input height of triangle: ")), 2)
    mainArea = calculateAreaOfTriangle (mainBase, mainHeight)
    print ("Area of triangle is :", round (mainArea, 2), sep =' ' )
    
main ()
    