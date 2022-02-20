'''
Python program to test whether all numbers of a list isgreater than a certain number.
'''
def basicSummation():
    num = [2, 3, 4, 5]
    print()
    print(all(x > 1 for x in num))
    print(all(x > 4 for x in num))
    print()


def genericSummation(nums, n):
       return(all(x > n for x in nums))    
   
     
def main():   
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print("Original list numbers:")
    print(nums)
    n = 12
    print("\nCheck whether all numbers of the said list greater than",n)
    print(genericSummation(nums, n))
    n = 5
    print("\nCheck whether all numbers of the said list greater than",n)
    print(genericSummation(nums, n))

main ()