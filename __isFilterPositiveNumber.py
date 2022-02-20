'''
Python program to filter the positive numbers from a list.
'''
#Sample Solution 01
def filterPositiveIntegerOptionOne():
    nums = [34, 1, 0, -23, 12, -88]
    print("Original numbers in the list: ",nums)
    new_nums = list(filter(lambda x: x >0, nums))
    print("Positive numbers in the said list: ",new_nums)

#Sample Solution 02
def filterPositiveIntegerOptionTwo():
    nums = [34, 1, 0, -23, 12, -88]
    print("Original numbers in the list: ",nums)
    print("Positive numbers in the said list: ")
    for pos_nums in nums:
        if pos_nums > 0:
            print(pos_nums, end = " ")

#Sample Solution 03      
def filterPositiveIntegerOptionThree():    
    nums = [34, 1, 0, -23, 12, -88]
    print("Original numbers in the list: ",nums)
    pos_nums = [n for n in nums if n> 0]
    print("Positive numbers in the said list: ",*pos_nums)

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : filterPositiveIntegerOptionOne,
                  2 : filterPositiveIntegerOptionTwo,
                  3 : filterPositiveIntegerOptionThree,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()