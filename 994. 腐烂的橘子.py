# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 20:22
# @Author  : Jackey-lu
# @File    : 994. 腐烂的橘子.py

class Solution:
    def orangesRotting(self, grid) -> int:
        time = 0
        bad = {(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 2}
        good = {(i,j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == 1}
        while good:
            if not bad : return -1
            bad = {(i+n,j+m) for i,j in bad for n,m in {(1,0),(0,1),(-1,0),(0,-1)} if (i+n,j+m) in good}
            good -= bad
            time += 1
        return time

obj = Solution()
print(obj.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
