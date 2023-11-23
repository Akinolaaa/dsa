# 322- https://leetcode.com/problems/coin-change/
import collections

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # dp solution
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

    # obviously very very slow- added just for the fun of it
    def coinChange1(self, coins: list[int], amount: int) -> int:
        dp = {}
        for c in coins:
            dp[c] = 1

        def bfs(amount):
            q = collections.deque()
            q.append(amount)

            result = 0
            while q:
                result += 1
                for _ in range(len(q)):  # remember it doesn't change
                    total = q.popleft()
                    if total == 0:
                        return result
                    for c in coins:
                        newTot = amount - c
                        if newTot > 0:
                            q.append(newTot)
            return -1

        return bfs(amount)
