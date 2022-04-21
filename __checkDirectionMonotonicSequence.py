'''
Python program to determine the direction ('increasing' or 'decreasing') of monotonic sequence numbers.

Input:
[1, 2, 3, 4, 5, 6]
Output:
Increasing.
Input:
[6, 5, 4, 3, 2, 1]
Output:
Decreasing.
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
Not a monotonic sequence!

A backslash at the end of a line tells Python to extend the current logical line over across 
to the next physical line.  See the Line Structure section of the Python reference documentation:

2.1.5. Explicit line joining
Two or more physical lines may be joined into logical lines using backslash characters (\), as follows:
when a physical line ends in a backslash that is not part of a string literal or comment, 
it is joined with the following forming a single logical line, deleting the backslash and the following 
end-of-line character. For example:

if 1900 < year < 2100 and 1 <= month <= 12 \
   and 1 <= day <= 31 and 0 <= hour < 24 \
   and 0 <= minute < 60 and 0 <= second < 60:   # Looks like a valid date
        return 1
There is also the option to use implicit line joining, by using parentheses or brackets or curly braces;
Python will not end the logical line until it finds the matching closing bracket or brace for each opening
bracket or brace. This is the recommended code style, the sample you found should really be written as:

if ((i < len(words_and_emoticons) - 1 and item.lower() == "kind" and
        words_and_emoticons[i+1].lower() == "of") or
        item.lower() in BOOSTER_DICT):
    sentiments.append(valence)
    continue

See the Python Style Guide (PEP 8) (but note the exception; 
some Python statements don't support (...) parenthesising so backslashes are acceptable there).

Note that Python is not the only programming language using backslashes for line continuation; 
bash, C and C++ preprocessor syntax, Falcon, Mathematica and Ruby also use this syntax to extend lines; 
see Wikipedia.

'''

#License: https://bit.ly/3oLErEI
def test(nums):
    
    #Highly compact return statement using backslash
    return "Increasing." if all(nums[i] < nums[i + 1] for i in range(len(nums) - 1)) else \
        "Decreasing." if all(nums[i + 1] < nums[i] for i in range(len(nums) - 1)) else \
        "Not a monotonic sequence!"


nums = [1,2,3,4,5,6]
print("Original list:")
print(nums)
print("Check the direction ('increasing' or 'decreasing') of the said list:")
print(test(nums))
nums = [6,5,4,3,2,1]
print("\nOriginal list:")
print(nums)
print("Check the direction ('increasing' or 'decreasing') of the said list:")
print(test(nums))
nums = [19,19,5,5,5,5,5]
print("\nOriginal list:")
print(nums)
print("Check the direction ('increasing' or 'decreasing') of the said list:")
print(test(nums))
