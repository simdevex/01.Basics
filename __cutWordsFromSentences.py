'''
Internet search engine giant, such as Google accepts web
pages around the world and classify them, creating a huge
database. The search engines also analyze the search keywords
entered by the user and create inquiries for database search. In
both cases, complicated processing is carried out in order to
realize efficient retrieval, but basics are all cutting out words from
sentences.

Write a Python program to cut out words of 3 to 6 characters
length from a given sentence not more than 1024 characters. 
For exaple in, sentence, do, will be removed, because they are not between 3 and 6 charecters

Input:
English sentences consisting of delimiters and alphanumeric
characters are given on one line.
Input a sentence (1024 characters. max.)
The quick brown fox
3 to 6 characters length of words:
The quick brown fox

'''

print("Input a sentence (1024 characters. max.)")
yy = input()
yy = yy.replace(",", " ")
yy = yy.replace(".", " ")
print("3 to 6 characters length of words:")

'''
Using * in front of a list expands out the members as individual arguments.
So, the following two function calls will be equivalent:
There is no problem to be solved using a dictionary

print(*[y for y in yy.split() if 3 <= len(y) <= 6])
There solved using

print([y for y in yy.split() if 3 <= len(y) <= 6])
['There', 'solved', 'using']

'''
print(*[y for y in yy.split() if 3 <= len(y) <= 6])
