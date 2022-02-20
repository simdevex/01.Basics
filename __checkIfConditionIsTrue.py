'''
Python program to perform an action if a condition is true
Given a variable name, if the value is 1, display the string 
"First day of aMonth!" and do nothing if the value is not equal.
'''

def processOptionOne ():
    print ("Print Option 01")
    n=1
    if n == 1:
        print("\nFirst day of a Month!")
        print()

def processOptionTwo ():
    print ("Print Option 02")
    n = float(input("Input a number: "))
    if (n == 1):
        print("First day of a Month!")
    else:
        print()

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : processOptionOne,
                  2 : processOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break
main()