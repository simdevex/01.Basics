'''
Python program to check whether two given lines are parallel or not. 
Note: Parallel lines are two or more lines that never intersect.
Parallel Lines are like railroad tracks that never intersect.
The General Form of the equation of a straight line is: ax + by = c

The said straight line is represented in a list as [a, b, c]
Example of two parallel lines:
x + 4y = 10 and x + 4y = 14
Sample Input:
([2,3,4], [2,3,8])
([2,3,4], [4,-3,8])
Sample Output:
True
False
'''
def parallel_lines(line1, line2):
    # if ratio of x and y is the same for the 2 lines then they are parrallel
    return line1[0]/line1[1] == line2[0]/line2[1]

#2x + 3y = 4, 2x + 3y = 8
print(parallel_lines([2,3,4], [2,3,8]))
#2x + 3y = 4, 4x - 3y = 8
print(parallel_lines([2,3,4], [4,-3,8])) 


