# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 19:43
# @Author  : Jackey-lu
# @File    : 322. 零钱兑换.py

'''
class Solution:
    def coinChange(self,coins, amount: int):
        # 备忘录
        memo = dict()

        def dp(n):
            # 查备忘录，避免重复计算
            if n in memo: return memo[n]

            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')
            for coin in coins:
                subproblem = dp(n - coin)
                if subproblem == -1: continue
                res = min(res, 1 + subproblem)

            # 记入备忘录
            memo[n] = res if res != float('INF') else -1
            return memo[n]

        return dp(amount)
'''





class Solution:
    def coinChange(self, coins, amount: int) -> int:
        cnt_list = [float("inf")] * (amount + 1)
        cnt_list[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                cnt_list[i] = min(cnt_list[i], cnt_list[i - coin] + 1)

        if cnt_list[-1] == float("inf"):
            return -1
        else:
            return cnt_list[-1]

obj = Solution()
print(obj.coinChange([1, 2, 5], 11))