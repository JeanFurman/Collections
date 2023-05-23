from collections import UserDict


class MyDict(UserDict):
    def __lshift__(self, value):
        self.data['last'] = value
    def __setitem__(self, key, value):
        super().__setitem__(key, value *2)

xpto = MyDict()

xpto['jean'] = 22
xpto << 77
print(xpto)
