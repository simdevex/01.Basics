'''
Python program to extract single key-value pair of a dictionary in variables.
'''

#Sample Solutions -1
def getSingleKeyValueFromDictOptionOne ():
    d = {'Red': 'Green'}
    (c1, c2), = d.items()
    print(c1)
    print(c2)

#Sample Solution-2:
def getSingleKeyValueFromDictOptionTwo ():   
    dict = {'key1': 'val1', 'key2': 'val2', 'key3': 'val3', 'key4': 'val4'}
    print("Extract specific key, value")
    x, y = list(dict.items())[0]
    print(x, y)
    x, y = list(dict.items())[3]
    print(x, y)

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : getSingleKeyValueFromDictOptionOne,
                  2 : getSingleKeyValueFromDictOptionTwo,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()
