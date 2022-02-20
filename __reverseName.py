def returnFirstName():
    return input ("Enter first name")
    
def returnLastName():
    return input ("Enter last name")
    
def reverseString (item = ''):
    return item[::-1]

def main():
    firstName = returnFirstName()
    reverseFirstName = reverseString(firstName)
    lastName = returnLastName()
    reverseLastName = reverseString(lastName)
   
    print (reverseFirstName,reverseLastName, sep = ' ' )
    
main()