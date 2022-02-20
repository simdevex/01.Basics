'''
Python program to remove the first item from a specified list
'''

def removeItemFromListOptionOne():
    color = ["Red", "Black", "Green", "White", "Orange"]
    print("Original list elements:")
    print(color)
    del color[0]
    print("After removing the first color:")
    print(color)

def removeItemFromListOptionTwo ():
    color = ["Red", "Black", "Green", "White", "Orange"]
    print("Original list elements:")
    print(color)
    print("\nAfter removing the first element from the said list:")
    new_color = color[1:]
    print(new_color)
    
def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : removeItemFromListOptionOne,
                  2 : removeItemFromListOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()