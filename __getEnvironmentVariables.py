'''A python program to access environment variables.'''

import os
import os.path

# Access all environment variables 
def printEnvVar_01():
    print('*----------------------------------*')
    print(os.environ)
    print('*----------------------------------*')
    # Access a particular environment variable 
    print(os.environ['HOME'])
    print('*----------------------------------*')
    print(os.environ['PATH'])
    print('*----------------------------------*')

def printEnvVar_02():
    
    for data in os.environ:
        print(data)
        print('-'*15)
        print(os.environ[data])
        print('='*30)

def printEnvVar_03(): 
    for item, value in os.environ.items():
        print('{}: {}'.format(item, value))


def main ():
    myOption = input ("Select an option : ")
    
    if int(myOption) == 1: 
        printEnvVar_01()
    elif int(myOption) == 2:
        printEnvVar_02()
    elif int(myOption) == 3:
        printEnvVar_03()
    else:
        print ("Invalid Option")
        
main ()