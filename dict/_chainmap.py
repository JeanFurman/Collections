from collections import ChainMap


a = {1: 'a', 2: 'b', 3: 'c'}
b = {2: 'x', 3: 'z', 4: 'w'}

c = ChainMap(a, b)
print(c.maps[0][1])
print(c.maps[1][3])