# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 10:00 AM 4/10/20

"""
from random import random
import random
def shuffle_system(cards):
    random.shuffle(cards)

def shuffle_1st(cards):
    for k in range(len(cards)):
        i = random.randint(0, len(cards) - 1)
        j = random.randint(0, len(cards) - 1)
        cards[i], cards[j] = cards[j], cards[i]



## DO More Exercise！！
def shuffle_correct(cards):
    for i in range(len(cards)):
        #randomi = i + random.randint(0, len(cards) - i - 1)
        randomi = random.randint(i, len(cards)-1)
        cards[i], cards[randomi] = cards[randomi], cards[i]

A = [i for i in range(0,10)]
print(A)
shuffle_correct(A)
print(A)