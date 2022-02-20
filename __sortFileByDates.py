'''
Python program to sort files by date
'''

import glob
import os

def sortFileByDates01 ():
    files = glob.glob("C:/Study/Funamentals/Python/01.Basics")
    files.sort(key=os.path.getmtime)
    print ("~sortFileByDates01~")
    print("\n".join(files))

def sortFileByDates02 ():  
    os.chdir('C:/Study/Funamentals/Python/01.Basics')
    result = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)
    print ("~sortFileByDates01~")
    print('\n'.join(map(str, result)))

def main ():
    sortFileByDates01()
    sortFileByDates02()
    
main ()