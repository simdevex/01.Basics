'''
Python program to remove two duplicate numbers from a given number of list. 
Sample Input:
([1,2,3,2,3,4,5])
([1,2,3,2,4,5])
([1,2,3,4,5])
Sample Output:
[1, 4, 5]
[1, 3, 4, 5]
[1, 2, 3, 4, 5]

'''

a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
uniq_items = []

for x in a:
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)
