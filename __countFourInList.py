'''
A Python program to count the number 4 in a given list.
'''

def coundFourInList(listItem = []):
    
    funList = listItem
    listCount = 0
    
    for funListItem in funList:
        if funListItem == str(4):
            listCount += 1 
            
    return listCount

def main ():
    mainInput = input ("Enter a list of numbers, separated by commas")
    mainList = list(mainInput)
    mainCountOfFour = coundFourInList (mainList)
    print ("Count of 4 in the list is:", mainCountOfFour)
    
main ()

    