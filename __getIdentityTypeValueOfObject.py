'''
Python program to get the Identity, Type, and Value of anobject.
'''
def getObjectIdentityTypeValue (x):
    print("\nIdentity: ",x)
    print("\nType: ",type(x))
    print("\nValue: ",id(x))

def main ():
    inpObject = input ("Input Object \n")
    getObjectIdentityTypeValue (inpObject)
    
main ()
    