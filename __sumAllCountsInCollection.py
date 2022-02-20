'''
Python program to sum of all counts in a collections
'''

def sumAllCollectionCountsOptionOne ():
    import collections
    num = [2,2,4,6,6,8,6,10,4]
    print(sum(collections.Counter(num).values()))

def sumAllCollectionCountsOptionTwo ():
    nums = [2,2,4,6,6,8,6,10,4]
    print(len(nums))

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : sumAllCollectionCountsOptionOne,
                  2 : sumAllCollectionCountsOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()

