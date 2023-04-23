"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/3/31 14:39
# @Author:YiShouquan
# @File:python_args_and_kwargs.py
# @Update:
"""
# python_*args_and_**kwargs

def combine(elements):
    return sum(elements)


def configure(arguments):
    for k, v in arguments:
        print(k, v)


def configure_s(*args):
    print(args)


def configure_ks(**kwargs):
    print(kwargs)


def fuction_with_three_arguments(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def get_config_info():
    return ('length', 3), ('level', 3), ('security', 3)


def control_by_configure(length, level, security):
    print(length, level, security)


def function_with_arbitary_arguments(*args, **kwargs):
    print(args)
    print(kwargs)


if __name__ == '__main__':

    arguments = get_config_info()
    #     fuction_with_three_arguments(get_config_info())  #==>fuction_with_three_arguments(get_config_info()[0],get_config_info()[1],get_config_info()[2])
    fuction_with_three_arguments(*get_config_info())
    #     arguments = [('length',3),('level',3),('security',3)]
    #     fuction_with_three_arguments(arguments)  --->这个运行后会出现错
    #     configure(arguments)
    configure_s(('length', 3), ('level', 3), ('security', 3))

    configure_ks(length=3, level=4, security=10)

    configure_map = {
        "length": 3,
        "level": 3,
        "security": 10
    }
    control_by_configure(**configure_map)
    control_by_configure(length=3, level=3, security=10)

    function_with_arbitary_arguments(10, 20, 30,
                                     key=20, age=10, some=False)
