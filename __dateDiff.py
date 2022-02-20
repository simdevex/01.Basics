from datetime import datetime 

def dateDiff(fDate , lDate ):
    return (lDate - fDate)
    
def getDate(strDateOrder = ''):
    inputString = str(input('Enter %s(yyyy-mm-dd): ' %strDateOrder))
    myDate = datetime.strptime(inputString, "%Y-%m-%d").date()
    return myDate

def main():
    firstDate = getDate ('First Date')
    lastDate = getDate ('Last Date')
    delta = dateDiff (firstDate, lastDate)
    print("Difference in day :", delta.days)
    
main()