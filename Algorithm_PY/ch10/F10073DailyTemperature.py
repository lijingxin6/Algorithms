# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 6:13 PM 4/30/20

Question: 

"""

def dailyTemperatures(temperatures):
    if not temperatures: return []
    result, stack = [0] * len(temperatures), []
    stack.append( (temperatures[0] , 0) ) # 后面的数字 是 当前temperature对应的index
    for i in range(1, len(temperatures)):
        while stack:
            prev = stack[-1]
            if prev[0] < temperatures[i]:
                result[prev[1]] = i - prev[1]
                stack.pop()
            else:
                break # 只是跳出while循环
        stack.append((temperatures[i], i))
    return result

def dailyTemperatures2(temperatures):
    if not temperatures: return  None
    result, stack = [0] * len(temperatures), []
    stack.append(0)
    for i in range(1, len(temperatures)):
        while stack:
            prev = stack[-1]
            if temperatures[prev] < temperatures[i]:
                result[prev] = i - prev
                stack.pop() # 找到第一个比它大的数值后 立即pop
            else:
                break
        stack.append(i) # 不管stack是空还是非空 都要把 i 的值push进去
    return  result








t = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(t))