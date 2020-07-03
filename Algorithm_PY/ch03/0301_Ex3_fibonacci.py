# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:23 PM 4/11/20

 1 1 2 3 5 8  13 21...

 f(n) = f(n-1) + f(n-2)

"""

def fibonacci1(n):
    assert (n>=0)
    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return  a

## This is Understandable.##
def fibonacci2(n):
    assert (n>=0)
    if(n <= 2):
        return 1
    return fibonacci2(n-1) + fibonacci2(n-2)

def fibonacci3(n):
    assert (n>=0)
    if(n <= 1):
        return (n, 0)
    (a,b) = fibonacci3(n-1)
    return (a+b, a)

print(fibonacci2(10))

def fibonaccis(n):
    assert (n>=0)
    result = [0, 1]
    for i in range(2, n+1):
        result.append(result[-2] + result[-1])
    return result
