# -*- coding: utf-8 -*-
# @Time    : 2020/3/9 16:30
# @Author  : Jackey-lu
# @File    : 121. 买卖股票的最佳时机.py


class Solution:
    def maxProfit(self, prices) -> int:
        if not prices: return 0
        low_pr = prices[0]
        profit = 0
        for i in prices:
            # if i <= low_pr:
            #     low_pr = i
            low_pr = min(low_pr,i)
            # elif i > low_pr and i - low_pr > profit:
            #     profit = i - low_pr
            profit = max(profit,i - low_pr)
        return profit
