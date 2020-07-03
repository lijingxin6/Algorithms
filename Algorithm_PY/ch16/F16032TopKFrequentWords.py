# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 9:08 AM 5/12/20

Question: 

"""

import collections
import heapq
import functools


@functools.total_ordering
class Element:
    def __init__(self, count, word):
        self.count = count
        self.word = word

    def __lt__(self, other):
        if self.count == other.count:
            print(self.word > other.word)
            return self.word > other.word  # 注意频率相同要按字典序排序，而我最终是从后往前塞元素的，所以要改成 >
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word


def topKFrequent(words, k):
    counts = collections.Counter(words)

    freqs = []
    heapq.heapify(freqs)
    for word, count in counts.items():
        heapq.heappush(freqs, (Element(count, word), word))
        if len(freqs) > k:
            heapq.heappop(freqs)

    res = []
    for _ in range(k):
        res.append(heapq.heappop(freqs)[1])
    return res[::-1]

# i 和 love 都是 3次,词频相同,  i在前面 所以 打印的时候i也在前
words = ["i", "love","love", "you", "i", "love", "coding","like","i","like", "sports"]
k = 2
topKFrequent(words, k)