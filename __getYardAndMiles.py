'''
Python program to convert the distance (in feet) to inches,yards, and miles
'''

def distanceInInches (d_ft):
    print("The distance in inches is %i inches." %(d_ft * 12))

def distanceInYard (d_ft):
    print("The distance in yards is %.2f yards." %(d_ft / 3.0))

def distanceInMiles (d_ft):
    print("The distance in miles is %.2f miles." %(d_ft / 5280.0) )
    

def main ():
    d_ft = int(input("Input distance in feet: "))
    distanceInInches (d_ft)
    distanceInYard (d_ft)
    distanceInMiles (d_ft)
    
main()