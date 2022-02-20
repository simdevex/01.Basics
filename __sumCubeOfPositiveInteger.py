'''
Python function that takes a positive integer and 
returns the sum of the cube of all the positive integers smaller than the specified number.
Ex.: 8 = 7^3 + 6^3 + 5^3 + 4^3 + 3^3 + 2^3 + 1^3 = 784
'''

#Sample Solution-1:
def sum_of_cubes_first(n):
    n -= 1
    total = 0
    while n > 0:
        total += n * n * n
        n -= 1
    return total

def getSumOfCubesOptionOne():
    print("Sum of cubes smaller than the specified number: ",sum_of_cubes_first(8))

#Sample Solution-2:
def sum_of_cubes_second(n):
    if n < 0:
        raise ValueError('n must be positive number!')
    return n * n * ((n * n) - (2 * n) + 1) / 4

def getSumOfCubesOptionTwo():
    print("Sum of cubes smaller than the specified number: ",sum_of_cubes_second(3))
    print("Sum of cubes smaller than the specified number: ",sum_of_cubes_second(8))

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : getSumOfCubesOptionOne,
                  2 : getSumOfCubesOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()

