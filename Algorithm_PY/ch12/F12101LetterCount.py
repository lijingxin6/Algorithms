# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 10:48 PM 5/2/20

Question: 

"""

def letterCount(s):
    freq = {}
    for piece in s:
        # only consider alphabetic characters within this piece
        word = ''.join(c for c in piece if c.isalpha())
        if word:
            freq[word] = 1 + freq.get(word, 0) #default 0

    max_word = ''
    max_count = 0
    for (w,c) in freq.items():    # (key, value) tuples represent (word, count)
        if c > max_count:
            max_word = w
            max_count = c
    print('The most frequent word is', max_word)
    print('Its number of occurrences is', max_count)

s = "Hello World"
letterCount(s)