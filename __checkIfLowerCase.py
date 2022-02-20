'''
Python program to check if any lowercase letters exist in a string.
'''
#Sample Solution-1
def isLowerCaseExistsOptionOne ():
    str1 = 'A8238i823acdeOUEI'
    print(any(c.islower() for c in str1))

#Sample Solution-2:
def lower_case_str_ord(text):
    ctr = 0
    for char in text:
       if(ord(char) >= 97 and ord(char) <= 122):
           ctr = ctr + 1
    if (ctr>0):
       return True
    else: 
        return False
   
def isLowerCaseExistsOptionTwo ():
    print("Check if all input alphabets are small!")
    str1 = 'A8238i823acdeOUEI'
    print("\nOriginal string:",str1)
    print("Lowercase letters exist in the said string: ", lower_case_str_ord(str1))
    str1 = 'PYTHON'
    print("\nOriginal string:",str1)
    print("Lowercase letters exist in the said string: ",lower_case_str_ord(str1))
    str1 = 'javascript'
    print("\nOriginal string:",str1)
    print("Lowercase letters exist in the said string: ",lower_case_str_ord(str1))

#Sample Solution-3:
def lower_case_str_islower(text):
    if text.islower():
        return True
    return False

def isLowerCaseExistsOptionThree():
    str1 = 'A8238i823acdeOUEI'
    print("Original string:",str1)
    print("Lowercase letters exist in the said string: ",lower_case_str_islower(str1))
    str1 = 'PYTHON'
    print("\nOriginal string:",str1)
    print("Lowercase letters exist in the said string: ",lower_case_str_islower(str1))
    str1 = 'javascript'
    print("\nOriginal string:",str1)
    print("Lowercase letters exist in the said string: ",lower_case_str_islower(str1))

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : isLowerCaseExistsOptionOne,
                  2 : isLowerCaseExistsOptionTwo,
                  3 : isLowerCaseExistsOptionThree,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()

