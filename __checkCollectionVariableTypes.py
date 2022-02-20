'''
Python program to test if a variable is a list or tuple or a set.
'''

#Sample Solution-1:

#x = ['a', 'b', 'c', 'd']
#x = {'a', 'b', 'c', 'd'}
def checkCollectioTypeOptionOne ():
    x = ('tuple', False, 3.2, 1)
    if type(x) is list:
        print('x is a list')
    elif type(x) is set:
        print('x is a set')
    elif type(x) is tuple:
        print('x is a tuple')    
    else:
        print('Neither a list or a set or a tuple.')


#Sample Solution-2:
def check_type(nums):
    if isinstance(nums, tuple)==True:
        return 'The variablex is a tuple'
    elif isinstance(nums, list)==True:
        return 'The variablex is a list'
    elif isinstance(nums, set)==True:
        return 'The variablex is a set'
    else:
        return 'Neither a list or a set or a tuple.'

def checkCollectioTypeOptionTwo ():
    x = ['a', 'b', 'c', 'd']
    print(check_type(x))
    x = {'a', 'b', 'c', 'd'}
    print(check_type(x))
    x = ('tuple', False, 3.2, 1)
    print(check_type(x))
    x = 100
    print(check_type(x))

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : checkCollectioTypeOptionOne,
                  2 : checkCollectioTypeOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()

