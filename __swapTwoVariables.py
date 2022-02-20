'''
Python program to swap two variables
'''
def swapUsingOptionOne (a, b):
    print("\nBefore swap a = %d and b = %d" %(a, b))
    a, b = b, a
    print("\nAfter swaping a = %d and b = %d" %(a, b))
    print()

def sampleUsingOptionTwo (a, b):
    print("Initial Value of x =", a)
    print("Initial Value of y =", b)
    temp = a
    a = b
    b = temp
    print("\nAfter swaping value of x =", a)
    print("After swaping value of y =", b) 

def main ():
    
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    numberOne = int (input ("Input the frst number\n"))
    numberTwo = int (input ("Input the second number\n"))
    
    #Use dictionary instead of switch case
    selection = { 1 : swapUsingOptionOne,
                  2 : sampleUsingOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key](numberOne, numberTwo)
            break
main()
