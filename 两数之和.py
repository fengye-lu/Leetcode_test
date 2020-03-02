# -*- coding: utf-8 -*-
# @Time    : 2020/2/25 19:36
# @Author  : Jackey-lu
# @File    : 两数之和.py

class Solution:
    def twoSum(self, nums, target):
        for index1,first in enumerate(nums):
            for index2,second in enumerate(nums[index1+1:]):
                if first + second == target:
                    index2 = index1+index2+1
                    break
            if first + second == target:
                break
        return [index1, index2]


# class Solution:
#     def twoSum(self,nums, target):
#         hashmap={}
#         for ind,num in enumerate(nums):
#             hashmap[num] = ind
#         for i,num in enumerate(nums):
#             j = hashmap.get(target - num)
#             if j is not None and i!=j:
#                 return [i,j]
obj = Solution()
print(obj.twoSum([2,11,2,3,2,3],5))
