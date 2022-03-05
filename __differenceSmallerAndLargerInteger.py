'''
Python program to find the difference between the
largest integer and the smallest integer which are created by 8
numbers from 0 to 9. The number that can be rearranged shall
start with 0 as in 00135668 (Sort descending, and sort ascending. Then take difference)

Input:
Input an integer created by 8 numbers from 0 to 9.:
34568729
Difference between the largest and the smallest integer from the given integer:
75308643
'''

print("Input an integer created by 8 numbers from 0 to 9.:")
num = list(input())
print("Difference between the largest and the smallest integer from the given integer:")
print(int("".join(sorted(num,reverse=True))) - int("".join(sorted(num))))
