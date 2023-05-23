from collections import deque

class Fila:
    
    
    def __init__(self) -> None:
        self.lista = deque()

    
    def insere(self, val):
        self.lista.append(val)

    
    def remove(self):
        return self.lista.popleft()
    

    def __repr__(self) -> str:
        return 'Fila [{}]'.format(', '.join(str(x) for x in self.lista))
    

f = Fila()
f.insere(10)
print(f)
f.insere(99)
print(f)
f.insere('xpto')
print(f)
f.remove()
print(f)