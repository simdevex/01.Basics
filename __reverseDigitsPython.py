'''
Python program to reverse the digits of a given number and add it to the original, 
If the sum is not a palindrome repeat this procedure. Note: A palindrome is a word, number, 
or other sequence of characters which reads the same backward as forward, such as madam or racecar
'''

def rev_number (n):
    s = 0
    while True:
        k = str (n)
        if k == k[::-1]:
            break
        else:
            '''
            when you do k[::-1], it starts from the end towards the first taking each element. 
            So it reverses a. This is applicable for lists/tuples as well.
            '''
            m =  int (k[::-1]) 
            n += m
    return n

print(rev_number(1234))
print(rev_number(1473))
print(rev_number(9999))
