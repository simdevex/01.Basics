'''
Python program to create a copy of its own source code
'''

def file_copy(src, dest):
    with open(src) as f, open(dest, 'w') as d:
        d.write(f.read())


def main ():
    scrFile = str (input ("Select source file\n"))
    destFile = str (input ("Select destination file\n"))
    # copy source file to destination file
    file_copy (scrFile, destFile)
    
    #Now read destination file line by line and print
    with open(destFile, 'r') as filehandle:
        for line in filehandle:
            print(line, end = '')
    
main ()