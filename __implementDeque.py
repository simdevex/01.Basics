'''
Implement deque
'''

import collections
x = collections.deque()

x.append(10)
x.appendleft(3)
print(x)

x.extend([100, 200, 300])
x.extendleft([3, 2, 1])
print(x)

x.pop()
x.popleft()
print(x)

x.rotate(3)
print(x)

x.rotate(-1)
print(x)