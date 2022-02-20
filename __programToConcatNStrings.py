'''
Python program to concatenate N strings
'''
def concatUsingJoin(colors):
    print("Concatenating With Join :")
    list_of_colors = colors  
    printColors = '-'.join(list_of_colors)
    print(printColors)


def concatUsingPlusOperator(colors):
    print("Concatenating With the + Operator :") 
    print(*colors, sep = "-") 
        
def main():
    n = int(input("Enter numbers of colors : "))
    lst = []
    # iterating till the range
    for i in range(0, n):
        color = str(input())
        lst.append(color) # adding the element
    
    concatUsingJoin (lst)
    concatUsingPlusOperator (lst)
    
main ()