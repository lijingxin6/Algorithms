# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 10:28 AM 4/30/20

Question: 1006_4

Given an absolute path for a file (Unix-style), simplify it.
For example,
path = "/home/" => "/home"
path = "/a/./b/../../c/" => "/c"

 .  means current directory
 .. means last directory

"""

def simplifyPath(path):
    lst = []
    splits = path.split("/")

    for s in splits:
        if s == "":
            continue
        if s == ".":
            continue
        if s == "..":
            if len(lst) != 0:
                lst.pop()
        else:
            lst.append(s)
    result = []
    if len(lst) == 0:
        return "/"
    result = ["/" + i for i in lst]  # 得到类似  /a   /b   /c
    return ''.join(result)           #  /a/b/c


path = "/home/"  # split =>  ['', 'home', '']
print(simplifyPath(path))
path = "/a/./b/../../c/d/../e/f/g/../"
print(simplifyPath(path))