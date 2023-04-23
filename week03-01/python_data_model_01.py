"""python最容易忽略的model
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/13 14:25
# @Author:YiShouquan
# @File:python_data_model_01.py
# @Update:
"""
"""Programming= Data Structure + AIgorithm"""

"""
问题描述:两只羊,两栏蔬菜,一个人.从A移动到B
"""
"""数据有很多中表现方式.在任何情况下,数据表示在哪里更适合
LIST:可修改,长度大小可变    下标修改内容     append 追加    pop
TUPLE:不可修改
DICT:可扩展性强
"""
"""在计算机内存中,同样的位置的数据声明的类型不一样,表示出来的也不一样
"""


def add(a, b): return a + b


# class Vector:
#
#     def __init__(self, *args):
#         self._list = list(args)
#
#     def __add__(self, other):
#         assert isinstance(other, Vector), f'unsupported vector typle {Vector}'
#
#         return [self._list[i] + other[i] for i in range(len(other))]
#
#     def __getitem__(self, item):
#         return self._list[item]
#
#     def __len__(self):
#         return len(self._list)

class Vector:

    def __init__(self, *args):
        self._list = list(args)

    def __add__(self, other):
        if isinstance(other, (Vector, tuple, list)):

            return [self._list[i] + other[i] for i in range(len(other))]

        else:
            return str(self) + str(other)

    def __getitem__(self, item):
        return self._list[item]

    def __len__(self):
        return len(self._list)

    def __repr__(self):
        return str(self._list)


class SameleBatch(dict):
    """
    'agent':[obs,obs,obs,....obs]
    """
    AGENT = 'agent'
    PERIOD = 'period'

    def __add__(self, other):
        for key, value in self.items():
            if key in other:
                self[key] += other[key]
        return self


vec1 = Vector(1, 2, 3, 4)
vec2 = Vector(-1, -2, -3, 4)
print(add(vec1, vec2))
print(add('I am a', ' good boy'))
agent = SameleBatch.AGENT
period = SameleBatch.PERIOD
sb = SameleBatch(agent=1, period=3)
sb2 = SameleBatch(agent=10, period=30)
print(sb)
print(sb[SameleBatch.AGENT])
print(sb[SameleBatch.PERIOD])
print(add(sb, sb2))
print(add(Vector(0, 1, 2), (-10, -9, -8)))
print(add(Vector(0, 1, 2), [-10, -9, -8]))
print(add(Vector(0, 1, 2), 'some other'))

"""Duck typing   鸭子类型
"""
from collections import namedtuple
import random
Card = namedtuple('Card', ['number', 'shape'])


class Poker:
    numbers = '23456789TJQKA'
    shapes = '♥♣♠♦'
    joker = '大王 小王'.split()

    def __init__(self):
        self._cards = [Card(n, s) for n in Poker.numbers for s in Poker.shapes]
        self._cards.append(Card(15, Poker.joker[0]))
        self._cards.append(Card(16, Poker.joker[1]))

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key] = value

    def __repr__(self):
        return str(self._cards)


if __name__ == '__main__':
    deck = Poker()
    print(len(deck))
    print(deck[19])
    print(deck[10:19])

    print('*'*8)
    for _ in range(8):
        print(random.choice(deck))

    random.shuffle(deck)
    print(deck)



