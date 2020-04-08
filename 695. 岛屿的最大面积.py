# -*- coding: utf-8 -*-
# @Time    : 2020/3/15 19:24
# @Author  : Jackey-lu
# @File    : 695. 岛屿的最大面积.py

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        ans = 0
        len_h = len(grid)
        len_l = len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i > len_h - 1 or j > len_l - 1: return 0
            if grid[i][j] == 0 : return 0
            grid[i][j] = 0
            left = dfs(i, j-1)
            right = dfs(i, j+1)
            top = dfs(i+1, j)
            bottom = dfs(i-1, j)
            return sum([left, right, top, bottom]) + 1
        for i in range(len_h):
            for j in range(len_l):
                ans = max(ans, dfs(i, j))
        return ans

obj = Solution()
print(obj.maxAreaOfIsland([[1, 1, 0, 0, 0],
                           [1, 1, 0, 0, 0],
                           [0, 0, 0, 1, 1],
                           [0, 0, 0, 1, 1]]))