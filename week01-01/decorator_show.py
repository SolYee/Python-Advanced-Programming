"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/3/31 14:43
# @Author:YiShouquan
# @File:decorator_show.py
# @Update:
"""
from functools import cache


def memory(f):
    memory.cache = {}

    def _wrap(*args, **kwargs):
        if args in memory.cache:
            print(f'hit{args}')
            return memory.cache(args)

        else:
            r = f(args)
            memory.cache[args] = r
            return r

    #         return f(n)
    return _wrap


# def change_result_to_none(f):
#     def _wrap(args):
#         return None
#     return _wrap

def buttons(c):
    def button(f):
        def _wrap(*a, **kwargs):
            r = f(*a, **kwargs)
            print(f'press keyboard {c}')
            return r

        return _wrap

    return button


buttons_s = {
    c: buttons(c) for c in "quert"
}


@buttons_s["q"]
# # @change_result_to_none
# @memory
# # @cache
def fib(n):
    return fib(n - 1) + fib(n - 2) if n >= 2 else 1


if __name__ == '__main__':
    #     print(memory(fib(5)))
    #     fib=memory(fib)
    print(fib(5))


#
# def flatten(elements):
#     match elements:
#         case []: return []
#         case list() | tuple() | set() as first, *remains:
#             return flatten(first) + flatten(remains)
#         case _: return [elements[0]] + flatten(elements[1:])
#
#
# if __name__ == '__main__':
#     simple = [0, 1, (2, 3)]
#     L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']
#     nest = [(0, 1), (2, 3), 4, 5, ((6, 7, 8), ((9, 10), ((11, 12, ((13, 14), 15), 16), 17)))]
#
#     print(flatten(simple))
#     print(flatten(L))
#     print(flatten(nest))