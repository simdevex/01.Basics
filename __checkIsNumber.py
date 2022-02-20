'''
Python program to input a number, if it is not a number generates an error message.
'''
#Sample Solution 01
def isNumberErrorOptionOne ():
    while True:
        try:
            a = int(input("Input a number: "))
            break
        except ValueError:
            print("\nThis is not a number. Try again...")
            print()

#Sample Solution 02
def isNumberErrorOptionTwo ():
    x = 1.23
    x_int = x.is_integer()
    print("Check if x is an integer!")
    print(x_int)
    y= 1.0
    y_int = y.is_integer()
    print("Check if y is an integer!")
    print(y_int)  

#Sample Solution 03
def isNumberErrorOptionThree ():
    x = 1.0
    x_int = isinstance(x, int)
    print("Check if x is an integer!")
    print(x_int)
    y = 1
    y_int = isinstance(y, int)
    print("Check if y is an integer!")
    print(y_int)

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : isNumberErrorOptionOne,
                  2 : isNumberErrorOptionTwo,
                  3 : isNumberErrorOptionThree,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()