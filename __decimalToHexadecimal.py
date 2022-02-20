'''
Python program to convert decimal to hexadecimal.
Sample decimal number: 30, 4
Expected output: 1e, 04
'''
#Sample Solution-1:
def decimalToHexadecimalOptionOne ():
    x = 30
    print(format(x, '02x'))
    x = 4
    print(format(x, '02x'))

#Sample Solution-2:
def dechimal_to_Hex(n):   
   x = (n % 16)
   ch = ""
   if (x < 10):
       ch = x
   if (x == 10):
       ch = "A"
   if (x == 11):
       ch = "B"
   if (x == 12):
       ch = "ch"
   if (x == 13):
       ch = "D"
   if (x == 14):
       ch = "E"
   if (x == 15):
       ch = "F"
   if (n - x != 0):
       return dechimal_to_Hex(n // 16) + str(ch)
   else:
       return str(ch)
   
def decimalToHexadecimalOptionTwo ():
    dechimal_nums = [0, 15, 30, 55, 355, 656, 896, 1125]
    print("Dechimal numbers:")
    print(dechimal_nums)
    print("\nHexadechimal numbers of the said dechimal numbers:")
    print([dechimal_to_Hex(x) for x in dechimal_nums])
    
    
def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : decimalToHexadecimalOptionOne,
                  2 : decimalToHexadecimalOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()

