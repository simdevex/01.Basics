'''
Python program to get an absolute file path 
Resolve a file's absolute path relative to the current working directory in Python
'''

def absolute_file_path(path_fname):
        import os
        return os.path.abspath(path_fname)        

print("Absolute file path: ",absolute_file_path("getAbsoluteFilePath.py"))

from pathlib import Path
p = Path("getAbsoluteFilePath.py").resolve()
print(p)
