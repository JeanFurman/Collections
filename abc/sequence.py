from collections.abc import Sequence


class MySequence(Sequence):
    def __init__(self, seq):
        self.seq = seq

    # def __contains__(self, val):
    #     return val in self.seq
    
    # def __iter__(self):
    #     return iter(self.seq)
    
    def __len__(self):
        return len(self.seq)
    
    def __getitem__(self, pos):
        return self.seq[pos]

s = Sequence([1, 2, 3, 4])

print(1 in s)

for x in s:
    print(x)

print(len(s))
