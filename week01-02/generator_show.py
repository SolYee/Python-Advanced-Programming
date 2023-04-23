"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/3/31 10:30
# @Author:YiShouquan
# @File:generator_show.py
# @Update:
"""
import time
from collections import defaultdict
import datetime

# 统计一个文件的里面的单词数量
def count_words(filename):
    counts = defaultdict(int)

    time.sleep(1)
    return counts


def get_all_results(files):
    return (count_words(f) for f in files)
    #     return [count_words(f) for f in files]
#     """
#     results = []
#     for f in files:
# #         results.append(count_words(f))
#         yield count_words(f)
#         """


def update_remote_db(k, v):
    pass


def collect_results(files):
    results = defaultdict(int)

    for c in get_all_results(files):
        print(f"get one {datetime.datetime.now()}")
        for k, v in c:
            update_remote_db(k, v)
            results[k] += v


if __name__ == '__main__':

    files = ['some_file'] * 5
    print(f"grogramming running at {datetime.datetime.now()}")
    collect_results(files)


