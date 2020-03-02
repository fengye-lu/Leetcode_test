# -*- coding: utf-8 -*-
# @Time    : 2020/2/27 20:27
# @Author  : Jackey-lu
# @File    : 最长回文子串.py


# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         length = len(s)
#         result = str()
#         for i in range(length):
#             sum1 = str()
#             sum2 = str()
#             for str1 in s[i:]:
#                 # if len(s[i:]) > 1:
#                 sum1 = sum1 + str1
#                 sum2 = str1 + sum2
#                 # if sum1 == sum2 and result == '':
#                 #     result = sum1
#                 if sum1 == sum2 and len(sum1)>len(result):
#                     result = sum1
#                 else:
#                     continue
#                 # else:
#                 #     return s
#         return result




# 动态规划法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size < 2:
            return s
        dp = [[False for _ in range(size)] for _ in range(size)]
        max_len = 1
        start = 0
        for i in range(size):
            dp[i][i] = True
        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start + max_len]

obj = Solution()
print(obj.longestPalindrome('babad'))