'''
Python program to only list files in a directory and skip sub-directories of a given directory.
'''

#Sample Solution #1
def findFileSkipDirectoryOne (dirPath):
    import os
    print([f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))])

#Sample Solution-2:
def findFileSkipDirectoryTwo (dirPath):
    import os
    user_path = dirPath
    for fname in os.listdir(user_path):
        path = os.path.join(user_path, fname)
        if os.path.isdir(path):
         # skip directories
            continue
        # print the file names
        print(fname)

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    inpVal = str (input ("Pick a directory to pick:\n"))
    #Use dictionary instead of switch case
    selection = { 1 : findFileSkipDirectoryOne,
                  2 : findFileSkipDirectoryTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key](inpVal)
            break

main ()