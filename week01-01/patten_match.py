"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/3/26 17:27
# @Author:YiShouquan
# @File:patten_match.py
# @Update:
"""
# pattern match
# 解析一个json
def parse_json(parsed_json):
    """
    possible input:{
    'Age':19,
    'user_id':'uuid12312314',
    'goods-info':{
        'price':100,
        'createtime':2022
        }
    }
    possible input:{
    "name":Tome,
    USER_ID:uuid15231365,
    "action-info":{
        "last-login":Match-22
        }
    }

    """
    # """
    # if isinstance(parsed_json,dict):
    #  if "name" in parsed_json:
    #      if "action-info" in parsed_json:
    #          pass
    #      elif "goods-info" in parsed_json:
    #          pass
    #      else:
    #          pass
    #  elif "Age" in parsed_json:
    #      if ...
    # """

    match parsed_json:
        case {'name': str(name), 'user-id': str(user_id), "goods-info": {"price": float(p), "createtime": str(time_)}}:
            print(f"{name}with id {user_id} bought {p} goods")
        case {'Age': str(age), 'user-id': str(user_id), "action-info": {"last-login": str(p)}}:
            print(f"{user_id}with age {age} last-login is {p}")
        case _:
            raise TypeError('invalid json format')






# func_define = """def some_test():return 10"""
# exec(func_define)
# # evel("some_test()")


# class Point:
#     x: int = 1
#     y: int = 2
# def location(point):
#     match point:
#         case Point(x=0, y=0):
#             print("坐标原点")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point(x=x, y=y):
#             print(f"X={x}, Y={y}")
#         case Point():
#             print("这个点不在轴上")
#         case _:
#             raise ValueError("未法的坐标数据")
# if __name__ == '__main__':
#     point = Point()
#     print(location(point))