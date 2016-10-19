from functools import partial
from itertools import groupby

class Infix(object):
    def __init__(self, func):
        self.func = func
    def __or__(self, other):
        return self.func(other)
    def __ror__(self, other):
        return Infix(partial(self.func, other))
    def __call__(self, v1, v2):
        return self.func(v1, v2)

class Postfix(object):
  def __init__(self, func):
    self.func = func
  def __ror__(self, other):
    return self.func(other)
  def __call__(self, v1):
    return self.func(v1)        

@Infix
def Filter(data, func):
    return list(filter(func,data))

@Infix
def Map(data, func):
    return list(map(func,data))

@Infix
def ItemAt(data, index):
    return data[index]

@Infix
def GroupBy(data, label):
    groups = []
    for k, g in groupby(data, lambda x: x[label]):
        groups.append(list(g))
    return groups

@Postfix
def Unique(data):
    return set(data)