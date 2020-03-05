# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 19:11
# @Author  : Jackey-lu
# @File    : 面试题 10.01. 合并排序的数组.py

# class Solution:
#     def merge(self, A, m: int, B, n: int) -> None:
#         """
#         Do not return anything, modify A in-place instead.
#         """
#         for i in B:
#             for index,j in enumerate(A):
#                 if index+1 > m:
#                     A.insert(index,i)
#                     m += 1
#                     del A[len(A)-1]
#                     break
#                 if i >= j and i <= A[index+1]:
#                     A.insert(index+1,i)
#                     m += 1
#                     del A[len(A) - 1]
#                     break
#                 elif i < j:
#                     A.insert(index,i)
#                     m += 1
#                     del A[len(A) - 1]
#                     break
#         return A


# code:'utf-8'

'''
class Solution:
    def merge(self, A, m: int, B, n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        node = m+n-1
        if m != 0:
            for i in range(n):
                for t in range(m):
                    if B[n-1-i] > A[m-t-1]:
                        A[node-i] = B[n-1-i]
                        break
                    elif B[n - 1 - i] == A[m - t - 1]:
                        A[node - i-1] = B[n - 1 - i]
                        break
                    else:
                        A[node-i] = A[m-t-1]
        else:
            A = B
        return A
'''

'''
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        idx1 = m - 1
        idx2 = n - 1
        cur = m + n - 1 # 添加 cur 指针追踪位置
        while idx1 > -1 and idx2 > -1:
            # print(A)
            if A[idx1] < B[idx2]:
                A[cur] = B[idx2]
                cur -= 1
                idx2 -= 1
            else:
                A[cur] = A[idx1]
                cur -= 1
                idx1 -= 1
        if idx2 != -1: A[:idx2 + 1] = B[:idx2 + 1] # 比较完B还有剩下的，全填到A前面即可
        return A
'''

obj = Solution()

print(obj.merge([0], 0, [1], 1))
