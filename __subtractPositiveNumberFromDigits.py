'''
Python program that accept a positive number and subtract from this number the sum of its digits and so on.
Continues this operation until the number is positive

'''

def repeat_times (n):
    n_str = str(n)
    while (n >0):
        n -= sum([int(i) for i in list (n_str)])
        n_str = list (str(n))
    return n

print (repeat_times(9))
print (repeat_times(20))
print (repeat_times (110))
print (repeat_times(5674))