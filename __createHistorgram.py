'''
A Python program to create a histogram from a given list ofintegers.

'''

def createHistoGram (inputChar, inputFormatTuple):
    
    for inputFormat in inputFormatTuple:
        strHistoLine = ""
        if inputFormat.isnumeric():
            for i in range (int(inputFormat)):
                strHistoLine = strHistoLine + inputChar
            print (strHistoLine)

def main():
    myChar = input ("Input character to draw : ")
    myTuple = tuple(input("Input comma separate histogram format (0-9) : "))
    createHistoGram (myChar, myTuple)
    
main()