'''A Python program to determine profiling of Python programs
Note: A profi le is a set of statistics that describes how often 
and for howlong various parts of the program executed. 
These statistics can beformatted into reports via the pstats module.
'''

import cProfile
def sum():
    print("Runnning..")

cProfile.run('sum()')
