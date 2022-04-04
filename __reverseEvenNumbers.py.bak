'''
Write a Python program to reverse all the words which have
even length. 
Sample Input:
("The quick brown fox jumps over the lazy dog")
("Python Exercises")
Sample Output:
The quick brown fox jumps revo the yzal dog nohtyP Exercises
'''

def reverse_even(txt):
    '''
    Powerful use of single line returns
    Reverse the string by slicing backwards [::-1]
    Row to return and single statement in a function call
    In Python you can read statement from right to left hence statement below can be compacted into
    a single line
    for i in txt.split():
        if not len(i)%2:
            return ' '.join(i[::-1]          
        else
            return i
            
    '''
    return ' '.join(i[::-1] if not len(i)%2 else i for i in txt.split())


print(reverse_even("The quick brown fox jumps over the lazy dog"))
print(reverse_even("Python Exercises"))
