'''
Python program to reverse the binary representation
of an given integer and convert the reversed binary number into an
integer. 
Original number: 13
Reverse the binary representation of the said integer and convert it
into an integer: 11
Original number: 145
Reverse the binary representation of the said integer and convert it
into an integer: 137
Original number: 1342
Reverse the binary representation of the said integer and convert it
into an integer: 997
'''
def test(n):
    #convert to binary, and then convert to integer
    return int(bin(n)[::-1][:-2], 2)

n = 13
print("Original number: ", n);
print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n));
n = 145
print("Original number: ", n);
print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n));
n = 1342
print("Original number: ", n);
print("Reverse the binary representation of the said integer and convert it into an integer:\n",test(n));
