# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 3:13 PM 4/12/20

#  h -> he -> hel -> hell -> hello
#                         -> hellO
#  h -> hE -> hEl -> hEll -> hEllo
#                         -> hEllO

"""
results = set()
keys = set()

def permLetter(word, rule):
    rule = rule.lower()
    for c in rule:
        keys.add(c)
    permHelper(word, rule, 0, "")

def permHelper(word, rule, index, prefix):
    length = len(word)

    for i in range(index, length): # i 有 length个数， 但是i的最大值是 length-1
        c = word[i]
        if(c in keys):             # 单词中的第i个 是否是 rule里的
            permHelper(word, rule, i+1, prefix+c)
            c = c.upper()
            permHelper(word, rule, i+1, prefix+c)
        else:
            prefix += c
    if(len(prefix) == len(word)):
        results.add(prefix)

word = "hello"
rule = "eo"
permLetter(word, rule)
print(results)