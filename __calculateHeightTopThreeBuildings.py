'''
Python program to find heights of the top three building in descending order from eight given buildings
Input:
0 <= height of building (integer) <= 10,000
Input the heights of eight buildings:
25
35
15
16
30
45
37
39
Heights of the top three buildings:
45
39
37

a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
'''

print ("Input the heights of eight buildings: ")
l = [int (input()) for i in range(8)]
print ("Heights of the top of three buildings:")
l = sorted (l)
print (*l[:4:-1], sep = '\n')