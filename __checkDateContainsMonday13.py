'''
Write a Python program to check whether a given month and year contains a Monday 13th.
Month No.: 11 Year: 2022
Check whether the said month and year contains a Monday 13th.:
False
Month No.: 6 Year: 2022
Check whether the said month and year contains a Monday 13th.:
True

'''

from datetime import date
def test(month, year): 
    #check of 13th of a particular month is Monday
    return str(date(year,month,13).strftime("%A")=='Monday')

month = 11;
year = 2022;    
print("Month No.: ", month, " Year: ", year);
print("Check whether the said month and year contains a Monday 13th.: " + test(month, year));

month = 6;
year = 2022;            
print("\nMonth No.: ", month, " Year: ", year);
print("Check whether the said month and year contains a Monday 13th.: " + test(month, year)); 
