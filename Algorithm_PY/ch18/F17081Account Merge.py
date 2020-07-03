# -*- coding:utf-8 -*-
"""
@author: lijingxin
@contact: lijingxin666@gmail.com
@site: https://github.com/lijingxin666
@time: Created on 9:23 PM 5/21/20

Question: 

"""
from collections import defaultdict


def accountsMerge(accounts):
    visited_accounts = [False] * len(accounts)
    emails_accounts_map = defaultdict(list)
    res = []
    # Build up the graph.
    for i, account in enumerate(accounts):
        for j in range(1, len(account)):  # email starts from 2nd
            email = account[j]
            emails_accounts_map[email].append(i)  # key:email    value: account

    print(emails_accounts_map)

    # DFS code for traversing accounts.
    def dfs(i, emails):
        if visited_accounts[i]:
            return
        visited_accounts[i] = True
        for j in range(1, len(accounts[i])):
            email = accounts[i][j]
            emails.add(email)
            for neighbor in emails_accounts_map[email]:
                dfs(neighbor, emails)

    # Perform DFS for accounts and add to results.
    for i, account in enumerate(accounts):
        if visited_accounts[i]:
            continue
        name, emails = account[0], set()
        dfs(i, emails)
        res.append([name] + sorted(emails))
    return res

accounts = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary@mail.com"]
]

accountsMerge(accounts)