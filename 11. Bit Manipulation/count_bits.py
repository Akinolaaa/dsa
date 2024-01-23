# 338- https://leetcode.com/problems/counting-bits/description/


class Solution:
    # better solution- remember binary of 1,2,4,8,16,32,...
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

    def countBits1(self, n: int) -> list[int]:
        res = []
        for num in range(n + 1):
            sol = 0
            while num:
                num = num & (num - 1)
                sol += 1
            res.append(sol)
        return res
