"""正则表达式
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/11 17:09
# @Author:YiShouquan
# @File:RegularExpression_re_show.py
# @Update:
"""
import re
import pandas as pd

# '\w'  --> 字符
# '\w+'  --> 一个或多个字符    '\w*'  --> 0个或多个字符
# '\W'  --> 所有的非文字
# '\d'  --> 数字
some_text = "i am a good man!"
print(re.findall('\w', some_text))
print(re.findall('\w+', some_text))

string = "'环球','commentnum','0','joinum'"
print(re.findall('[a-z]+', string))  # '[a-z]+'   a到z之间的所有字符
print(re.findall('[a-z\d]+', string))  # '[a-z\d]+'           '[a-z0-9]+'       a到z或者0-9
print(re.sub('[a-z\d\w]+', '', string))

string = "'环球','commen00t9999num','0','jo00inum'"
print(re.sub('(\d)', 'Num', string))
print(re.sub('(\d)', '\g<0>', string))
print(re.sub('(\d)', '#\g<0>#', string))
print(re.sub('[a-z\d\w]+', '', string))

chinese_string = "河南省与浙江省政府进行合作,河南经济将会有比较大的提升"
print(re.sub('(河南)\w+', '#\g<1>#:\g<0>', chinese_string))


def token(string):
    return re.findall('\w+', string)


def clean(string):
    return re.sub('[a-z\d\w]+', '', string)


file = open('sqlResult_1558435.csv', encoding='gb18030')
length = int(1e5)
"""Task-01:
Characters -->字符
"""
short_sample = open("short_sample", 'w')
for i, line in enumerate(file):
    if i >= length: break

    tokes = token(line.lower())
    print(tokes)
    short_sample.write(''.join(tokes) + '\n')
short_sample.close()
"""
Input:单词  多个单词
Output:包含该单词的所有句子并且用特殊的##进行高亮
"""


def read_and_write(file):
    for i, line in enumerate(file):
        if i >= length: break

        tokes = token(line.lower())
        print(tokes)
        short_sample.write(''.join(tokes) + '\n')
    short_sample.close()


if __name__ == '__main__':
    content = open("short_sample").read()
    PAT = r'(河南)\w+'
    searched = re.sub(PAT, r'\n##\g<1>##:\n \g<0>', content)
    print(searched)
    with open('result.md','w')as f:
        f.write(searched)
        # print()
