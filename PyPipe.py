from functools import partial

class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def Filter(data, func):
    return list(filter(func,data))

@Infix
def Map(data, func):
    return list(map(func,data))    

@Infix
def ItemAt(data, index):
    return data[index]        