'''
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the list
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole list

a[::-1]    # all items in the list, reversed
a[1::-1]   # the first two list, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed

The double colon is a special case in Python’s extended slicing feature. 
The extended slicing notation string[start:stop:step] uses three arguments start, stop, and step to carve out a subsequence. 
It accesses every step-th element between indices start (included) and stop (excluded). The double colon :: occurs if you drop the stop argument. 
In this case, Python will use the default value and doesn’t assume an artificial stop.

string[::2] reads “default start index, default stop index, step size is two—take every second element”.
string[::3] reads “default start index, default stop index, step size is three—take every third element”.
string[::4] reads “default start index, default stop index, step size is four—take every fourth element“.
string[2::2] reads “start index of two, default stop index, step size is two—take every second element starting from index 2“.

'''

print ("Input 8 numbers in an list: ")
#a = [int (input()) for i in range(8)]
a = [14, 2, 8, 9, 77, 93]
print ("All items in the list : ", a)
print ("All items in the list, reversed : ", a[::-1])
print ("All the first two items, reversed : ", a[1::-1])
print ("All the last two items, reversed : ", a[:-3:-1])
print ("All everything except the last two items, reversed : ", a[-3::-1])
