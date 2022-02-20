import calendar

def main ():
    y = int(input("Input the year : "))
    m = int(input("Input the month : "))
    print(calendar.month(y, m))
    
main ()