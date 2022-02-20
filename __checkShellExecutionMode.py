'''
A Python program to determine if a Python shell is executing in32bit or 64bit mode on OS.
'''
# For 32 bit it will return 32 and for 64 bit it will return 64
import platform, struct
print(platform.architecture()[0])
print(struct.calcsize("P") * 8)
