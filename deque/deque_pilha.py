from collections import deque

class Pilha:
    
    
    def __init__(self) -> None:
        self.lista = deque()

    
    def insere(self, val):
        self.lista.append(val)

    
    def remove(self):
        return self.lista.pop()
    

    def __repr__(self) -> str:
        return 'Pilha [{}]'.format(', '.join(str(x) for x in self.lista))
    

p = Pilha()
p.insere(10)
print(p)
p.insere(99)
print(p)
p.insere('xpto')
print(p)
p.remove()
print(p)