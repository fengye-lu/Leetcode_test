# -*- coding: utf-8 -*-
# @Time    : 2020/3/11 19:13
# @Author  : Jackey-lu
# @File    : 1013. 将数组分成和相等的三个部分.py

'''
给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2]
+ ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

'''

class Solution:
    def canThreePartsEqualSum(self, A) -> bool:
        i  = 0
        sum_ = sum(A)
        if sum_ % 3 != 0:return False
        while i < len(A)-2:
            if sum(A[0:i+1]) != sum_ / 3:
                i += 1
                continue
            j = i + 2
            while j < len(A):
                if sum(A[i+1:j]) != sum_/3:
                    j += 1
                    continue
                # if sum(A[j:]) != sum_/3:
                #     j += 1
                #     continue
                return True
            i += 1
        return False

object = Solution()
print(object.canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]))