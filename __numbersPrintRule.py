'''a Python program to print all even numbers from a givennumbers list 
in the same order and stop the printing if any numbers thatcome after 237 in the sequence'''

def printEvenNumbersFromList (inputList):
    localList = list (inputList)
    localStr = []
    
    for item in localList:
        if str(item).isdigit:
            if item % 2 == 0 and item < 237 : 
                localStr.append (item)
    
    return localStr
    
def main ():
    mainList = [
                386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
                399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
                815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527
                ]
    mainStr = printEvenNumbersFromList (mainList)
 
    print (mainStr)
    
main ()
