'''
Python program to compute the sum of the negative
and positive numbers of an array of integers and display the
largest sum. 
Original array elements: {0, 15, 16, 17, -14, -13, -12, -11, -10, 18,
19, 20}
Largest sum - Positive/Negative numbers of the said array: 105
Original array elements: {0, 3, 4, 5, 9, -22, -44, -11}
Largest sum - Positive/Negative numbers of the said array: -77
'''
def test(lst):
    pos_sum = 0
    neg_sum = 0
    for n in lst:
        if n > 0:
            pos_sum += n
        elif n < 0:
            neg_sum += n
    print ("Pos Sum", pos_sum)
    print ("Neg Sum", neg_sum)
    return max(pos_sum, neg_sum, key=abs)

nums = { 0, -10, -11, -12, -13, -14, 15, 16, 17, 18, 19, 20 };
print("Original array elements:");
print(nums)
print("Largest sum - Positive/Negative numbers of the said array: ", test(nums));
nums = { -11, -22, -44, 0, 3, 4 , 5, 9 };
print("\nOriginal array elements:");
print(nums)
print("Largest sum - Positive/Negative numbers of the said array: ", test(nums));
