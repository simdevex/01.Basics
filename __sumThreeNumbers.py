
def calculateSum (firstNum = 0.0, secondNum = 0.0, thirdNum = 0.0):
    if firstNum == secondNum and firstNum == thirdNum and secondNum == thirdNum:
        return 3 * (firstNum + secondNum + thirdNum)
    else:
        return (firstNum + secondNum + thirdNum)
    
def main ():
    myFirstNum = input ("Enter first number : ")
    mySecondNum = input ("Enter second number : ")
    myThirdNum = input ("Enter third number : ")
    print("Sum of 3 numbers", calculateSum (float(myFirstNum), float(mySecondNum), float(myThirdNum) ))
    
main()