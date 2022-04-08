'''
Python program to alternate the case of each letter in
a given string and the first letter of the said string must be uppercase. 
Original string: Python Exercises
After alternating the case of each letter of the said string: PyThOn ExErCiSeS
Original string: C# is used to develop web apps, desktop apps,
mobile apps, games and much more.

After alternating the case of each letter of the said string: C# iS
uSeD tO dEvElOp WeB aPpS, dEsKtOp ApPs, MoBiLe ApPs,
GaMeS aNd MuCh MoRe.
'''
def test(txt):
    result_str = ""
    s = True
    for i in txt:
        result_str += i.upper() if s else i.lower()
        '''
        if s:
            result_str += i.upper()
        else:
            i.lower()
        '''
        '''
        isalpha() method returns True if all the characters are alphabet letters (a-z).
        print ("isalpha()", i.isalpha())
        use logic below to flip between lower and upper case, and ignore the spaces or any non
        alphanumberic charecters
        '''
        
        if i.isalpha():
            s = not s
    return result_str

str1 = "Python Exercises";
print("Original string: ", str1);
print("After alternating the case of each letter of the said string:")
print(test(str1))

'''
str1 = "C# is used to develop web apps, desktop apps, mobile apps, games and much more.";
print("\nOriginal string: ", str1);
print("After alternating the case of each letter of the said string:")
print(test(str1))  
'''