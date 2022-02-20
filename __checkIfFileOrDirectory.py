'''
Python program to check whether a fi le path is a fi le or adirectory
'''
#"C:/Study/Funamentals/Python/01.Basics/__calculateGCD.py"
#"C:/Study/Funamentals/Python/01.Basics"

import os  
path="C:/Study/Funamentals/Python/01.Basics/__calculateGCD.py"  
if os.path.isdir(path):  
    print("\nIt is a directory")  
elif os.path.isfile(path):  
    print("\nIt is a normal file")  
else:  
    print("It is a special file (socket, FIFO, device file)" )
print()
