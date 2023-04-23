"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/14 17:30
# @Author:YiShouquan
# @File:show_scope.py
# @Update:
"""
def solution(num: int)-> int:
    # your code here
    st = str(num)
    li = list(st)
    for i in range(len(li)):
        if li[i:i+3]==["7","9","7"]:
            li.pop(i+1)
    return int("".join(li))

assert solution(797) == 77
assert solution(7979797) == 7777
assert solution(165561786121789797) == 16556178612178977


