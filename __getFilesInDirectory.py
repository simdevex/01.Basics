'''
A Python program to list all fi les in a directory in Python.
'''
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('C:/Study/Funamentals/To Read/Excercises/03.Python NumPy') 
              if isfile(join('C:/Study/Funamentals/To Read/Excercises/03.Python NumPy', f))]
print(files_list);