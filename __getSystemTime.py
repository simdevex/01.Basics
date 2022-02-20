'''
Python program to get the system time
Note : The system time is important for debugging, network information,random number seeds, 
or something as simple as program performance.
'''

import time
import datetime

def printUsingTime ():
    print("Print using time")
    print(time.ctime())
    print()


def printUsingDateTime ():
    print("Print using date time")
    print(datetime.datetime.now())


printUsingTime ()
printUsingDateTime ()