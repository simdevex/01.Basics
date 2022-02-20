'''
Python program to get file creation and modificationdate/times.
'''

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("C:\\Study\\Funamentals\\Python\\01.Basics\\getHeightToCentimeter.py")))
print("Created: %s" % time.ctime(os.path.getctime("C:\\Study\\Funamentals\\Python\\01.Basics\\getHeightToCentimeter.py")))
