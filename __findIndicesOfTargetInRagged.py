'''
An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row. Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them, but they are useful as arrays in computing.

Python program to find the indices of all occurrences of target in the uneven matrix. Go to the editor
Input:
[([1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]),19]
Output:
[[0, 4], [1, 0], [1, 3], [4, 1]]
Input:
[([1, 2, 3, 2], [], [7, 9, 2, 1, 4]),2]
Output:
[[0, 1], [0, 3], [2, 2]]
Click me to see the sample solution

'''

def test(M, T):
    #Compact return statement  with multiple for loops
    '''
    raggedList = []
    for i, row in enumerate(M):
        for j, n in enumerate(row):
             if n == T:
                 raggedList.append ([i,j])
        
    return raggedList
    '''
    return [[i, j] for i, row in enumerate(M) for j, n in enumerate(row) if n == T]


M = [[1, 3, 2, 32, 19], [19, 2, 48, 19], [], [9, 35, 4], [3, 19]]
T = 19
print("Matrix:")
print(M)
print("Target value:")
print(T)
print("Indices of all occurrences of the target value in the said uneven matrix:")
print(test(M,T))
 
M = [[1, 2, 3, 2], [], [7, 9, 2, 1, 4]]
T = 2
print("\nMatrix:")
print(M)
print("Target value:")
print(T)
print("Indices of all occurrences of the target value in the said uneven matrix:")
print(test(M,T)) 
