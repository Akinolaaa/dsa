# 70  https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1

        for _ in range(n - 1):
            t = a
            a = a + b
            b = t

        return a
