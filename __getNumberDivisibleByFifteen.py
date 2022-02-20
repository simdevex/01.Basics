'''
Python program to get numbers divisible by fi fteen from alist using an anonymous function.
'''

#Sample Solution 01
def getNumbersOptionOne ():
    num_list = [45, 55, 60, 37, 100, 105, 220]
    # use anonymous function to filter
    result = list(filter(lambda x: (x % 15 == 0), num_list))
    print("Numbers divisible by 15 are",result)

#Sample Solution 02
def getNumbersOptionTwo ():
    num_list = [45, 55, 60, 37, 100, 105, 220]
    print("Original list:",num_list)
    # use anonymous function to filter
    result = list(filter(lambda x: (x % 15 == 0), num_list))
    print("Numbers of the said list divisible by 15 are:",result)

#Sample Solution 03
def getNumbersOptionThree ():
    num_list = [45, 55, 60, 37, 100, 105, 220]
    print("Original list:",num_list)
    print("\nNumbers of the said list divisible by 15 are:")
    print(str(''.join(filter(lambda x: x, str(list([i for i in num_list if i % 15 == 0]))))))

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : getNumbersOptionOne,
                  2 : getNumbersOptionTwo,
                  3 : getNumbersOptionThree,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()