from itertools import chain, count


a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]

r = chain(a, b, c)
print(next(r))
print(next(r))
print(next(r))
print('------')
for x in r:
    print(x)
print(list(r))

c = count(1)

for f in range(100):

    print(next(c), sep=',', end='')