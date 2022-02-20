'''
Python program to check whether multiple variables have the same value
'''

def areVariablesEqualOptionOne():
    x = 20
    y = 20
    z = 20
    if x == y == z == 20:
        print("All variables have same value!")  
	
 
def areVariablesEqualOptionTwo(*vars):
   for x in vars:
       if x != vars[0]:
           return "All variables have not same value."
   return "All variables have same value."

print("Option One", areVariablesEqualOptionOne ())
print("Option Two", areVariablesEqualOptionTwo(2,3,2,2,2,2))
print("Option Two", areVariablesEqualOptionTwo(10,10,10,10))
print("Option Two", areVariablesEqualOptionTwo(-3,-3,-3,-3))  
