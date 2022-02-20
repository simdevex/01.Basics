'''
Python program to add leading zeroes to a string.
'''

#Sample Solution-1:
def addLeadingZeroOptionOne ():
    str1='122.22'
    print("Original String: ",str1)
    print("\nAdded trailing zeros:")
    str1 = str1.ljust(8, '0')
    print(str1)
    str1 = str1.ljust(10, '0')
    print(str1)
    print("\nAdded leading zeros:")
    str1='122.22'
    str1 = str1.rjust(8, '0')
    print(str1)
    str1 = str1.rjust(10, '0')
    print(str1)

#Sample Solution-2:
#'<': Forces the field to be left-aligned within the available space (this is the default for most objects).
#'>': Forces the field to be right-aligned within the available space (this is the default for numbers).
def addLeadingZeroOptionTwo():
    str1='122.22'
    print("Original String: ",str1)
    print("\nAdded trailing zeros:")
    f_text = '{:<08}'
    str1 = f_text.format(str1)
    print(str1)
    f_text = '{:<010}'
    str1 = f_text.format(str1)
    print(str1)
    print("\nAdded leading zeros:")
    str1='122.22'
    f_text = '{:>08}'
    str1 = f_text.format(str1)
    print(str1)
    f_text = '{:>010}'
    str1 = f_text.format(str1)
    print(str1)

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : addLeadingZeroOptionOne,
                  2 : addLeadingZeroOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()