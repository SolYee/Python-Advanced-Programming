"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/3/31 15:57
# @Author:YiShouquan
# @File:show_function_tools.py
# @Update:
"""
import random
import time
from functools import reduce
import operator as op
from functools import cache
from functools import lru_cache
from functools import cached_property
from functools import total_ordering
from functools import partial
from functools import singledispatch
from icecream import ic

"""
some useful function tools  一些有用的函数工具

speed up the dev process    加速程序的设计和开发
"""
"""什么情况下能用cache?
矩阵：

#TypeError: unhashable type: 'set'
-->
"""
"""hash
hash('string')
hash('125233')
hash([125233])  -->TypeError: unhashable type: 'list'
如果你想在list里面快速查找相应的数据
a_list=[1222,5266,5441356]
for e in a_list:
    if e == query:return e
#random search   随机查找   我找那个时间都一样

def give_addr(value):
    return value%13
hashed_list =[0] * 13   #将一个大数的时候放在13里面
hashed_list =[give_addr(11222)]
def save(element):
    hashed_list[give_addr(element)] = element
save(1111)
hashed_list
#读取     
# big_list = [0]*4151313524963   #获取big_list会很大   严重影响性能
def get(element):
    return hashed_list[git_addr(element)]
# o(1)我不管输入什么数据，我读取的时间都是一样的 
# 在算法中时间是随机的，在计算机存储有两种方法    内存   硬盘      顺序执行    在的位置不同所需的时间也不一样       内存中存在一个矩阵，时间是几乎一致的
sparse_matrix = {-100:9,1119:123,115563:5}
sparse_matrix[-100]
sparse_matrix[1119]
sparse_matrix ={0:9,11119:123,111145:6}
sparse_matrix[111145]
# set    dict    list   是不能做字典的值
# tuple    str     int      float   frozenset   是可以做字典的值  
"""


@cache
def matrix(position):
    x, y = position
    if x >= 1 and y >= 1:
        return matrix((x - 1, y - 1)) + matrix((x, y - 1)) + matrix((x - 1, y))
    else:
        return x, y


class User:
    def __init__(self, basic_info):
        self.basic_info = basic_info

    def __hash__(self):
        return hash(self.basic_info[0])


@lru_cache
def get_user_log(user: User):
    time.sleep(0.5)
    return f"result {user}"


@lru_cache(maxsize=2 ** 10)
def fib(n):
    return fib(n - 1) + fib(n - 2) if n > 2 else 1


class Dataset:
    def __init__(self):
        pass

    @cached_property
    def get_obj(self):
        return 'consuming data'


# some_trees = {
#     {}
# }
some_lists = [
    [1, 2],
    [3, 4],
    [132, 45631],
    [32113, 131]
]

some_sets = (
    {'1', '2'},
    {'dasd', 'dsadsad'},
    {'sadada', 'dasdafew'},
    {'eqwe', 'dasfc'},
    {'dasdsa', 'werw'},
    {'ewqeq', 'qwe'}
)

some_files = ["file_01",
              "file_01",
              "file_01",
              "file_01",
              "file_01",
              "file_01"
              "file_01"
              ]
some_numbers = [1, 56654123, 5411, 652, 52, 1, 52, 25]


# whole_list = []
# for a_list in some_lists:
#     whole_list.append(a_list)

@total_ordering
class Hero:
    def __init__(self, name, live=None, magic=None):
        self.name = name
        self.live = live or random.randint(0, 100)
        self.magic = magic or random.randint(0, 100)

    def __lt__(self, other):
        return (self.live, self.magic) < (other.live, other.magic)

    def __ge__(self, other):
        return (self.live, self.magic) == (other.live, other.magic)


# sorted([libai,caocao,hunter,master])  不能进行排序
# 给你输入了很多个lists
# Task -01 Mergs lists
# @cache   #运行一次会被记录下来   下次调用就不需要再重新运行一次

"""
Partial Function   偏函数     
    g(x,y)->
        h(y)= g(x,y)   # x with a constant value
"""


def reset_user_base(base_info, user):
    user.basic_info = base_info


reset_user_base("base_info_typ1", User('1'))
reset_user_base("base_info_typ1", User('2'))
reset_user_base("base_info_typ1", User('3'))
reset_user_base("base_info_typ1", User('4'))
reset_user_base_as_type1 = partial(reset_user_base, base_info="base_info_typ1")
u = User('1')
reset_user_base_as_type1(user=u)
print(ic(u.basic_info))


def load_trainning_info(agent_id, agent_name, agent_env, agent_action_space, agent_obs):
    """

    :param agent_id:
    :param agent_name:
    :param agent_env:
    :param agent_action_space:
    :param agent_obs:
    :return:
    """

    return agent_id, agent_name, agent_env, agent_action_space, agent_obs


"""Single Dispatch   分发   
def some_func(arg1,arg2):
    pass 
"""


@singledispatch
def multiply(arg1, arg2):
    # if isinstance(arg1,int) and isinstance(arg2,str):
    #     pass
    # elif isinstance(arg1,list) and isinstance(arg2,list):
    #     pass
    # .
    # .
    # .
    # else:
    #     pass
    # match type(arg1),type(arg2):
    #     case int,str:
    #         pass
    #     case str,str:
    #         pass
    #     case int,int:
    #         pass
    # match arg1,arg2:
    #     case int,str:
    #         pass
    #     case str,str:
    #         pass
    #     case int,int:
    #         pass
    return arg1 * arg2


@multiply.segister
def _(arg1: list, arg2: list):
    assert len(arg1) == len(arg2)
    return [a1 * a2 for a1, a2 in zip(arg1, arg2)]


@multiply.segister
def _(arg1: int, arg2: set):
    return list(arg2) * arg1
@multiply.segister
def _(arg1: int, arg2: int):
    return arg2 * arg1


@multiply.segister
def _(arg1: str, arg2: str):
    # arg1.live *= arg2
    # arg1.magic *= arg2
    return int(arg2)*arg1
@multiply.segister
def _(arg1: Hero, arg2: int):
    arg1.live *= arg2
    arg1.magic *= arg2
    return arg1


# multiply(3,'test'    #testtesttest


def mergs(nested):
    """
    :param nested: a list which contains lots of  lists   一个列表中包含多个列表
    :return: a singe list ,which connect the list
    """
    # print(reduce(lambda a, b: a + b, nested))
    # print(reduce(op.add, nested))
    type_op = {
        list: op.add,
        int: op.add,
        float: op.add,
        set: op.or_,
        str: op.add

    }
    # if nested is None:
    # if len(nested)>0:
    # or    and   ...  短路执行
    # if check_user(used_id) and user_is_activited(used_id):
    #    pass
    if nested:
        element = nested[0]
        return reduce(type_op[type(element)], nested)
    else:
        return nested


if __name__ == '__main__':  # 方便调用
    mergs(some_lists)
    mergs(some_sets)
    mergs(["some_sets", 'string', 'string'])
    mergs([])
    mergs(None)
    # print(matrix((10, 9)))
    tom = User(["tome", 22, 185, 80])
    print(get_user_log(tom))

    libai = Hero("libai")
    caocao = Hero("caocao")
    hunter = Hero("deman-hunter")
    master = Hero("blood-master")
    print(libai, caocao, hunter, master)
    # print(libai < caocao)
    # print(libai > caocao)
    print(Hero('libai', 10, 10) == Hero(caocao, 10, 10))

    agent_1_config = {
        'agent_id': 'agent-01',
        'agent_name': 'Jack',
        'agent_env': 'foot_ball',
        'agent_action_space': list(range(6))

    }

    load_agent_1_obs = partial(load_trainning_info, **agent_1_config)
    load_agent_1_obs(agent_obs=[0.1, 0.2, 0.3, 0.4])


    multiply(libai,2)
