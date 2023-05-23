from collections import deque


cache_values = deque(maxlen=3)


def cache(func):
    def inner(*args):
        cache_values.append(args)
        return func(*args)
    return inner


@cache
def soma(x, y):
    return x + y


print(soma(1, 1))
print(cache_values)
print(soma(9, 17))
print(cache_values)
print(soma(10, 10))
print(cache_values)
print(soma(5, 88))
print(cache_values) 
cache_values.rotate(2)
print(cache_values)
cache_values.rotate(-1)
print(cache_values)