'''
Write a Python program to check whether a given sequence is linear, quadratic or cubic.
Sequences are sets of numbers that are connected in some way.
Linear sequence:
A number pattern which increases or decreases by the same amount each time is called a linear sequence. 
The amount it increases or decreases by is known as the common difference. 
Meaning the first difference is constant

Quadratic sequence:
In quadratic sequence, the difference between each term increases, or decreases, at a constant rate.
Meaning the second difference is constant

Cubic sequence:
Sequences where the 3rd difference  between its terms is constant.
Meaning the third difference is constant

Sample Input:
[0,2,4,6,8,10]
[1,4,9,16,25]
[0,12,10,0,-12,-20]
[1,2,3,4,5]
Sample Output:
Linear Sequence
Quadratic Sequence
Cubic Sequence
Linear Sequence

'''

def Seq_Linear_Quadratic_Cubic(seq_nums):
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    print ("seq_nums", seq_nums)
    print ("set seq_nums", set(seq_nums))
    # set will remove duplicate elements, and confirm if all elements have a constant difference
    if len(set(seq_nums)) == 1: return "Linear Sequence" 
    
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    print ("seq_nums", seq_nums)
    print ("set seq_nums", set(seq_nums))
    # set will remove duplicate elements, and confirm if all elements have a constant difference
    if len(set(seq_nums)) == 1: return "Quadratic Sequence"
    
    seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
    print ("seq_nums", seq_nums)
    print ("set seq_nums", set(seq_nums))
    # set will remove duplicate elements, and confirm if all elements have a constant difference
    if len(set(seq_nums)) == 1: return "Cubic Sequence"

nums = [0,2,4,6,8,10]
print("Original Sequence:",nums)
print("Check the said sequence is Linear, Quadratic or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))
nums = [1,4,9,16,25]
print("\nOriginal Sequence:",nums)
print("Check the said sequence is Linear, Quadratic or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))
nums = [0,12,10,0,-12,-20]
print("\nOriginal Sequence:",nums)
print("Check the said sequence is Linear, Quadratic or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))
nums = [1,2,3,4,5]
print("\nOriginal Sequence:",nums)
print("Check the said sequence is Linear, Quadratic or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums))
nums = [1,3,8,4,7]
print("\nOriginal Sequence:",nums)
print("Check the said sequence is Linear, Quadratic or Cubic?")
print(Seq_Linear_Quadratic_Cubic(nums)) #as does not return anything, hence print None
