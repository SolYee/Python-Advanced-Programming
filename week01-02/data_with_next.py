"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/3/31 11:41
# @Author:YiShouquan
# @File:data_with_next.py
# @Update:
"""


class Data:
    def __init__(self, initialized):
        self.index = 0
        for i in initialized:
            self.update_db(i)
            self.index += 1

    def update_db(self, e):
        print(f'onnect db and update {e} with index')

    def retrieval_db(self, i):
        print(f'based on {i} get data form db')

    def __next__(self):
        for i in range(self.index):
            yield self.retrieval_db(i)

# data = Data([1,2,3,4,5])

# for d in data:
#     print(d)