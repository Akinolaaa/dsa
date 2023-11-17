## 309- https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = {}  # (i, buying): bestPrice

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                p = dfs(i + 1, not buying) - prices[i]
                cool = dfs(i + 1, buying)
                dp[(i, buying)] = max(p, cool)
            else:
                p = dfs(i + 2, not buying) + prices[i]
                cool = dfs(i + 1, buying)
                dp[(i, buying)] = max(p, cool)
            return dp[(i, buying)]

        return dfs(0, True)


prices = [1, 2, 3, 0, 2]
print(Solution().maxProfit(prices))
