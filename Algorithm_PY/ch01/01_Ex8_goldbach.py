# -*- coding:utf-8 -*-
"""
author: lijingxin

Created on 12:50 PM 4/10/20

"""

def goldbach(n):
    is_prime = [True] * (n + 1)
    i = 2
    while(i * i <= n):
        if(is_prime[i]):
            j = i
            while(j * i <= n):
                is_prime[j * i] = False
                j += 1
        i += 1
    counts = 0
    for i in range(2, n+1):
        if(is_prime[i]):
            counts += 1

    primes = [None] * counts
    idx = 0
    for i in range(2, n+1):
        if (is_prime[i]):
            primes[idx] = i
            idx += 1

    left = 0
    right = counts - 1
    while(left < right):
        if(n == primes[left] + primes[right]):
            print(n, "=", primes[left], "+", primes[right])
            left += 1
            right -= 1
        elif(n > primes[left] + primes[right]):
            left += 1
        else:
            right -= 1

goldbach(100)