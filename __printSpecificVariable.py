'''
Given variables x=30 and y=20, write a Python program to print"30+20=50".
'''
def printOptionOne ():
    print ("Print Option 01")
    x = 30
    y = 20
    print("\n%d+%d=%d" % (x, y, x+y))
    print()

def printOptionTwo ():
    print ("Print Option 02")
    x = 30
    y = 20
    print("{0}+{1}={2}".format(x, y, x+y))

def printOptionThree ():
    print ("Print Option 03")
    x = 30
    y = 20
    print("{}+{}={}".format(x, y, x + y))
    
    
def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : printOptionOne,
                  2 : printOptionTwo,
                  3 : printOptionThree,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break
main()
