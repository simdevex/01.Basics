def  getDifference (firstNum = 0.0 , secondNum  = 17.0):
    if firstNum > secondNum:
        return abs(2 * (float (firstNum) - float(secondNum)))
    else:
        return firstNum - secondNum
    
def main ():
    firstNum = input ("Enter the first number : ")
    secondNum = input ("Enter the second number : ")
    myResult = getDifference (firstNum, secondNum)
    print ("Result is : %s" %myResult)
    
main ()
        