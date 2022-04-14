'''
Write a Python program to check a given list of integers where
the sum of the first i integers is i. 
Input:
[0, 1, 2, 3, 4, 5]
Output:
False
Input:
[1, 1, 1, 1, 1, 1]
Output:
True
Input:
[2, 2, 2, 2, 2]
Output:
False

'''

#License: https://bit.ly/3oLErEI
 
def test(nums):
    #all() function returns True if all items in an iterable are true, otherwise it returns False. 
    #If the iterable object is empty, the all() function also returns True. all() only works on iteratable
    #Long single line return statement 
    
    statusList = []
    
    for i in range(len(nums)):
        statusList.append(sum(nums[:i]) == i)
    
    return all(statusList)
    
    #return all([sum(nums[:i]) == i for i in range(len(nums))])

nums = [0,1,2,3,4,5]
print("Original list:")
print(nums)
print("Check the said list, where the sum of the first i integers is i:")
print(test(nums))
nums = [1,1,1,1,1,1]
print("\nOriginal list:")
print(nums)
print("Check the said list, where the sum of the first i integers is i:")
print(test(nums))
nums = [2,2,2,2,2]
print("\nOriginal list:")
print(nums)
print("Check the said list, where the sum of the first i integers is i:")
print(test(nums))
