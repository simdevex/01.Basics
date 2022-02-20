'''
A Python program to convert height (in feet and inches) to centimeters.
'''

def calculateHeightInCentimeter(h_ft, h_inch):
    
    h_inch += h_ft * 12
    h_cm = round(h_inch * 2.54, 1)
    return h_cm
    
def main ():
    print("*** Input your height ***")
    h_ft = int(input("Feet: "))
    h_inch = int(input("Inches: "))

    print("Your height is : %d cm." %calculateHeightInCentimeter(h_ft,h_inch ))

main ()