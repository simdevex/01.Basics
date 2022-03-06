'''
Python program to create maximum number of regions obtained by drawing n given straight lines

if you draw a straight line on a plane, the plane is divided into
two regions. For example, if you pull two straight lines in parallel,
you get three areas, and if you draw vertically one to the other you
get 4 areas.

Write a Python program to create "maximum" number of regions
obtained by drawing n given straight lines. Go to the editor
Input:
(1 <= n <= 10,000)
Input number of straight lines (o to exit):
5
Python Basic (Part-II) - Exercises, Practice, Solution - w3resource about:reader?url=https%3A%2F%2Fwww.w3resource.com%2Fpython-e...
17
Number of regions:
16
'''

while True:
    print ("Input number of straight lines (0 to exit): ")
    n = int (input())
    if n <= 0:
        break
    print ("Number of regions:")
    print ((n*n+n+2)//2)

