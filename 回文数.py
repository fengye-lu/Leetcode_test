# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 20:13
# @Author  : Jackey-lu
# @File    : 回文数.py


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        pan_val = x
        com_num = 0
        rel = 0
        while x != 0:
            rel = int(x % 10)
            com_num = 10 * com_num + rel
            x = int(x / 10)
        if com_num == pan_val:
            return True
        else:
            return False



# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         str1 = str(x)
#         com = ''
#         for i in str1:
#             com = i + com
#         if com == str1:
#             return True
#         else:
#             return False
obj = Solution()
print(obj.isPalindrome(12321))