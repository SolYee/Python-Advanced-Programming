"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/3/31 10:46
# @Author:YiShouquan
# @File:map_filter_show.py
# @Update:
"""
import random
from icecream import ic


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Task-->Person.age += 1


persons = [Person('test', random.randint(2, 10)) for _ in range(10)]
print(persons)


def add_age(p):
    p.age += 1
    return p.age

# for i in map(add_age,persons):   #==> for p in persons: r=add_age(p)     #map的返回值是generator
#     print(i)
# persons = [p.age + 1 for p in persons]
# print(persons)
r = map(add_age,persons)
print(next(r))
print(next(r))
print(next(r))

def reverse_name(p):
    p.name = p.name[::-1]
    return p


# # returned = reverse_name(add_age) for p in persons
# returned = map(reverse_name,
#                map(add_age,reverse_name)
#               )
returned = filter(lambda n: n >= 50,
                  map(lambda n: n ** 2,
                      map(lambda p: p.age, persons)
                      )
                  )
# for r in returned:
#     print(r)
ic(list(returned))     #使用generator需要使用list强行转换显示

for i in map(add_age, persons):  # ==> for p in persons: r=add_age(p)      #map的返回值是genertor
    print(i)


# persons = [p.age + 1 for p in persons]
# print(persons)



def simple_yield():
    yield 'one'
    yield 'towe'
    yield 'three'
    yield 'end'
g=simple_yield()
# next(g)
# next(g)
# next(g)
# next(g)