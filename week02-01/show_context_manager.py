"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/3/31 15:21
# @Author:YiShouquan
# @File:show_context_manager.py
# @Update:
"""
"""  
Context  Manager
E.g:
    open a file    打开一个文件
    connect a dataset    链接一个数据库
    process images or some big files   对图片或者文件进行处理
    
    
    => Manaage  the   resource
"""
from  contextlib import  contextmanager


@contextmanager   #将下面的connect_database类改写成
def connect_database(url):
    obj = open(url,'r')
    try:
        print('enter the obj')
        yield obj

    finally:
        print("exit the obj")
        obj.close()
"""file = open("show_context_manager.py")
# connect a dataset
try:
    file.write("\n#newline")
finally:
    
    file.close()"""

class Processer:
    def __init__(self,filename):
        self.file = filename

    def __enter__(self):
        try:
            print('initialize {}'.format(file))
            self.fileobj = open(self.file)
            return self.file
        except FileNotFoundError as e:
            self.fileobj = None
            print('file not exists')


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.fileobj:
            print('file not find')
        else:

            self.file.close()

with  Processer('show_context_manager.py') as file:
    pass




# with open("show_context_manager.py") as file:
#     files.write("\n#newline")

with connect_database("show_context_manager.py") as c:
    print(c.read())