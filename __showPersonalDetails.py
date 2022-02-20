'''
A Python program to display your details like name, age, addressin three diff erent lines.
'''


def main ():
    a,b,c = [str(x) for x in input("Enter name, age, and addrees\n").split(',')]
    print ("Your details are :", a,b,c, sep ='\n')

def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

main ()