'''
Calculate the path on a Rombhus made by integers that gives the maximum value
    7
   3 8
  8 1 0    
 2 7 4 4
4 5 2 6 5
 2 7 4 4 
  8 1 0
   3 8
    7

Arrange the integers (0 to 99 or less) on the pattern, 
as illustrated in figure 1. when you load this stringed data and start 
from the top and follow the following rules, write a program
that prints the maximum sum of the integers that pass through.

At each step, you can go diagonally to the lower left or diagonal lower right.
for example, in the example in figure 1, when you select 7,3,8,8,7,5,7,8,3,7, 
and pass, the sum is the largest 55 (7+3+8+7+5+7+8+3+7=55).


Input:
A series of integers separated by commas are given in diamonds.
No spaces are included in each line. The input example
corresponds to Figure 1. The number of lines of data is less than
100 lines.

Output:
The maximum value of the sum of integers passing according to
the rule on one line.
Input the numbers (ctrl+d to exit):
8
4, 9
9, 2, 1
3, 8, 5, 5
5, 6, 3, 7, 6
3, 8, 5, 5
9, 2, 1
4, 9
8
Maximum value of the sum of integers passing according to the
rule on one line.
64
'''

import sys
print("Input the numbers (ctrl+d to exit):")
nums = [list(map(int, l.split(","))) for l in sys.stdin]
mvv = nums[0]

for i in range(1, (len(nums)+1)//2):
    rvv = [0]*(i+1)
    for j in range(i):
        rvv[j] = max(rvv[j], mvv[j]+nums[i][j])
        rvv[j+1] = max(rvv[j+1], mvv[j]+nums[i][j+1])
    mvv = rvv

for i in range((len(nums)+1)//2, len(nums)):
    rvv = [0]*(len(mvv)-1)
    for j in range(len(rvv)):
        rvv[j] = max(mvv[j], mvv[j+1]) + nums[i][j]
    mvv = rvv
print("Maximum value of the sum of integers passing according to the rule on one line.") 
print(mvv[0])
