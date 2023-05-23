from collections import Counter

s = 'batatinha quando nasce espalha rama pelo chão'

print(s.count('a'))

print(Counter(s))

l = [1, 2, 3, 5, 7, 8, 989898, 989, 00, 544, 334, 133, 55543, 87]

print(l.count(1))
print(Counter(l))

entrada = 'BBBBBBBBBBBBBBBBBBBBAACCCDD'

def comprimir(letras):

    l = Counter(letras)
    r = ''
    for a, b in l.items():
        if b>9:
            aux = b // 9
            for _ in range(aux):
                r += f'{a}{9}'
            r += f'{a}{b%9}'
        else:
            r += f'{a}{b}'
    return r


print(comprimir(entrada.upper()))