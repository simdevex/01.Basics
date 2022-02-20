'''
Python function to check whether a distinct pair of numbers whose product is odd is present 
in a sequence of integer values.
'''
import itertools

def odd_product(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if  i != j:
                product = nums[i] * nums[j]
                if product & 1:
                    return True
    return False          

def checkDistinctPairOne ():
    dt1 = [2, 4, 6, 8]
    dt2 = [1, 6, 4, 7, 8]
    dt3 = [1, 3, 5, 7, 9]
    print(dt1, odd_product(dt1));
    print(dt2, odd_product(dt2));
    print(dt3, odd_product(dt3));


def pair_nums_odd(nums):
    uniquelist = set(nums)
    result =[]
    for n in itertools.combinations(uniquelist, 2):
        if ((n[0] * n[1]) % 2 == 1):
            temp = str(n[0]) + " * " + str(n[1])
            result.append(temp)
    return result

def checkDistinctPairTwo ():
          
    dt1 = [2, 4, 6, 8]
    print("Original sequence:")
    print(dt1)
    print("Distinct pair of numbers whose product is odd present in the said sequence:") 
    print(pair_nums_odd(dt1));
    dt2 = [1, 6, 4, 7, 8]
    print("\nOriginal sequence:")
    print(dt2)
    print("Distinct pair of numbers whose product is odd present in the said sequence:") 
    print(pair_nums_odd(dt2));
    dt3 = [1, 3, 5, 7, 9]
    print("\nOriginal sequence:")
    print(dt3)
    print("Distinct pair of numbers whose product is odd present in the said sequence:") 
    print(pair_nums_odd(dt3));

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : checkDistinctPairOne,
                  2 : checkDistinctPairTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()
