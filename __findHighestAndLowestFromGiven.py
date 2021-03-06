'''
Write a Python program to find the highest and lowest number
from a given string of space separated integers. 
Sample Input:
("1 4 5 77 9 0")
("-1 -4 -5 -77 -9 0")
("0 0")
Sample Output:
(77, 0)
(0, -77)
(0, 0)
'''
def highest_lowest_num(str1):
      #first create a numeric list  
      num_list = list(map(int, str1.split()))
      #then return minmum and maximum value
      return max(num_list), min(num_list)

print(highest_lowest_num("1 4 5 77 9 0"))
print(highest_lowest_num("-1 -4 -5 -77 -9 0"))
print(highest_lowest_num("0 0"))
