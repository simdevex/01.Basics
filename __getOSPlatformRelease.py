'''
A Python program to get OS name, platform and releaseinformation.
'''

import platform
import os
print("Name of the operating system:",os.name)
print("\nName of the OS system:",platform.system())
print("\nVersion of the operating system:",platform.release())