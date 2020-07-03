# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 10:28 AM 4/13/20
 1. 找到最大值 最小值
 2.确定范围  max - min + 1
 3. 计数  counts[items[i] - min] += 1
 4. 打印出结果： i 个 相同的 一起打印

"""

def count_sort(items):
    mmax, mmin = items[0], items[0]
    for i in range(1, len(items)): # 不从 0 开始， 从 1 开始 因为0已经设置了
        if(items[i] > mmax): mmax = items[i]
        elif( items[i] < mmin): mmin = items[i]

    nums = mmax - mmin + 1

    counts = [0] * nums
    for i in range(len(items)):
        counts[items[i] - mmin] += 1

    # ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  下面有点慢  可以提升
    pos = 0
    for i in range(nums):            # i 遍历所有的数
        for j in range(counts[i]):   ## counts[i] 表示 j个相同的数， 某个数的个数
            items[pos] = i + mmin
            pos += 1                  ## pos 要保留itmes所有信息， 所以 pos = 0 到 pos += 1
    print(items)
    # ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

items = [4, 1, 2, 3, 4, 5, 3, 4, 2, 4, 5]
items2 = [94, 99, 91, 93, 96, 99, 90, 98, 99, 99]
print(count_sort(items))
