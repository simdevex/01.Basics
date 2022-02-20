'''
Python program to check if every consecutive 
sequence ofzeroes is followed by a consecutive sequence of ones of same length in agiven string.
Return True/False.
Original sequence: 01010101
Check if every consecutive sequence of zeroes is followed by a consecutivesequence of ones in the said string:
True
Original sequence: 00
Check if every consecutive sequence of zeroes is followed by a consecutivesequence of ones in the said string:
False
Original sequence: 000111000111
Check if every consecutive sequence of zeroes is followed by a consecutivesequence of ones in the said string:
True
Original sequence: 00011100011
Check if every consecutive sequence of zeroes is followed by a consecutivesequence of ones in the said string:
False
'''

#Sample Solution-1:
def testZeroOneOptionOne(str1):
    while '01' in str1:
        str1 = str1.replace('01', '')
    return len(str1) == 0

def checkConsecutiveZerosOptionOne ():
    str1 = "01010101"
    print("Original sequence:",str1)
    print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
    print(testZeroOneOptionOne(str1))
    str1 = "00"
    print("\nOriginal sequence:",str1)
    print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
    print(testZeroOneOptionOne(str1))
    str1 = "000111000111"
    print("\nOriginal sequence:",str1)
    print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
    print(testZeroOneOptionOne(str1))
    str1 = "00011100011"
    print("\nOriginal sequence:",str1)
    print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
    print(testZeroOneOptionOne(str1))

#Sample Solution-2:
def testZeroOneOptionTwo(str1):
    temp=[]
    for x in str1:
        if (x=='0'):
            temp.append('0')
        else:
            temp.pop()
    return not temp

def checkConsecutiveZerosOptionTwo ():
    str1 = "01010101"
    print("Original sequence:",str1)
    print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
    print(testZeroOneOptionTwo(str1))
    str1 = "00"
    print("\nOriginal sequence:",str1)
    print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
    print(testZeroOneOptionTwo(str1))
    str1 = "000111000111"
    print("\nOriginal sequence:",str1)
    print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
    print(testZeroOneOptionTwo(str1))
    str1 = "00011100011"
    print("\nOriginal sequence:",str1)
    print("Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:")
    print(testZeroOneOptionTwo(str1))

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : checkConsecutiveZerosOptionOne,
                  2 : checkConsecutiveZerosOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()
