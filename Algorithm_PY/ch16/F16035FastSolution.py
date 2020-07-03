# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 5:57 PM 5/12/20

Question: 

"""
import  heapq
# O(kLogk)
def kSmallestPairs(nums1, nums2, k):
    queue = []
    def push(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
    push(0, 0)
    pairs = []
    while queue and len(pairs) < k:
        _, i, j = heapq.heappop(queue)
        pairs.append([nums1[i], nums2[j]]) # 先把第一个从queue pop出来 再添加进pairs去
        push(i, j + 1)
        if j == 0:
            push(i + 1, 0)
    return pairs

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 20
kSmallestPairs(nums1, nums2, k)