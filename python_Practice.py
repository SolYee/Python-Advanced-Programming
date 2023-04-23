"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/9/22 14:11
# @Author:YiShouquan
# @File:python_Practice.py
# @Update:
"""
# 练习一：
from numpy import equal


# from venv.Lib.re import search

# equal(pattern="abc", string='abc')
# equal(pattern="ab+c", string='abbc')
# equal(pattern="a+", string='aaa')


# search(pattern="ab+",string='this is an absolutely diffifult problem')
# match(pattern="ab+",string='absolutely')  -->test if this pattern exists on the  string begining

def match(pattern, string):
    for i in range(len(string)):
        if equal(pattern='a+', string=string[i:]):
            return string[i:]
    return None

def match(pattern, string):
    for i in range(len(string)):
        if equal(pattern, string=string[i:]):
            return string[i:]

def search(pattern, string):
    for i in range(len(string)):
        m = match(pattern, string[i:])
        if m:
            return m


def equal_1(pattern, string):
    return pattern == string or pattern == '.'
    # if pattern == string:return True
    # elif pattern=='.':
    #     return  True
    # else:
    #     return False
