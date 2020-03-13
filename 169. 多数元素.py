# -*- coding: utf-8 -*-
# @Time    : 2020/3/13 16:30
# @Author  : Jackey-lu
# @File    : 169. 多数元素.py

'''
class Solution:
    def majorityElement(self, nums) -> int:
        a = []
        for i in nums:
            if i in a:continue
            if nums.count(i) > len(nums) // 2:
                return i
            else:
                a.append(i)
'''


'''
class Solution:
    def majorityElement(self, nums) -> int:
        nums.sort()
        return nums[len(nums)//2]
'''


import collections
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

