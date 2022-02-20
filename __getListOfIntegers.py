'''
Python program to compute the product of a list of integers(without using for loop).
'''

#Sample Solution-1:
def getListOfIntegerOptionOne ():
    from functools import reduce
    nums = [10, 20, 30,]
    print("Original list numbers:")
    print(nums)
    '''
    The reduce(fun,seq) function is used to apply a particular function passed in its argument 
    to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

    Working :  

    At first step, first two elements of sequence are picked and the result is obtained.
    Next step is to apply the same function to the previously attained result and the number 
    just succeeding the second element and the result is again stored.
    This process continues till no more elements are left in the container.
    The final returned result is returned and printed on console.
    '''
    
    '''
    Add 10 to argument a, and return the result:

    x = lambda a : a + 10
    print(x(5))
    '''
    
    '''
    Multiply argument a with argument b and return the result:

    x = lambda a, b : a * b
    print(x(5, 6))
    '''
    
    nums_product = reduce( (lambda x, y: x * y), nums)
    print("\nProduct of the said numbers (without using for loop):",nums_product)


#Sample Solution-1:
def getListOfIntegerOptionTwo ():
    import math
    # Python version 3.9.
    nums = [10, 20, 30,]
    print("Original list numbers:")
    print(nums)
    nums_product = math.prod(nums)
    print("\nProduct of the said numbers (without using for loop):",nums_product)

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : getListOfIntegerOptionOne,
                  2 : getListOfIntegerOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()