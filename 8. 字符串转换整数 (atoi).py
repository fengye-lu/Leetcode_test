# -*- coding: utf-8 -*-
# @Time    : 2020/4/8 19:08
# @Author  : Jackey-lu
# @File    : 8. 字符串转换整数 (atoi).py


import re
'''
import re
class Solution:
    def myAtoi(self, str: str) -> int:
        val = 0
        if not str : return 0 
        for index,i in enumerate(str):
            if i == 0:
                continue
            elif i.isdigit():
                break
            elif i == ' ' :
                if val == 1:
                    return 0
                continue
            elif i == '+' or i == '-':
                if val == 1:
                    return 0
                val = 1
                continue
            else:
                return 0
        try:
            b = re.search(r'(\+|\-|'')\d+',str).group()
            a =int(b)
        except Exception as e:
            return 0     
        high = (2**31) - 1
        low = -2**31
        if a < low:
            return low
        elif a > high:
            return high
        return a
'''

# return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)
