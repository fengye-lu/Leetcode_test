# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 19:31
# @Author  : Jackey-lu
# @File    : 1103. 分糖果 II.py

class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        rel = [0 for t in range(num_people)]
        amount = 0
        while candies:  # 当糖果的数量不为空时，一轮一轮的接着发
            for i in range(num_people):
                candies_num = i + amount +1  # 初始化每轮发糖果时，第一个小朋友应该发的数量
                if candies > candies_num:
                    rel[i] += candies_num
                    candies -= candies_num
                else:
                    rel[i] += candies
                    candies = 0
                    break  # 如果糖果的数量少于小朋友应该得到的糖果的数量应该立即退出

            amount += num_people  # 每轮小朋友发的糖果数量应该比上一轮多num_people
        return rel

obj = Solution()
print(obj.distributeCandies(10,3))