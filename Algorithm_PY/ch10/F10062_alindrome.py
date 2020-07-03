# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 9:40 AM 4/30/20

    1006_1

"""
from F10061reverseString import reverse

def isPalindrome(s):
    r = reverse(s)
    return r ==s


s = "hello world"
print(isPalindrome(s))

s = "madamimadam"
print(isPalindrome(s))