'''
Python program to convert seconds to day, hour, minutes andseconds.
'''

time = float(input("Input time in seconds: "))
print ("Time 00 ", time)
day = time // (24 * 3600)
print ("Day ", day )
time = time % (24 * 3600)
print ("Time 01 ", time )
hour = time // 3600
print ("Hour ", hour )
time %= 3600
print ("Time 02 ", time )
minutes = time // 60
print ("Minutes ", minutes )
time %= 60
print ("Time 03 ", time )
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
