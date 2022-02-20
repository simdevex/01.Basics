'''
Python program to get the size of a fi le
'''

import os

#Sample Solution-1
def getFileSizeUsingSize (path):
    print ("Sample solution 01")
    file_size = os.path.getsize(path)
    print("\nThe size of %s is : " %path,file_size,"Bytes")
    print()

#Sample Solution-2:
def getFileSizeUsingStat(path):
    print ("Sample solution 02")
    file_size = os.stat(path)
    print("\nThe size of %s is : " %path,file_size,"Bytes")

#Sample Solution-3:
def getFileSizeUsingSeek(path):
    print ("Sample solution 03")
    file = open(path)
    file.seek(0, os.SEEK_END)
    print("The size of %s is : " %path, file.tell(), "bytes")

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|\n"))
    inpPath = str (input ("Provide a path\n"))
    #Use dictionary instead of switch case
    selection = { 1 : getFileSizeUsingSize,
                  2 : getFileSizeUsingStat,
                  3 : getFileSizeUsingSeek,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key](inpPath)
            break
main()


