from collections.abc import Container


class MyContainer(Container):

    def __init__(self, value):
        self.data = value

    def __contains__(self, value):
        return value in self.data
    

xpto = MyContainer('jean')

print('a' in xpto)
print('z' in xpto)
print(isinstance(xpto, Container))