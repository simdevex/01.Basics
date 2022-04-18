'''
Given a string consisting of whitespace and groups of matched
parentheses, write a Python program to split it into groups of
perfectly matched parentheses without any whitespace. 
Input:
( ()) ((()()())) (()) ()
Output:
['(())', '((()()()))', '(())', '()']
Input:
() (( ( )() ( )) ) ( ())
Output:
['()', '((()()()))', '(())']
'''

#License: https://bit.ly/3oLErEI

def test(combined):
    ls = []
    s2 = ""
    for s in combined.replace(' ', ''):
        s2 += s
        if s2.count("(") == s2.count(")"):
            ls.append(s2)
            s2 = ""
    return ls 

combined = '( ()) ((()()())) (()) ()'
print("Parentheses string:")
print(combined)
print("Separate parentheses groups of the said string:")
print(test(combined))

combined = '() (( ( )() (   )) ) ( ())'
print("\nParentheses string:")
print(combined)
print("Separate parentheses groups of the said string:")
print(test(combined))
