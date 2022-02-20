def calcMultipleSum(strVal = 0):
    n1 = int( "%s" % strVal )
    n2 = int( "%s%s" % (strVal,strVal) )
    n3 = int( "%s%s%s" % (strVal,strVal,strVal) )
    return (n1+n2+n3)

def main ():
    inputVal = input("Input an integer : ")
    rintVal = calcMultipleSum (inputVal)
    print (rintVal)
    
main ()

