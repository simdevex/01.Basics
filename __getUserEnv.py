'''
Python program to get the users environment
'''
import os
import pprint

def getUserEnvOptionOne():
    print()
    print(os.environ)
    print()

def getUserEnvOptionTwo():
    # User's environment variables
    u_env_var = os.environ
    print("User's Environment variable:")
    pprint.pprint(dict(u_env_var), width = 1)


def getUserEnvOptionThree():  
    host_name = os.environ['HOSTNAME']
    print("HOSTNAME:", host_name)
    python_path = os.environ.get('PYTHONPATH')
    print("Python Path:", python_path)

def main ():
    inpOption = int (input ("Select options one of the options : |1|2|3|\n"))
    #Use dictionary instead of switch case
    selection = { 1 : getUserEnvOptionOne,
                  2 : getUserEnvOptionTwo,
                  3 : getUserEnvOptionThree,
                } 
        
    for key in selection:
        if key == inpOption:
            selection[key]()
            break

main ()