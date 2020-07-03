# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 3:10 PM 4/30/20

Question: 

"""
# 错误写法  while应该对应一个else, 如果少写else, break的时候,就只会break while 而不会跳出去,程序会执行没写else的那句 造成bug
def asteroidCollision_wrong(asteriod):
    ans = []
    for new in asteriod:
        while ans and new < 0 < ans[-1]:
            if ans[-1] < -new:
                ans.pop()
            elif ans[-1] == -new:
                ans.pop()
            else:
                break
        #else:
        ans.append(new)
    return ans

# 正确写法
def asteroidCollision(asteroids):
    stack = []
    for new in asteroids:
        while stack and new < 0 < stack[-1]:
            if stack[-1] < -new:
                stack.pop()
            elif stack[-1] == -new:
                stack.pop()
            else:
                break
        else: # stack为空 或者 同号
            stack.append(new)
    return stack
asteroids = [-2, -1, 1, 2]
print(asteroidCollision(asteroids))

asteroids = [5, 10, -5]
print(asteroidCollision(asteroids))

asteroids = [3, 2, -5, 1, 6, -3, -7]
print(asteroidCollision(asteroids))