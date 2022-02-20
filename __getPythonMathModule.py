'''
Python program to get the details of math module.
'''

# Imports the math module
import math            

def getMathModuleOption01():
    #Sets everything to a list of math module
    math_ls = dir(math) # 
    print(math_ls)


def getMathModuleOption02():
    print("Details of math module:\n")
    help(math)
    
def main():
    getMathModuleOption01()
    getMathModuleOption02()
    
main ()