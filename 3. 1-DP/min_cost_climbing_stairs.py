# 764 https://leetcode.com/problems/min-cost-climbing-stairs/


class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a, b = 0, cost[-1]

        for c in cost:
            t = a
            a = min(a, b) + c
            b = t

        return min(a, b)
