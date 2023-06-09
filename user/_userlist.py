from collections import UserList


class MyList(UserList):
    def __add__(self, value):
        if isinstance(value, list):
            return super().__add__(value)
        else:
            self.data.append(value)
    
    def __sub__(self, value):
        if value in self.data:
            self.data.remove(value)
        else:
            pass

l = MyList()
print(l)
l + 40
print(l)
l + 99
print(l)
l + 103
print(l)
l - 40
print(l)