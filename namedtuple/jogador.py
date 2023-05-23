from collections import namedtuple


j = namedtuple('Jogador', 'nome time camisa n')
jean = j('Jean', 'São paulo', 11, 21)
print(jean)

n = namedtuple('ABC', 'slot1 slot2 slot3')
n1 = n([1, 2, 3, 4], 10, 'xpto')
print(n1)

naipes = 'P C O E'.split()
valores = list(range(2, 11)) + 'A J Q K'.split()
carta = namedtuple('Carta', 'naipe valor')
baralho = [carta(naipe, valor) for naipe in naipes for valor in valores]
print(baralho)