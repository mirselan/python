"""
# Задание_1
list_1 = [[1, 2, 4], [7, 5, 3], [5, 6, 8]]
list_2 = [[8, 1, 9], [6, 7, 9], [4, 8, 6]]


class Matrix:
    def __init__(self, list_new):
        self.list_new = list_new

    def __str__(self):
        return '\n'.join(map(str, self.list_new))

    def __add__(self, other):
        list_3 = []
        for a in range(len(self.list_new)):
            list_3.append([])
            for b in range(len(self.list_new[0])):
                list_3[a].append(self.list_new[a][b] + other.list_new[a][b])
        return '\n'.join(map(str, list_3))


m1 = Matrix(list_1)
m2 = Matrix(list_2)
print(m1, '\n')
print(m2, '\n')
print(m1 + m2)

"""
"""
# Задание_2
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def cost(self):
        ...

    def __add__(self, other):
        return self.cost + other.cost


class Coat(Clothes):

    @property
    def cost(self):
        return round(self.param / 6.5) + 0.5


class Suit(Clothes):

    @property
    def cost(self):
        return (2 * self.param + 0.3) / 100


coat = Coat(41)
suit = Suit(180)
print(coat + suit)

"""
# Задание_3 сделать не успел до дедлайна
