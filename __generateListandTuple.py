def getValues ():
    values = input("Input some comma seprated numbers : ")
    return values

def printListValue(str=''):
    listValue = str.split(',')
    print('List : ',listValue)
    
def printTupleValue(str=''):
    tupleValue =  eval(str)
    print('Tuple : ',tupleValue)
    
def main():
    strValue = getValues ()
    printListValue (strValue)
    printTupleValue (strValue)
     
main ()