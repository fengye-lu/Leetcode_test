# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 19:10
# @Author  : Jackey-lu
# @File    : 整数反转.py

'''
class Solution:
    def reverse(self, x: int) -> int:
        num = str(x)
        if num[0] == '-':
            j = -1
        else:
            j = 1
        num1 = str(abs(x))
        rel = ''
        for val1 in num1:
            rel = val1 + rel
        fin_rel = int(rel)*j
        if fin_rel < (-2**31) or fin_rel > (2**31)-1:
            return 0
        return fin_rel

obj = Solution()
print(obj.reverse(-1563847412))
'''



class Solution:
    def reverse(self, x: int) -> int:
        val = 0
        j = 1 if x < 0 else  -1
        x = abs(x)
        while x != 0 :
            right = x % 10
            x = int(x / 10)
            val = val*10 + right
        val = j * val
        if val < (-2**31) or val > (2**31)-1:
            return 0
        return val



obj = Solution()
print(obj.reverse(-123))



