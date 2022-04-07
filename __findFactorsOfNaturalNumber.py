'''
Python program to find all the factors of a given
natural number. Go to the editor
Factors: The factors of a number are the numbers that divide into it exactly.
The number 12 has six factors:
1, 2, 3, 4, 6 and 12 If 12 is divided by any of the six factors then
the answer will be a whole number. For example:
12 / 3 = 4
Original Number: 1
Factors of the said number: {1}
Original Number: 12
Factors of the said number: {1, 2, 3, 4, 6, 12}
Original Number: 100
Factors of the said number: {1, 2, 4, 100, 5, 10, 50, 20, 25}
'''

#Source https://bit.ly/3w492zp

from functools import reduce

'''
sqrt(x) * sqrt(x) = x. So if the two factors are the same, they're both 
the square root. If you make one factor bigger, you have to make the other 
factor smaller. This means that one of the two will always be less than or 
equal to sqrt(x), so you only have to search up to that point to find one 
of the two matching factors. You can then use x / fac1 to get fac2.

The reduce(list.__add__, ...) is taking the little lists of [fac1, fac2] 
and joining them together in one long list.

The [i, n/i] for i in range(1, int(sqrt(n)) + 1) if n % i == 0 returns 
a pair of factors if the remainder when you divide n by the smaller one 
is zero (it doesn't need to check the larger one too; it just gets that 
by dividing n by the smaller one.)

The set(...) on the outside is getting rid of duplicates, which only 
happens for perfect squares. For n = 4, this will return 2 twice, so 
set gets rid of one of them.
'''
def test(n):    
    '''
    a function that implements a mathematical technique called folding or reduction. reduce()
    is useful when you need to apply a function to an iterable and reduce it to a single cumulative value.
    A user-defined function
    A lambda function
    A function called operator.add()
    '''
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

n = 1
print("\nOriginal Number:",n)
print("Factors of the said number:",test(n))
n = 12
print("\nOriginal Number:",n)
print("Factors of the said number:",test(n))
n = 100
print("\nOriginal Number:",n)
print("Factors of the said number:",test(n))
