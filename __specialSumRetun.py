'''
A Python program to sum of two given integers. However, if thesum is between 15 to 20 it will return 20.
'''

def getSumSpecial (inputNum01, inputNum02):
    
    sumNum = int(inputNum01) + int(inputNum02)
    if 20 > sumNum  and sumNum > 15:
        return 20
    else:
        return sumNum
    
    
def main ():
    #special for loop forming a list, and returning more than one variables
    a,b = [int(x) for x in input("Enter two values\n").split(',')]
    print ("Sum is : ", getSumSpecial(a,b))

main ()