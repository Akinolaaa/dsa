# 518- https://leetcode.com/problems/coin-change-ii/
class Solution:
        # same as below
    def change(self, amount: int, coins: list[int]) -> int:
        dp = {}  # (i, total): int
        def dfs(i, total):
            if (i, total) in dp:
                dp[(i, total)]
            if total == 0:
                return 1
            if total < 0:
                return 0
            if i == len(coins):
                return 0
            else:
                dp[(i, total)] = dfs(i + 1, total) + dfs(i, total - coins[i])
            return dp[(i, total)]

        res = dfs(0, amount)
        return res
    # too slow
    def change2(self, amount: int, coins: list[int]) -> int:
        dp = {}  # (i, total): int

        def dfs(i, total):
            if (i, total) in dp:
                dp[(i, total)]
            if total == 0:
                return 1
            elif total < 0:
                return 0
            else:
                res = 0
                for j in range(i, len(coins)):
                    res += dfs(j, total - coins[j])
                dp[(i, total)] = res
            return dp[(i, total)]

        res = dfs(0, amount)
        print(dp)

        return res


amount, coins = 5, [1, 2, 5]
print(Solution().change(amount, coins))
