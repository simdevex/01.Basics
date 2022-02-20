'''
Python program to split a variable length string into variables
'''
#Sample Solution-1:
def splitStringIntoVariablesOne ():
    #You have a list. Length of list can vary. If you want to store value in three variables.
    var_list = ['a', 'b', 'c']
    x, y, z = (var_list + [None] * 3)[:3]
    print(x, y, z)
    var_list = [100, 20.25]
    x, y = (var_list + [None] * 2)[:2]
    print(x, y)

#Sample Solution-2:
def splitStringIntoVariablesTwo ():
    var_list = ['a', 'b', 'c', 'd', 'e']
    v, w, x, y, z = var_list
    print(v, w, x, y, z)

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : splitStringIntoVariablesOne,
                  2 : splitStringIntoVariablesTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()
