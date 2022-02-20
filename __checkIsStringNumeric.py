'''
Python program to check whether a string is numeric.
'''
def isStringNumericOption1(inputStr):
    inputStr = 'a123'
    #str = '123'
    try:
        i = float(inputStr)
    except (ValueError, TypeError):
        print('\nNot numeric')
    print()


def isStringNumericOption2(inputStr):
    # Doesn't work for floats
    inputStr = input("Input a word or numbers: ")
    if inputStr.isdigit():
        print("The input value is numbers.")
    else:
        print("The input value is string.")

def main ():
    
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case

    inputStr = input("Input a word or numbers: ")
    selection = { 1 : isStringNumericOption1,
                  2 : isStringNumericOption2,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key](inputStr)
            break
        
        
main ()