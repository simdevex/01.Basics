'''
Python program to sort three integers without using conditional statements and loops
'''
def doSimpleSort (a1, a2, a3):

    l1 = min(a1, a2, a3)
    l3 = max(a1, a2, a3)
    l2 = (a1 + a2 + a3) - l1 - l3

    return  (l1, l2, l3)

def main ():
    x = int(input("Input first number: "))
    y = int(input("Input second number: "))
    z = int(input("Input third number: "))
    a, b, c = [int(i) for i in doSimpleSort (x, y, z)] 
    print("Numbers in sorted order: ", a, b, c)
    
main ()