'''
Python program to print a variable without spaces between values.
Sample value : x =30
Expected output : Value of x is "30"
'''
#Sample Solution-1:
def getValueUsingFormat(x):
    print('Value of x is "{}"'.format(x))

#Sample Solution-2:
def getValueUsingAmpersand(x):
    print("Value of x is \"%i\"" % x)

#Sample Solution-3:
def getValueUsingBackslash(x):
    print("Value of x is "+'\"' + str(x) + '\"')


def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|\n"))
    inpVal = int (input ("Pick a number:\n"))
    #Use dictionary instead of switch case
    selection = { 1 : getValueUsingFormat,
                  2 : getValueUsingAmpersand,
                  3 : getValueUsingBackslash,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key](inpVal)
            break

main ()

