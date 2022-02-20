'''
Python program to make file lists from current directory using a wildcard.
'''

#Sample Solution-1:
def getFileListOptionOne ():
    import glob
    file_list = glob.glob('*.*')
    print(file_list)
    #Specific files
    print(glob.glob('*.py'))
    print(glob.glob('./[0-9].*'))

#Sample Solution-2:
def getFileListOptionTwo ():
    from pathlib import Path
    for path in Path("/").glob("*.*"):
        print(path)

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : getFileListOptionOne,
                  2 : getFileListOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()