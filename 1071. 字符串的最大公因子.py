# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 17:01
# @Author  : Jackey-lu
# @File    : 1071. 字符串的最大公因子.py
'''
import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        candidate_len = math.gcd(len(str1), len(str2))
        candidate = str1[: candidate_len]
        if candidate * (len(str1) // candidate_len) == str1 and candidate * (len(str2) // candidate_len) == str2:
            return candidate
        return ''
'''



class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        rel = ''
        for i in range(1,min(len1,len2)+1):
            if len1 % i == 0 and len2 % i== 0:
                if (len1 // i)*str1[0:i] == str1:
                    if (len2 // i)*str1[0:i] == str2:
                        rel = str1[0:i]
        return rel

