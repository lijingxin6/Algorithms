# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:39 PM 4/11/20

*********************************
1

1 2 1

1 2 1 3 1 2 1

1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
*********************************


"""

def ruler_bad(n):
    assert (n>=0)
    if(n == 1):
        return "1"
    return ruler_bad(n-1) + " " + str(n) + " " + ruler_bad(n-1)

def ruler(n):
    assert (n>=0)
    if(n == 1):
        return "1"
    t = ruler(n-1)
    return t + " " + str(n) + " " + t

def ruler2(n):
    result = ""
    for i in range(1, n+1):
        result = result + str(i) + " " + result
    return result

print(ruler_bad(3))

def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(center_length):
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)        #### draw_line
        draw_interval(center_length - 1)

def draw_ruler(num_inchs, major_length):
    draw_line(major_length, '0')
    for j in range(1, 1+ num_inchs):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))