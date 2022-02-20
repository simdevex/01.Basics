'''
Python program to round a fl oating-point number to specifi ednumber decimal places
'''

#Sample Solution-1:
def setListOfIntegerOptionOne (order_amt):   
    print('\nThe total order amount comes to %f' % float(order_amt))
    print('The total order amount comes to %.2f' % float(order_amt))
    print()

def setListOfIntegerOptionTwo (order_amt):  
    print("\nThe total order amount comes to {:0.6f}".format(float(order_amt)))
    print("\nThe total order amount comes to {:0.2f}".format(float(order_amt)))

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    impNumber = float (input ("Input a number"))
    #Use dictionary instead of switch case
    selection = { 1 : setListOfIntegerOptionOne,
                  2 : setListOfIntegerOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key](impNumber)
            break

main ()