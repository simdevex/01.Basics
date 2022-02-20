def testNumberRange(inputNum = '0'):
    
    if abs (float(inputNum) - 1000) < 100:
        return "is within 100 of 1000"
    elif abs (float(inputNum) - 2000) < 100:
         return "is within 100 of 2000"
    else:
        return "is not within 100 of 1000 OR 2000"
        
def main ():
    
    myNum = input ("Enter a number : ")
    print("Number", testNumberRange(myNum))
    
main ()  