# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 9:46 PM 5/27/20

Question: 

"""

# O(m*n)
# O(m) space
def uniquePathsWithObstacles(obstacleGrid):
    M, N = len(obstacleGrid), len(obstacleGrid[0])
    dp = [1] + [0] * (N-1)
    for i in range(M):
        for j in range(N):
            if obstacleGrid[i][j] == 1: # 有障碍物 就赋值成 0
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j-1]
    return dp[N-1]

grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
uniquePathsWithObstacles(grid)