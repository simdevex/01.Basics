'''
Python program to find the largest number where commas or periods are decimal points. 

Input:
['100', '102,1', '101.1']
Output:
102.1
'''

#License: https://bit.ly/3oLErEI

def test(str_nums):
    
    str_nums_formatted = []
    for s in str_nums:
        str_nums_formatted.append (float(s.replace(",", ".")))
        
    return max(str_nums_formatted)
    
    #return max(float(s.replace(",", ".")) for s in str_nums)

str_nums = ["100", "102,1", "101.1"]
print("Original list:")
print(str_nums)
print("Largest number where commas or periods are decimal points:")
print(test(str_nums))
