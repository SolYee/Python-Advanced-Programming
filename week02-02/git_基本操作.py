"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2022/4/11 14:30
# @Author:YiShouquan
# @File:git_基本操作.py
# @Update:
"""
"""版管理一般有两种：SVN GIT
GIT好处：
    去中心化管理
"""
"""
git init   #已经新建的git环境/仓库  初始化
git status #返回现在所处的状态
vim ~/.gitconfig   #进入gitconfig文件编辑内容
[user]
# Please adapt and uncomment the following lines:
        name = Szeto
        email = 15989434843@163.com
[alias]
        co = commit
        st = status
[core]
        autocrlf = input
[http]
        proxy = socks5://127.0.0.1:4781

git add #新加入某文件
git commit -m '+++' #提交并说明提交内容
git log #查看提交日志信息
git checkout    #切换版本
git checkout -b  #新开一个分支
git marge   #合并
"""


""" 
#git远程连接github   gitlab
git remote add origin
git pull origin master  #拉去最新的代码
     #上传代码
git clone   #复制并拉取所有源代码
"""



# __match_args__ =('name','age','city')
# @dataclasses