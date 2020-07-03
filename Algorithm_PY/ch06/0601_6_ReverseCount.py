# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 3:06 PM 4/17/20

"""
def reversePairs(nums: list) -> int:
    cnt = 0
    def merge(nums, start, mid, end, temp):
        nonlocal cnt
        i, j = start, mid + 1    # j 从 mid+1开始
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                cnt += mid - i + 1     ###     mid - i + 1
                j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1                  # 不要忘记i++
        while j <= end:
            temp.append(nums[j])
            j += 1                  # 不要忘记 j++
        for i in range(len(temp)):
            nums[start + i] = temp[i]
        temp.clear()

    def mergeSort(nums, start, end, temp):
        if start >= end: return
        mid = (start + end) // 2    ### mid
        mergeSort(nums, start, mid, temp)
        mergeSort(nums, mid+1, end, temp)
        merge(nums, start, mid, end, temp)

    mergeSort(nums, 0, len(nums)-1, [])
    return cnt

l = [7,5,6,4]
print(reversePairs(l))