'''
Write a Python program to check if a given string contains two
similar consecutive letters. 
Original string: PHP
Check for consecutive similar letters! False
Original string: PHHP
Check for consecutive similar letters! True
Original string: PHPP
Check for consecutive similar letters! True
'''
def test(str1):
    #Check if any() of the items in a list are True:
    return any(c1 == c2 for c1, c2 in zip(str1, str1[1:]))

str = "PHP"
print("Original string: ",str)
print("Check for consecutive similar letters! ",test(str))
str = "PHHP"
print("\nOriginal string: ",str)
print("Check for consecutive similar letters! ",test(str))
str = "PHPP"
print("\nOriginal string: ",str)
print("Check for consecutive similar letters! ",test(str))
