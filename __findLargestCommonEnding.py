'''
Python program to find the longest common ending
between two given strings. 
Original strings: running ruminating
Common ending between said two strings: ing
Original strings: thisisatest testing123testing
Common ending between said two strings:
'''

def test(str1, str2):
    for i in range(len(str2)):
        while str2[i:] in str1 and str2[-1]==str1[-1]:
            return str2[i:]
    return ""

str1 = "running";
str2 = "ruminating";
print("Original strings: " + str1 + "  " + str2);
print("Common ending between said two strings: " + test(str1, str2));
str1 = "thisisatest";
str2 = "testing123testing";
print("\nOriginal strings: " + str1 + "  " + str2);
print("Common ending between said two strings: " + test(str1, str2));
