# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 19:31
# @Author  : Jackey-lu
# @File    : 1103. 分糖果 II.py

class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        rel = [0 for t in range(num_people)]
        amount = 0
        while candies:
            for i in range(num_people):
                candies_num = i + amount +1
                if candies > candies_num:
                    rel[i] += candies_num
                    candies -= candies_num
                else:
                    rel[i] += candies
                    candies = 0
                    break

            amount += num_people
        return rel

obj = Solution()
print(obj.distributeCandies(10,3))