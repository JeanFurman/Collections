from myABC import Functor

class MyFunctor(Functor):
    
    def __init__(self, list_):
        self._d = list_

    def __getitem__(self, pos):
        return self._d[pos]

    def __len__(self):
        return len(self._d)

    def fmap(self, function):
        return [function(x) for x in self._d]
    