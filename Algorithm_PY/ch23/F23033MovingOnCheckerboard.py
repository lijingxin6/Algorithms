# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 10:06 AM 5/28/20

Question: 

"""

# space O(m*n) -> O(m)
def movingBoard2(board):
    result = board[0] # 只用到左上,正上,右上  只需要用一排
    m = len(board)
    n = len(board[0])
    for i in range(1, m):
        for j in range (0, n):
            result[j] = max(0 if j == 0 else result[j-1], \
                            result[j], \
                            0 if j == n-1 else result[j+1] ) \
                        + board[i][j]
    return max(result)
board = [
    [-2,-1,0,-3,1],
    [1,3,5,4,2],
    [3,5,2,0,4],
    [2,3,1,4,2]
]
movingBoard2(board)