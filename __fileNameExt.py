def printFileExt (str =''):
    f_extns = str.split(".")
    print ("The extension of the file is :" , repr(f_extns[-1]), sep = ' ')
    
def getFileName():
    fName = input ("Enter file name : ")
    return fName

def main():
    fileName = getFileName()
    printFileExt(fileName)
    
main()