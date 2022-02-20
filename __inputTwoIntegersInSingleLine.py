'''
Python program to input two integers in a single line.
'''
#Sample Solution-1
def inputTwoIntegerOptionOne ():
    print("Input the value of x & y separated by ,")
    x, y = map(int, input().split(','))
    print("The value of x & y are: ",x,y)

#Sample Solution 2
def inputTwoIntegerOptionTwo (): 
    a, b = [int(a) for a in input("Input the value of a & b: ").split(',')]
    print("The value of a & b are:",a,b)


def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : inputTwoIntegerOptionOne,
                  2 : inputTwoIntegerOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()