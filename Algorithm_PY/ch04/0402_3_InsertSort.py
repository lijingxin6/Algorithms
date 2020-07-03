# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:23 PM 4/12/20

"""

def insert_sort(items):
    for sort_idx in range(1, len(items)): # 手里有张底牌， 摸第一张牌 到最后一张牌
        unsort_idx = sort_idx
        while(unsort_idx > 0 and items[unsort_idx - 1] > items[unsort_idx]):
            items[unsort_idx-1], items[unsort_idx] = items[unsort_idx], items[unsort_idx-1]
            unsort_idx = unsort_idx - 1

    return len((items))




def insert_sort2(items):
    for i in range(1, len(items)): # 手里有张底牌， 摸第一张牌 到最后一张牌
        for j in range(i, 0, -1):
            if (items[j - 1] > items[j]):
                items[j-1], items[j] = items[j], items[j-1]

    return len((items))

l = [1, 3, 95, 7, 9, 2, 4, 6, 8, 99]
insert_sort2(l)
print(l)