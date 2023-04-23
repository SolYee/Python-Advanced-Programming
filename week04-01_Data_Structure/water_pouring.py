"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/20 9:49
# @Author:YiShouquan
# @File:water_pouring.py
# @Update:
"""
"""
大杯子90ml,小杯子40ml,如何得到50ml/60ml的水
"""
from collections import defaultdict
from icecream import ic

some_elements = list()


def append(e, elements):
    return elements.append(e)


def get(elements):
    # return elements.pop(-1)  # pop(-1)
    return elements.pop(0)  # pop(0)  即获得下标为0的数然后删掉该数值    LIST -->pop(0):队列   pop(-1):堆栈


nested_tree = {
    'a': {
        'a1': {
            'b1': -1,
            'b2': {'b21': {'b211': 0,
                           'b212': -1}}
        },
        'a2': {'c1': -2,
               'c2': {'c21': {'c211': 0,
                              'c212': 1}}},
        'a3': {'d1': -3,
               'd2': {'d21': {'d211': 2,
                              'd212': 3}}},
        'a4': {'e1': -4,
               'e2': {'e21': {'e211': 4,
                              'e212': 5}}
               }
    }
}


# print(nested_tree)


def get_connect_graph(tree):
    connect_graph = defaultdict(list)
    for node, connect in tree.items():

        if isinstance(connect, dict):
            for k in connect:
                connect_graph[node].append(k)
            connect_graph |= get_connect_graph(connect)  # |=  或等于   更新的符号
        else:
            connect_graph[node].append(connect)
    return connect_graph


def get_next(a, b, A, B):
    """

    :param a: current water amount in cup a  # 杯中当前水量a
    :param b: current water amount in cup b  # 杯中当前水量b
    :param A: capacity of cup A   杯子的容量A
    :param B: capacity of cup B   杯子的容量B
    :return: the next possible state
    """
    next_state = {
        'a->p': (0, b),
        'b->p': (a, 0),
        'p->a': (A, b),
        'p->b': (a, B),
        'a->b': (a + b - B, B) if a + b > B else (0, a + b),
        'b->a': (A, a + b - A) if a + b > A else (a + b, 0)
    }
    return next_state


def search(a, b, A, B, target=None):
    # need_visit = [begin]
    paths = [[('init', (a, b))]]
    seen = set()
    # while need_visit:
    while paths:
        # ic(paths)
        # path = paths[0]
        # node = get(need_visit)
        path = get(paths)
        state = path[-1][-1]
        if state in seen: continue
        for action, next_s in get_next(*state, A, B).items():
            # for next_ in connect_g[node]:
            # need_visit.append(next_)
            paths.append(path + [(action, next_s)])
            if target in next_s:
                return paths[-1]
            # paths.append(path)
            seen.add(state)
            # seen.add(node)
            # if node == target:
            #     print(f'target is found:{node}')
            # print(f'i have looked up {node}')
            paths = sorted(paths, key=len)


def matter_match(names):
    match names:
        case [first,*middle,last] if len(middle) <3:
            print(f'{first} and {last} have some few friends')
        case [first, *middle, last] if len(middle) >= 5:
            print(f'{first} and {last} have some few friends,they got {len(middle)}')
        case _:
            print('just two boys')



connect_graph = get_connect_graph(nested_tree)
# search(begin='a', connect_g=connect_graph, target='c211')
ic(search(a=0, b=0, A=90, B=50, target=60))
ic(search(a=0, b=0, A=90, B=50, target=70))
