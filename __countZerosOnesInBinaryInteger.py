'''
Write a Python program to count number of zeros and ones in
the binary representation of a given integer.

Original number: 12
Number of ones and zeros in the binary representation of the said
number: Number of zeros: 2, Number of ones: 2
Original number: 1234
Number of ones and zeros in the binary representation of the said
number: Number of zeros: 6, Number of ones: 5

'''

def test(num):
    #bin(num) will produce a string like this 0b1100
    #replace("0b", "") replacement will remove 0b
    ones =  bin(num). replace("0b", "").count('1')
    zeros = bin(num). replace("0b", "").count('0')
    return "Number of zeros: " + str(zeros) + ", Number of ones: " + str(ones);

n = 12; 
print("Original number: ",n);
print("Number of ones and zeros in the binary representation of the said number:");
print(test(n));
n = 1234;
print("\nOriginal number: ",n);
print("Number of ones and zeros in the binary representation of the said number:");
print(test(n));
