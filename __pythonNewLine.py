'''A Python program to print without newline or space.'''
import functools

def printSolutionOne():
    for i in range(0, 10):
        print('*', end="")
 
def printSolutionTwo():
    printf = functools.partial(print, end="")
    for i in range(0, 10):
        printf('*')
        i = 0
   
def printSolutionThree(): 
    i=0;
    while i<10 :
        print('*',end='')
        i = i+1

def main ():
    printSolutionOne()
    #printSolutionTwo()
    #printSolutionThree()
    
main ()