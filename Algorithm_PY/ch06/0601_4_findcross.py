# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 5:00 PM 4/16/20

"""
# set()
def intersection(nums1: list, nums2: list) -> list:
    nums1 = set(nums1)
    nums2 = set(nums2)
    return nums1 & nums2
# 暴力
def findcross1(m: list, n: list) -> list:
    c = set()
    for i in range(len(m)):
        for j in range(len(n)):
            if m[i] == n[j]:
                c.add(n[j])
    return c

# 双指针
def intersection2(nums1: list, nums2: list) -> list:
    nums1.sort()
    nums2.sort()
    i, j, res = 0, 0, []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            if nums1[i] not in res:
                res.append(nums1[i])
            i += 1
            j += 1
    return res

# 输出可以有重复的情况
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j, res = 0, 0, []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                res.append(nums2[j])
                i += 1
                j += 1
        return res

# [未完成] 二分法
def findcross2(m: list, n: list) -> list:
    n.sort()
    left, right = 0, len(n) - 1
    for num in m:
        while(left <= right):
            mid = left + (right-left) // 2
            if n[mid] == num:
                return mid
            elif n[mid] > num:
                right = mid
            else:
                left = mid
        return -1












m = [1, 2, 3, 4]
n = [1, 6, 5, 3]
print(findcross2(m,n))
