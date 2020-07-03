# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 8:44 PM 4/12/20

======> Find the smallest num and put it in the first place #####

"""
def selection_sort(items):
    for i in range(len(items)):
        pos_min = i
        for j in range(i+1, len(items)):
            if items[j] < items[pos_min]:
                pos_min = j    # find the smallest num's index
        items[i], items[pos_min] = items[pos_min], items[i]   # change with the i th num
    return len(items)

l = [1, 3, 5, 7, 9, 2, 4, 6, 8, 99]
selection_sort(l)
print(l)