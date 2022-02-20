'''
Python program to check if a number is positive, negative or zero.
'''

#Sample Solution 01
def checkNumberOptionOne (): 
    num = float(input("Input a number: "))
    if num > 0:
        print("It is positive number")
    elif num == 0:
        print("It is Zero")
    else:
        print("It is a negative number")

#Sample Solution 02
def checkNumberOptionTwo (): 
    n = float(input('Input a number: '))
    print('Number is Positive.' if n > 0 else 'It is Zero!' if n == 0 else 'Number is Negative.')

#Sample Solution 03
def checkNumberOptionThree (): 
    n = float(input("Input a number: "))
    if n >= 0:
        if n == 0:
            print("It is Zero!")
        else:
            print("Number is Positive number.")
    else:
        print("Number is Negative number.")

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : checkNumberOptionOne,
                  2 : checkNumberOptionTwo,
                  3 : checkNumberOptionThree,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()
   