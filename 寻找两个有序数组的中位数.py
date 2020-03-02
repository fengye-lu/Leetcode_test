# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 19:29
# @Author  : Jackey-lu
# @File    : 寻找两个有序数组的中位数.py

# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) -> float:
#         nums3 = nums2.copy()
#         for index1,str1 in enumerate(nums1):
#             for index2,str2 in enumerate(nums2):
#                 if index2+1 < len(nums2):
#                     if str1 >= str2 and str1 < nums2[index2+1]:
#                         nums3.insert(index1+index2+1,str1)
#                         break
#                     elif str1 < str2:
#                         nums3.insert(index1+index2,str1)
#                         break
#                 elif str1 > str2:
#                     nums3.append(str1)
#                     break
#                 else:
#                     nums3.insert(index1 + index2, str1)
#                     break
#         length = len(nums3)
#
#         if length > 1:
#             if length % 2 == 0:
#                 mid = int(length/2) - 1
#                 mid_val = float((nums3[mid]+nums3[mid+1]))/2
#             else:
#                 mid = int(length/2)
#                 mid_val = float(nums3[mid])
#         elif nums1:
#             length = len(nums1)
#             if length % 2 == 0:
#                 mid = int(length/2) - 1
#                 mid_val = float((nums1[mid]+nums1[mid+1]))/2
#             else:
#                 mid = int(length/2)
#                 mid_val = float(nums1[mid])
#             return mid_val
#         else:
#             length = len(nums2)
#             if length % 2 == 0:
#                 mid = int(length/2) - 1
#                 mid_val = float((nums2[mid]+nums2[mid+1]))/2
#             else:
#                 mid = int(length/2)
#                 mid_val = float(nums2[mid])
#             return mid_val
#
#
#         return mid_val
#
#
#
# obj = Solution()
# print(obj.findMedianSortedArrays([3,4],[]))




class Solution:
    def comput_mid(self,arg):
        length = len(arg)
        if length % 2 == 0:
            mid = int(length / 2) - 1
            mid_val = float((arg[mid] + arg[mid + 1])) / 2
        else:
            mid = int(length / 2)
            mid_val = float(arg[mid])
        return mid_val

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums3 = nums2.copy()
        for index1,str1 in enumerate(nums1):
            for index2,str2 in enumerate(nums2):
                if index2+1 < len(nums2):
                    if str1 >= str2 and str1 < nums2[index2+1]:
                        nums3.insert(index1+index2+1,str1)
                        break
                    elif str1 < str2:
                        nums3.insert(index1+index2,str1)
                        break
                elif str1 > str2:
                    nums3.append(str1)
                    break
                else:
                    nums3.insert(index1 + index2, str1)
                    break
        length = len(nums3)

        if length > 1:
            rel = self.comput_mid(nums3)
            return rel

        elif nums1:
            rel = self.comput_mid(nums1)
            return rel
        else:
            rel = self.comput_mid(nums2)
            return rel


obj = Solution()
print(obj.findMedianSortedArrays([],[3,4]))
