'''
Python program to get the name of the host on which theroutine is running.
'''
#Sample Solution 1
import socket
host_name = socket.gethostname()
print ()
print("Sample Solution 1")
print("Host name:", host_name)

#Sample Solution 2
import platform
host_name = platform.uname()[1]
print ()
print("Sample Solution 2")
print("Host name:", host_name)

#Sample Solution 3
#import os
#host_name = os.uname().nodename
#print("Sample Solution 3", sep ='\n')
#print("Host name:", host_name)

