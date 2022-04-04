'''
Python program to empty a variable without destroying it.
'''
'''
Sample data: n=20
d = {"x":200}
Expected Output : 0 {}
'''
def emptyVariableOptionOne (): 
    n = 20
    d = {"x":200}
    l = [1,3,5]
    t= (5,7,8)
    print(type(n)())
    print(type(d)())
    print(type(l)())
    print(type(t)())

def Empty_Var(lst):
       return [type(i)() for i in lst]

def emptyVariableOptionTwo (): 

    lst = ["python",{"x":12},[10,12,"sfsd"], (4,5), 200]
    print("Original objects:")
    print(lst)
    print("\nEmpty the said variables without destroying it:")
    print(Empty_Var(lst))

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : emptyVariableOptionOne,
                  2 : emptyVariableOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()
