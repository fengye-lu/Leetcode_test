# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 18:44
# @Author  : Jackey-lu
# @File    : 300. 最长上升子序列.py


class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0
        dp = []
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


obj = Solution()
print(obj.lengthOfLIS([10,9,2,5,3,7,101,18]))