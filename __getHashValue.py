'''
Python program to hash a word.
The Unicode Standard (version 14.0) classifies 1,475 characters as belonging to the Latin script.
Latin Alphabet: Uppercase A starts at 65
'''

def codedToUpper(word):
    return word.upper()
    
def codedToHash(word):
    soundex=[0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
    coded=word[0]
    
    for a in word[1:len(word)]:
        i=65-ord(a)
        coded=coded+str(soundex[i])
 
    return coded

def main ():
    word=input("Input the word be hashed: ")
    upperWord = codedToUpper (word)
    coded = str (codedToHash (upperWord))    
    print() 
    print("The coded word is using method one : ", coded)
    print("The coded word is using method two : ", str(hash(word)))
    print()

main ()