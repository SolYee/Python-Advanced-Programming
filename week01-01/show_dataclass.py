"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/3/31 10:29
# @Author:YiShouquan
# @File:show_dataclass.py
# @Update:
"""

# persons=[]

# person = namedtuple("Person","name age location weight".split())

# # class  OldPerson:
# #     def __init__(self,name="tom",age=20,location=180.0,weight=20.0):
# #         self.name = name
# #         self.age = age
# #         self.location = location
# #         self.weight = weight

# #     def __repr__(self):
# #         return f"Person(name={self.name}, age={self.age}, location={self.location}, weight={self.weight})"

# # person = OldPerson()
# # print(person)
# person.age =10
# person.name='name'

from dataclasses import dataclass


@dataclass
class Person:
    name: str = ""
    age: int = 18
    location: float = 18.5
    weight: float = 20.0


person = Person()
print(person)
person.name = "jack"
person.age = 19
print(person)