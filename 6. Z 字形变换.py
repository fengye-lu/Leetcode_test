# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 16:58
# @Author  : Jackey-lu
# @File    : 6. Z 字形变换.py

'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        a = [[] for i in range(numRows)]
        l = 0
        cow_index = 0
        row_index = 0
        # row = numRows - 2
        row = 3
        b = ''
        for i in s :
            if numRows == 2:
                if l % 2 == 0:
                    a[0].append(i)
                    l += 1
                    continue
                else:
                    a[1].append(i)
                    l += 1
                    continue
            if cow_index % 2 != 0:
                a[row].append(i)
                row -= 1
            elif cow_index % 2 == 0:
                a[row_index].append(i)
                row_index += 1
            if row_index > numRows-1 or row <= 0:
                cow_index += 1
                row_index = 0
                row = numRows - 2
        for i in range(numRows):
            for j in a[i]:
                b += j
        return b
'''


'''

'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)

obj = Solution()
print(obj.convert("ABCDEF",2))