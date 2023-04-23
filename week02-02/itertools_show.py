"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/11 15:40
# @Author:YiShouquan
# @File:itertools_show.py
# @Update:
"""
import itertools  # 所有的返回都是genertor迭代器
import random
from dataclasses import dataclass

# some_names =['Jhon','Tom','Mike']
# some_attributs = [1165,2341,165431,4965,4865]
# some_level =['level','high','low']
#
# for z in zip(some_names,some_attributs,some_level):
#     print(z)

some_names = ['GRU', 'CNN', 'LSTM']
lr = [1e-3, 1e-4, 1e-5, 1e-6]
gamma = [1e-3, 1e-2, 1e-1]


# set{A} X set{B}  笛卡尔乘积
@dataclass
class Model:
    lr: float
    gamma: float


class CNN(Model):
    pass


class GRU(Model):
    pass


class LSTM(Model):
    pass


def run_a_model(model_name, lr, gamma):
    model_name_mapping = {
        'GRU': GRU,
        'CNN': CNN,
        'LSTM': LSTM
    }
    print(f"running model {model_name} as{lr}{gamma}")
    acc = model_name_mapping[model_name](lr, gamma)
    print(acc)


if __name__ == '__main__':

    # for p in itertools.product(some_names, lr, gamma):
    #     # print(p)
    #     run_a_model(*p)

    for n in itertools.permutations(some_names):  # 进行全排列
        print(n)

    for n in itertools.permutations(some_names, r=2):  # 取两个进行全排列
        print(n)
    print("*" * 8)
    for n in itertools.combinations(some_names, r=2):
        print(n)

    ### group by

    mock_login = ['uid54161', 'uid465654', 'uid642165'] * 10
    random.shuffle(mock_login)
    print(mock_login)
    for g, elements in itertools.groupby(mock_login):
        print(g, list(elements))

    for g, elements in itertools.groupby(mock_login, key=lambda n: int(n[-1]) % 2):  # 末尾通过奇偶数进行分类
        print(g, list(elements))

    numbers = [11, 165, 1, 113.1, 5610, 2, 48, 461, 456, 185]
    # 从0开始到n
    # 返回最大值和最小值max   min
    print(list(itertools.accumulate(numbers, max)))
    print(list(itertools.accumulate(numbers, min)))
    print(list(itertools.accumulate(numbers, lambda x, y: x + y)))

    for i in itertools.tee(numbers, 2):
        print(list(i))

    lines = open('itertools_show.py').readline()
    for lines_copy in itertools.tee(numbers, 2):
        for line in lines_copy:
            print(line)
