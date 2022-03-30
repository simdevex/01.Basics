'''
Python program to find the lucky number(s) in a given matrix.
A lucky number is an element of the matrix such that it is the 
minimum element in its row and maximum in its column
Sample Input:
Original matrix: [[1, 2], [2, 3]]
Lucky number(s) in the said matrix: [2]
Original matrix: [[1, 2, 3], [3, 4, 5]]
Lucky number(s) in the said matrix: [3]
Original matrix: [[7, 5, 6], [3, 4, 4], [6, 5, 7]]
Lucky number(s) in the said matrix: [5]
'''

# Lucky number in a Matrix: Maximum in its column and minimum in its row.

def lucky_Numbers(matrix):
    '''
    The zip() function returns a zip object, which is an iterator of tuples where the 
    first item in each passed iterator is paired together, and then the second item in
    each passed iterator are paired together etc.
    If the passed iterators have different lengths, the iterator with the least items
    decides the length of the new iterator.
    
    *args and **kwargs allow you to pass multiple arguments or keyword arguments to a function.
    **kwargs works just like *args, but instead of accepting positional arguments it accepts keyword
    (or named) arguments
    zip(*matrix) is accepting a variable length iteratable
    
    map() function executes a specified function for each item in an iterable. 
    The item is sent to the function as a parameter.
   
    Original matrix: [[1, 2], [2, 3]]
    Min  {1, 2} - find the minimum number in each row, meanining 1 in [1,2] , 2 in [2,3]
    Max  {2, 3} - find the maximum number in each column using zip()
    Lucky number(s) in the said matrix:  [2]

    Original matrix: [[1, 2, 3], [3, 4, 5]]
    Min  {1, 3} - 1 is minimum in [1, 2, 3] , 3 is minimum in [3, 4, 5]
    Max  {3, 4, 5} -  3 is maximum in [1,3] , 4 is maximum in [2, 4] , 5 is maximum in [3, 5] 
    Lucky number(s) in the said matrix:  [3] if you & the 2 sets you get 3

    Original matrix: [[7, 5, 6], [3, 4, 4], [6, 5, 7]]
    Min  {3, 5} - note since we are using set we are getting elements ordered and duplicates removed
    Max  {5, 7} - note since we are using set we are getting elements ordered and duplicates removed
    Lucky number(s) in the said matrix:  [5]
    '''
       
    result = set(map(min, matrix)) & set(map(max, zip(*matrix)))
    return list(result)

m1 = [[1,2], [2,3]]
print("Original matrix:",m1)
print("Lucky number(s) in the said matrix: ",lucky_Numbers(m1))

m1 = [[1,2,3], [3,4,5]]
print("\nOriginal matrix:",m1)
print("Lucky number(s) in the said matrix: ",lucky_Numbers(m1))

m1 = [[7,5,6], [3,4,4], [6,5,7]]
print("\nOriginal matrix:",m1)

print("Lucky number(s) in the said matrix: ",lucky_Numbers(m1))