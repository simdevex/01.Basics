'''
Python program to get all strobogrammatic numbers that are of length

A strobogrammatic number is a number whose numeral is
rotationally symmetric, so that it appears the same when rotated
180 degrees. In other words, the numeral looks the same rightside
up and upside down (e.g., 69, 96, 1001).
For example,
Given n = 2, return ["11", "69", "88", "96"].
Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609',
'888', '181', '986', '689']

'''

#https://github.com/keon/algorithms/blob/master/math/generate_strobogrammtic.py

from numpy import result_type


def gen_strobogrammatic (n):
    """
    :type n: int
    :rtype: List [str]
    """
    
    result = helper (n,n)
    return result

def helper (n, length):
    if n == 0:
        return [""]
    if n == 1:
        return ["1", "0", "8"]
    middles = helper (n-2, length)
    result = []
    for middle in middles:
        if n != length:
            result.append ("0" + middle + "0")
        result.append ("8" + middle + "8")
        result.append ("1" + middle + "1")
        result.append ("9" + middle + "6")
        result.append ("6" + middle + "9")
    return result
print ("n = 2: \n" , gen_strobogrammatic(2))
print ("n = 3: \n" , gen_strobogrammatic(3))
print ("n = 4: \n" , gen_strobogrammatic (4) )        