#!/usr/bin/env python
# coding: utf-8

# In[9]:


"""
4 kyu: Strip Comments
http://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
"""

def solution(s,m):
    s = s.split('\n')
    for i in range(len(s)):
        for marker in m:
            x = s[i].find(marker)
            if x != -1:
                s[i] = s[i][:x]
        s[i] = s[i].rstrip(' ')
    return '\n'.join(s)

