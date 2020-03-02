# -*- coding: utf-8 -*-
# @Time    : 2020/2/26 15:43
# @Author  : Jackey-lu
# @File    : 无重复字符的字符串长度.py

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         count = []
#         lenth = len(s)
#         if s != '':
#             for i, str in enumerate(s):
#                 out = []
#                 sum = 1
#                 out.insert(0, str)
#                 if len(s) > 1:
#                     if i+1 == lenth:
#                         sum = 1
#                     else:
#                         for j, str1 in enumerate(s[i + 1:]):
#                             if str1 not in out:
#                                 out.insert(j + 1, str1)
#                                 sum += 1
#                                 continue
#                             else:
#                                 out = []
#                                 break
#                 else:
#                     sum = 1
#                 count.insert(i,sum)
#             return max(count)
#         else:
#             return 0
#


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:max_len = cur_len
            lookup.add(s[i])
        return max_len
obj = Solution()
print(obj.lengthOfLongestSubstring("abcabcab"))