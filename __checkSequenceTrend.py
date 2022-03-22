'''
Python program to check whether a sequence of numbers has an increasing trend or not. 
Sample Input:
[1,2,3,4]
[1,2,5,3,4]
[-1,-2,-3,-4]
[-4,-3,-2,-1]
[1,2,3,4,0]
Sample Output:
'''

def increasing_trend(nums):
    if (sorted(nums) == nums):
        return True
    else:
        return False

print(increasing_trend([1,2,3,4]))
print(increasing_trend([1,2,5,3,4]))
print(increasing_trend([-1,-2,-3,-4]))
print(increasing_trend([-4,-3,-2,-1]))
print(increasing_trend([1,2,3,4,0]))
