# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 19:55
# @Author  : Jackey-lu
# @File    : 面试题57 - II. 和为s的连续正数序列.py


# class Solution:
#     def findContinuousSequence(self, target: int):
#         mid = []
#         rel = []
#         for i in range(1,target//2+1):
#             val = i
#             mid = [i]
#             for j in range(1+i,target//2+2):
#                 mid.append(j)
#                 if  j + val == target:
#                     rel.append(mid)
#                     break
#                 else:
#                     val +=  j
#         return rel


# class Solution:
#     def findContinuousSequence(self, target: int):
#         a = [i for i in range(1,target+1)]
#         rel = []
#         left = 0
#         right = 1
#         while left <= target // 2:
#             if sum(a[left:right+1]) > target:
#                 left += 1
#             elif sum(a[left:right+1]) < target:
#                 right += 1
#             else:
#                 rel.append(a[left:right+1])
#                 left += 1
#         return rel



class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i = 1 # 滑动窗口的左边界
        j = 1 # 滑动窗口的右边界
        sum = 0 # 滑动窗口中数字的和
        res = []

        while i <= target // 2:
            if sum < target:
                # 右边界向右移动
                sum += j
                j += 1
            elif sum > target:
                # 左边界向右移动
                sum -= i
                i += 1
            else:
                # 记录结果
                arr = list(range(i, j))
                res.append(arr)
                # 左边界向右移动
                sum -= i
                i += 1

        return res


obj = Solution()
print(obj.findContinuousSequence(15))
