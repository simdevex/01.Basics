'''
Python program to find the name of the oldest student from a given dictionary 
containing the names and ages of a group of students.

Sample Input:
{"Bernita Ahner": 12, "Kristie Marsico": 11, "Sara Pardee": 14,
"Fallon Fabiano": 11, "Nidia Dominique": 15}
{"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, "Sofia Park": 12.4,
"Joannie Archibald": 12.6, "Becki Saunder": 12.7}
Sample Output:
Nidia Dominique
Becki Saunder
'''

def oldest_student(students):
    '''
    max() for iterables
    max(iterable, *[, key, default])
    Where,

    iterable - sequence or collection whose largest item is to be returned.
    key (optional) - It is a function to which iterables are passed and the comparison is done based on the value returned by this function.
    default (optional) - default value that specifies an object to return in case of empty iterable. 
    If a default value is not given when empty iterable is passed, ValueError will be raised.
    When an iterable is passed as the argument, the largest item of the iterable is returned. 
    If multiple iterables are passed then, the list for which the key function return greater value is returned.
    # using max(arg1, arg2, *args, key)
    print('Number with max remainder is:', max(11,48,33,17,19, key=findMax))

    # using max(iterable, key)
    num = [11,48,33,17]
    print('Number with max remainder is:', max(num, key=findMax))
    '''
    return max(students, key=students.get)

print(oldest_student({"Bernita Ahner": 12, "Kristie Marsico": 11, 
                      "Sara Pardee": 14, "Fallon Fabiano": 11, 
                      "Nidia Dominique": 15})) 
print(oldest_student({"Nilda Woodside": 12, "Jackelyn Pineda": 12.2, 
                      "Sofia Park": 12.4, "Joannie Archibald": 12.6, 
                      "Becki Saunder": 12.7})) 
