from collections import deque

class Lista:
    
    
    def __init__(self) -> None:
        self.lista = deque()

    
    def insere(self, val, pos=None):
        if pos:
            self.lista.insert(val, pos)
        else:
            self.lista.append(val)

    
    def remove(self, val):
        return self.lista.remove(val)
    

    def __repr__(self) -> str:
        return 'Lista [{}]'.format(', '.join(str(x) for x in self.lista))
    

lista = Lista()
lista.insere(99)
print(lista)
lista.insere(100)
print(lista)
lista.insere(0, 2)
print(lista)
lista.insere(1, 'Jean')
print(lista)